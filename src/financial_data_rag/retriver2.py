import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_neo4j import Neo4jGraph, GraphCypherQAChain

from langchain_core.prompts.prompt import PromptTemplate

from neo4j import GraphDatabase
from langchain_neo4j import Neo4jGraph

# ✅ Initialize graph FIRST
graph = Neo4jGraph(
    url="bolt://localhost:7687",
    username="neo4j",
    password="password123",
    database="financialdata"
)

def get_metrics(company_name: str, metrics: list):

    match_clause = ""
    return_clause = "r1.period AS Period"

    for idx, metric in enumerate(metrics):
        metric_clean = metric.lower().strip()

        if idx == 0:
            match_clause += f"""
            MATCH (c)-[r1:HAS_METRIC]->(m1:Metric)
            WHERE toLower(m1.name) CONTAINS '{metric_clean}'
            """
            return_clause += f", r1.value AS `{metric}`"
        else:
            match_clause += f"""
            MATCH (c)-[r{idx+1}:HAS_METRIC]->(m{idx+1}:Metric)
            WHERE toLower(m{idx+1}.name) CONTAINS '{metric_clean}'
                  AND r1.period = r{idx+1}.period
            """
            return_clause += f", r{idx+1}.value AS `{metric}`"

    query = f"""
    MATCH (c:Company)
    WHERE toLower(c.name) CONTAINS toLower('{company_name}')
    {match_clause}
    RETURN {return_clause}
    ORDER BY Period DESC
    LIMIT 5
    """

    # print("\nGenerated Query:\n", query)

    result = graph.query(query)

    # print("\nRaw Result:\n", result)

    return result

if __name__ == "__main__":

    metrics = [
        "Sales",
        "Profit before tax",

        "No. of Shareholders",
        "FIIs ",
        "DIIs ",
        "Public"

    ]

    data = get_metrics("3MINDIA", metrics)

    print("\nFinal Output:\n")

    for row in data:
        print(row)
