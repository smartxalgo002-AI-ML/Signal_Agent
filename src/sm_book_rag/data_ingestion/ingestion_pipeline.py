import os
import sys
from typing import List
from collections import OrderedDict
from dotenv import load_dotenv

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.retrievers import BM25Retriever
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage

from src.exception import SignalAgentException
from src.utils.model_loaders import ModelLoader
from src.aws.s3_downloader import download_s3_folder


class BookIngestionPipeline:
    """
    Hybrid BM25 + Vector Retrieval + LLM summarization pipeline for book markdown files.
    """

    def __init__(self):
        try:
            print("Initializing Book Pipeline...")

            load_dotenv()
            self._load_env_variables()

            # 🔹 Ensure data folder exists
            self._ensure_data_folder()

            # ✅ Load embedding once
            self.model_loader = ModelLoader()
            self.embeddings = self.model_loader.load_embeddings()

            # ✅ Setup persist directory
            self.persist_directory = r"src\sm_book_rag\data\vector_data\book_vdb_latest"

            # Runtime objects
            self.chroma_vdb = None
            self.bm25_retriever = None

        except Exception as e:
            raise SignalAgentException(e, sys)

    # --------------------------------------------------
    # 1️⃣ ENV VALIDATION
    # --------------------------------------------------
    def _load_env_variables(self):
        required_vars = ["GOOGLE_API_KEY"]
        missing_vars = [var for var in required_vars if os.getenv(var) is None]

        if missing_vars:
            raise EnvironmentError(f"Missing environment variables: {missing_vars}")

    def _ensure_data_folder(self):
        """
        If local data folder does not exist → download from S3.
        """

        local_data_path = r"src\sm_book_rag\data"

        if not os.path.exists(local_data_path):
            print("\nLocal data folder not found. Downloading from S3...\n")

            download_s3_folder(
                bucket_name="utk-signal-agent",
                s3_prefix="book_rag_data/",
                local_dir=local_data_path
            )

            print("\nS3 data download completed.\n")

        else:
            print("Local data folder exists. Skipping S3 download.")

    # --------------------------------------------------
    # 2️⃣ LOAD DOCUMENTS
    # --------------------------------------------------
    def load_documents(self, folder_path: str) -> List[Document]:
        try:
            print(f"Loading markdown files from: {folder_path}")

            documents = []

            for file in os.listdir(folder_path):
                if file.lower().endswith(".md"):
                    with open(os.path.join(folder_path, file), "r", encoding="utf-8") as f:
                        documents.append(
                            Document(
                                page_content=f.read(),
                                metadata={"source": file}
                            )
                        )

            print(f"Loaded {len(documents)} documents")
            return documents

        except Exception as e:
            raise SignalAgentException(e, sys)

    # --------------------------------------------------
    # 3️⃣ STORE IN VECTOR DB
    # --------------------------------------------------
    def store_in_vector_db(self, documents: List[Document]):
        try:
            print("Preparing hybrid retrievers...")

            # Split docs
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=2000,
                chunk_overlap=300
            )

            split_docs = splitter.split_documents(documents)

            # BM25
            self.bm25_retriever = BM25Retriever.from_documents(split_docs)
            self.bm25_retriever.k = 5

            # Chroma
            if os.path.exists(self.persist_directory) and os.listdir(self.persist_directory):
                print("Loading existing vector DB...")
                self.chroma_vdb = Chroma(
                    persist_directory=self.persist_directory,
                    embedding_function=self.embeddings
                )
            else:
                print("Creating new vector DB...")
                self.chroma_vdb = Chroma.from_documents(
                    documents=split_docs,
                    embedding=self.embeddings,
                    persist_directory=self.persist_directory
                )
                self.chroma_vdb.persist()

            print("Hybrid retrievers ready.")

        except Exception as e:
            raise SignalAgentException(e, sys)

    # --------------------------------------------------
    # 4️⃣ RUN PIPELINE (ONE TIME SETUP)
    # --------------------------------------------------
    def run_pipeline(self, folder_path: str):
        docs = self.load_documents(folder_path)

        if not docs:
            print("No documents found.")
            return

        self.store_in_vector_db(docs)

    # --------------------------------------------------
    # 5️⃣ QUERY METHOD
    # --------------------------------------------------
    def query_vector_db(self, query: str):

        try:
            if self.chroma_vdb is None or self.bm25_retriever is None:
                raise ValueError("Pipeline not initialized. Run run_pipeline() first.")

            vector_retriever = self.chroma_vdb.as_retriever(search_kwargs={"k": 5})

            bm25_docs = self.bm25_retriever.invoke(query)
            vector_docs = vector_retriever.invoke(query)

            # Deduplicate
            docs = OrderedDict()
            for d in bm25_docs + vector_docs:
                docs[d.page_content] = d

            search_results = list(docs.values())

            context = "\n".join([doc.page_content for doc in search_results])

            return context

        except Exception as e:
            raise SignalAgentException(e, sys)


# --------------------------------------------------
# MAIN
# --------------------------------------------------

if __name__ == "__main__":

    pipeline = BookIngestionPipeline()

    folder_path = r"src\sm_book_rag\data\markdown_folder"

    # Setup only once
    pipeline.run_pipeline(folder_path)

    print("\nBook RAG Ready. Type 'exit' to quit.\n")

    while True:
        query = input("Enter your query: ")

        if query.lower() in ["exit", "quit", "q"]:
            print("Exiting...")
            break

        result = pipeline.query_vector_db(query)

        print("\n--- Response ---\n")
        print(result)
        print("\n" + "=" * 80 + "\n")
