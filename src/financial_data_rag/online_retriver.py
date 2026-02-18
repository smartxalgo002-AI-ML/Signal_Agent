import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_neo4j import Neo4jGraph, GraphCypherQAChain

from langchain_core.prompts.prompt import PromptTemplate

from neo4j import GraphDatabase
from langchain_neo4j import Neo4jGraph

from dotenv import load_dotenv # Install with: pip install python-dotenv

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
load_dotenv(BASE_DIR / ".env")

NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

# print(NEO4J_URI)
# print(NEO4J_USER)
# print(NEO4J_PASSWORD)

# ✅ Initialize graph FIRST
graph = Neo4jGraph(
    url=NEO4J_URI,
    username=NEO4J_USER,
    password=NEO4J_PASSWORD,
    database="a1983859"
)


def get_metrics(company_name: str, metrics: list):

    conditions = " OR ".join(
        [f"toLower(m.name) CONTAINS '{m.strip().lower()}'" for m in metrics]
    )

    query = f"""
    MATCH (c:Company)-[r:HAS_METRIC]->(m:Metric)
    WHERE toLower(c.name) = toLower('{company_name}')
      AND ({conditions})
    RETURN r.period AS Period,
           m.name AS Metric,
           r.value AS Value
    ORDER BY Period DESC
    LIMIT 100
    """

    return graph.query(query)


if __name__ == "__main__":

    metrics = [
        "Sales",
        "Profit before tax",
        "Expenses",
        "Operating Profit",
        "OPM %",
        "Interest",
        "Depreciation",
        "Net Profit",
        "EPS in Rs"

    ]

    data = get_metrics("RELIANCE", metrics)
    print(data)

    print("\nFinal Output:\n")

    for row in data:
        print(row)
