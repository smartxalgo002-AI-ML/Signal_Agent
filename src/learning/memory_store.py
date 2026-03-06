import json
import uuid
from datetime import datetime
import chromadb
from chromadb.utils import embedding_functions


class ExperienceMemory:

    def __init__(self):

        # embedding model
        self.embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )

        # persistent DB
        self.client = chromadb.Client(
            chromadb.config.Settings(
                persist_directory="memory_chroma_db"
            )
        )

        self.collection = self.client.get_or_create_collection(
            name="trading_experiences",
            embedding_function=self.embedding_function
        )

    # ==============================
    # STORE EXPERIENCE
    # ==============================

    def store_experience(self, signal, decision, pnl, lesson):

        experience = {
            "signal": signal,
            "decision": decision,
            "pnl": pnl,
            "lesson": lesson,
            "timestamp": str(datetime.utcnow())
        }

        doc = json.dumps(experience)

        self.collection.add(
            documents=[doc],
            metadatas=[{
                "decision": decision,
                "pnl": pnl
            }],
            ids=[str(uuid.uuid4())]
        )

    # ==============================
    # RETRIEVE SIMILAR EXPERIENCES
    # ==============================

    def retrieve_similar(self, signal, k=5):

        signal_text = json.dumps(signal)

        results = self.collection.query(
            query_texts=[signal_text],
            n_results=k
        )

        experiences = []

        if results["documents"]:
            for doc in results["documents"][0]:
                experiences.append(json.loads(doc))

        return experiences