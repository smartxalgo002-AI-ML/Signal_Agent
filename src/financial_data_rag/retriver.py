import os
import sys
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_neo4j import Neo4jGraph, GraphCypherQAChain
from langchain_core.prompts import PromptTemplate

from src.exception import SignalAgentException


class Neo4jCypherPipeline:
    """
    Production-ready Neo4j + Gemini Cypher QA pipeline.
    """

    def __init__(self):
        try:
            print("Initializing Neo4j Cypher Pipeline...")

            self._load_env_variables()

            self.llm = self._init_llm()
            self.graph = self._init_graph()
            self.chain = self._build_chain()

        except Exception as e:
            raise SignalAgentException(e, sys)

    # ---------------------------------------------------
    # 1️⃣ ENV VALIDATION
    # ---------------------------------------------------
    def _load_env_variables(self):
        load_dotenv()

        required_vars = ["GOOGLE_API_KEY"]
        missing_vars = [var for var in required_vars if os.getenv(var) is None]

        if missing_vars:
            raise EnvironmentError(f"Missing environment variables: {missing_vars}")

    # ---------------------------------------------------
    # 2️⃣ INIT LLM
    # ---------------------------------------------------
    def _init_llm(self):
        print("Loading Gemini LLM...")
        return ChatGoogleGenerativeAI(model="gemini-2.5-pro")

    # ---------------------------------------------------
    # 3️⃣ INIT NEO4J GRAPH
    # ---------------------------------------------------
    def _init_graph(self):
        print("Connecting to Neo4j...")

        return Neo4jGraph(
            url="bolt://localhost:7687",
            username="neo4j",
            password="password123",
            database="financialdata"
        )

    # ---------------------------------------------------
    # 4️⃣ BUILD CYPHER CHAIN
    # ---------------------------------------------------
    def _build_chain(self):

        CYPHER_GENERATION_TEMPLATE = """
Task: Generate Cypher statement to query a graph database.

Instructions:
1. Use only the provided schema: {schema}
2. If multiple metrics requested, return them in same row.
3. Match Company first.
4. Match separate Metric nodes sharing SAME period.
5. Use CONTAINS for metric names.

Example:
MATCH (c:Company) WHERE toLower(c.name) CONTAINS '3mindia'
MATCH (c)-[r1:HAS_METRIC]->(m1:Metric) WHERE toLower(m1.name) CONTAINS 'sales'
MATCH (c)-[r2:HAS_METRIC]->(m2:Metric)
WHERE toLower(m2.name) CONTAINS 'profit before tax'
AND r1.period = r2.period
RETURN r1.period AS Period, r1.value AS Sales, r2.value AS Profit
ORDER BY Period DESC

The question is:
{question}
"""

        cypher_prompt = PromptTemplate(
            template=CYPHER_GENERATION_TEMPLATE,
            input_variables=["schema", "question"]
        )

        print("Building GraphCypherQAChain...")

        return GraphCypherQAChain.from_llm(
            llm=self.llm,
            graph=self.graph,
            top_k=50,
            verbose=True,
            cypher_prompt=cypher_prompt,
            allow_dangerous_requests=True,
            return_intermediate_steps=True
        )

    # ---------------------------------------------------
    # 5️⃣ QUERY METHOD
    # ---------------------------------------------------
    def query(self, question: str):

        try:
            result = self.chain.invoke({"query": question})

            print("\nGenerated Cypher:")
            print(result["intermediate_steps"][0]["query"])

            print("\nRaw Neo4j Context:")
            print(result["intermediate_steps"][1]["context"])

            return result["result"]

        except Exception as e:
            raise SignalAgentException(e, sys)


# ---------------------------------------------------
# MAIN
# ---------------------------------------------------

if __name__ == "__main__":

    pipeline = Neo4jCypherPipeline()

    print("\nNeo4j Cypher QA Ready. Type 'exit' to quit.\n")

    while True:
        query = input("Enter your question: ")

        if query.lower() in ["exit", "quit", "q"]:
            print("Exiting...")
            break

        answer = pipeline.query(query)

        print("\nFinal Answer:")
        print(answer)
        print("\n" + "=" * 80 + "\n")
