import requests
from datetime import datetime, timedelta
from langchain_core.documents import Document
from langchain_community.retrievers import BM25Retriever


def fetch_news(api_url: str):
    """Fetch news from API"""
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()


def filter_recent_news(data, hours: int = 24):
    """Filter news within given hours"""
    documents = []

    now = datetime.now()
    time_limit = now - timedelta(hours=hours)

    for item in data:
        published_time = datetime.fromisoformat(item["published_time"])

        if published_time >= time_limit:
            documents.append(
                Document(
                    page_content=item["content"],
                    metadata={
                        "headline": item["headline"],
                        "published_time": item["published_time"]
                    }
                )
            )

    return documents


def build_retriever(documents, k: int = 3):
    """Create BM25 retriever"""
    retriever = BM25Retriever.from_documents(documents)
    retriever.k = k
    return retriever


def ingest_news(api_url: str, hours: int = 24, k: int = 3):
    """Complete ingestion pipeline"""
    raw_data = fetch_news(api_url)
    documents = filter_recent_news(raw_data, hours)

    print(f"Documents after filtering: {len(documents)}")

    retriever = build_retriever(documents, k)

    return retriever


if __name__ == "__main__":

    API_URL = "http://127.0.0.1:8000/news"

    retriever = ingest_news(API_URL, hours=24, k=3)

    query = "bank"

    results = retriever.invoke(query)

    for doc in results:
        print("================================================")
        print(f"Meta Data: {doc.metadata}")
        print("*************************")
        print(f"Content: {doc.page_content}")