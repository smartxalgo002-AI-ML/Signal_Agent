from typing import Annotated
from langchain.tools import tool

from src.market_live_rag.data_ingestion.ingestion_pipeline import DataIngestion
from src.sm_book_rag.data_ingestion.ingestion_pipeline import BookIngestionPipeline
from src.financial_data_rag.retriver import Neo4jCypherPipeline
from src.financial_data_rag.retriver2 import get_metrics

@tool
def news_vector_db(query: Annotated[str, "News query"]):
    """Retrieve latest relevant news for a stock."""
    return "This is the News data"

# @tool
# def financial_data(query: Annotated[str, "Financial query"]):
#     """Retrieve latest financial fundamentals for a stock."""
#     return "This is the Financial data"

@tool
def financial_data(query: Annotated[str, "Financial query"]):
    """Retrieve latest financial fundamentals for a stock."""

    metrics = [
        "Sales",
        "Profit before tax",

        "No. of Shareholders",
        "FIIs ",
        "DIIs ",
        "Public"

    ]

    answer = get_metrics(query, metrics)

    # print("\nFinal Output:\n")

    # for row in data:
    # print(answer)

    return answer


@tool
def historical_model(query: Annotated[str, "OHLCV data"]):
    """Predict next-minute movement using historical OHLCV indicators."""
    return "This is the Historical model output"


# @tool
# def market_live_data(query: Annotated[str, "Live market query"]):
#     """Retrieve live market technical data for a stock."""
#     data_ingestion = DataIngestion()
#     file_path = r"src\market_live_rag\data\json_data\Markets.json"
#     data_ingestion.run_pipeline(file_path)
#     results = data_ingestion.query_vector_db(query)
#     # print(results)
#     return results

# ✅ Create ONE global instance
# data_ingestion = DataIngestion()
# file_path = r"src\market_live_rag\data\json_data\Markets.json"
# data_ingestion.run_pipeline(file_path)
@tool
def market_live_data(query: Annotated[str, "Live market query"]):
    """Retrieve live market technical data for a stock."""
    # results = data_ingestion.query_vector_db(query)
    return results

book_data_ingestion = BookIngestionPipeline()
file_path = r"src\sm_book_rag\data\markdown_folder"
book_data_ingestion.run_pipeline(file_path)
@tool
def book_data(query: Annotated[str, "Book query"]):
    """Retrieve relevant stock market book knowledge."""
    results = book_data_ingestion.query_vector_db(query)
    # print(results)
    return results
