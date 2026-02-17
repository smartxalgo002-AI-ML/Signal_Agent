import os
from dotenv import load_dotenv
# from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from src.utils.config_loader import load_config
from langchain_groq import ChatGroq
from src.exception import SignalAgentException
import sys

class ModelLoader:
    """
    A utility class to load embedding models and LLM models.
    """
    def __init__(self):
        load_dotenv()
        self._validate_env()
        self.config=load_config()

    def _validate_env(self):
        """
        Validates the environment variables.
        """
        try:
            required_vars = ["GOOGLE_API_KEY"]
            self.google_api_key=os.getenv("GOOGLE_API_KEY")
            missing_vars = [var for var in required_vars if not os.getenv(var)]
            if missing_vars:
                raise EnvironmentError(f"Missing environment variables: {missing_vars}")
        except Exception as e:
            raise SignalAgentException(e, sys)

    def load_embeddings(self):
        """
        Load and return the embedding model.
        """
        print("Loading Embedding model")
        model_name=self.config["embedding_model"]["model_name"]
        return HuggingFaceEmbeddings(model_name=model_name)

    def load_llm(self):
        """
        Load and return the LLM model.
        """
        print("LLM loading...")
        model_name=self.config["llm"]["google"]["model_name"]
        gemini_model=ChatGoogleGenerativeAI(model=model_name, streaming=True)
        
        return gemini_model  # Placeholder for future LLM loading
    
if __name__ == "__main__":
    model_loader = ModelLoader()
    # print(model_loader.load_llm())
    llm = model_loader.load_llm()
    response = llm.invoke("What is the current stock price of Reliance Industries?")
    # for chunk in response:
    #     print(chunk.text, end="", flush=True)
    print(response.text)