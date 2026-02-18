import json
import os
from typing import List

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

from src.logger import logging
from src.exception import SignalAgentException
from src.utils.model_loaders import ModelLoader
from src.utils.config_loader import load_config
from dotenv import load_dotenv

import sys

class DataIngestion:
    """
    Class to handle document loading, transformation and ingestion into Pinecone vector store.
    """
    def __init__(self):
        """
        Initializes the DataIngestion class.
        """

        try:
            print("Initializing DataIngestion pipeline...")
            self.model_loader = ModelLoader()
            self._load_env_variables()
            self.config = load_config()

            # ✅ Load embeddings ONCE
            self.embeddings = self.model_loader.load_embeddings()

            # ✅ Setup persist directory once
            index_name = self.config["vector_db"]["index_name"]
            self.persist_directory = r"src\market_live_rag\data\vector_data"

            # ✅ Initialize vector DB once (may be empty first run)
            self.chroma_vdb = None

        except Exception as e:
            raise SignalAgentException(e, sys)

    def _load_env_variables(self):
        try:
            load_dotenv()

            required_vars = [
                "GOOGLE_API_KEY",
                "TAVILY_API_KEY"
            ]

            missing_vars = [var for var in required_vars if os.getenv(var) is None]
            if missing_vars:
                raise EnvironmentError(f"Missing environment variables: {missing_vars}")

            self.google_api_key = os.getenv("GOOGLE_API_KEY")
            self.tavily_api_key = os.getenv("TAVILY_API_KEY")

        except Exception as e:
            raise SignalAgentException(e, sys)

    def load_json_documents(self, file_path: str) -> List[Document]:
        """
        Load JSON market data file and convert into LangChain Documents.
        """
        try:
            # logging.info(f"Loading JSON file from: {file_path}")
            print(f"Loading JSON file from: {file_path}")

            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File not found: {file_path}")

            with open(file_path, 'r', encoding='utf-8') as f:
                raw_data = json.load(f)

            documents = []

            for entry in raw_data:
                combined_content = (
                    f"Date: {entry.get('publication_date')}\n"
                    f"Title: {entry.get('title')}\n\n"
                    f"Content: {entry.get('full_text')}"
                )

                metadata = {
                    "url": entry.get("url"),
                    "title": entry.get("title"),
                }

                documents.append(
                    Document(
                        page_content=combined_content,
                        metadata=metadata
                    )
                )

            # logging.info(f"Loaded {len(documents)} documents successfully.")
            print(f"Loaded {len(documents)} documents successfully.")
            return documents

        except Exception as e:
            raise SignalAgentException(e, sys)

    def store_in_vector_db(self, documents: List[Document]):
        """
        Split documents and store them in Chroma vector database.
        If DB exists → load it.
        If not → create and ingest.
        """

        try:
            print("Starting vector DB ingestion...")

            # ----------------------------------------
            # 1️⃣ If DB already exists → load & exit
            # ----------------------------------------
            if os.path.exists(self.persist_directory) and os.listdir(self.persist_directory):
                print("Vector DB already exists. Loading existing DB...")
                self.chroma_vdb = Chroma(
                    embedding_function=self.embeddings,
                    persist_directory=self.persist_directory
                )
                print("Vector DB loaded successfully.")
                return self.chroma_vdb

            # ----------------------------------------
            # 2️⃣ Otherwise → Create & Ingest
            # ----------------------------------------
            print("No existing DB found. Creating new one...")

            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=2000,
                chunk_overlap=300,
                separators=["\n\n", "\n", ".", " "],
                length_function=len
            )

            split_docs = text_splitter.split_documents(documents)
            total_docs = len(split_docs)

            print(f"Total split documents: {total_docs}")

            BATCH_SIZE = 2000
            chroma_vdb = None

            for start in range(0, total_docs, BATCH_SIZE):
                end = min(start + BATCH_SIZE, total_docs)
                batch = split_docs[start:end]

                if chroma_vdb is None:
                    chroma_vdb = Chroma.from_documents(
                        documents=batch,
                        embedding=self.embeddings,
                        persist_directory=self.persist_directory
                    )
                else:
                    chroma_vdb.add_documents(batch)

                print(f"Ingested {end}/{total_docs} documents "
                    f"({total_docs - end} remaining)")

            chroma_vdb.persist()

            print("Vector DB ingestion completed successfully.")
            return chroma_vdb

        except Exception as e:
            raise SignalAgentException(e, sys)

    def run_pipeline(self, uploaded_files):
        try:
            documents = self.load_json_documents(uploaded_files)
            if not documents:
                print("No valid documents found.")
                return
            self.vector_db = self.store_in_vector_db(documents)
        except Exception as e:
            raise SignalAgentException(e, sys)

    def query_vector_db(self, query: str):

        try:
            if self.vector_db is None:
                raise ValueError("Vector DB not initialized.")

            retriever = self.vector_db.as_retriever(
                search_kwargs={"k": self.config["retriever"]["top_k"]}
            )

            return retriever.invoke(query)

        except Exception as e:
            raise SignalAgentException(e, sys)



if __name__ == "__main__":
    data_ingestion = DataIngestion()

    file_path = r"src\market_live_rag\data\json_data\Markets.json"

    # Step 1: Ensure DB exists (runs only once)
    data_ingestion.run_pipeline(file_path)

    print("\nVector DB Ready. Type 'exit' to quit.\n")

    while True:
        query = input("Enter your query: ")

        if query.lower() in ["exit", "quit", "q"]:
            print("Exiting...")
            break

        results = data_ingestion.query_vector_db(query)

        if not results:
            print("No relevant documents found.\n")
            continue

        print("\n--- Retrieved Results ---\n")

        for i, doc in enumerate(results, 1):
            print(f"\nResult {i}:")
            print(doc.page_content[:500])
            print("-" * 50)

        print("\n") 