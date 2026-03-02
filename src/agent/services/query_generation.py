from langsmith import traceable
from src.utils.model_loaders import ModelLoader
import asyncio
from src.agent.trading_signal.decision_schema import IntelligenceQuery   # src\agent\trading_signal\decision_schema.py

loader = ModelLoader()
llm = loader.load_llm()
intelligence_llm = llm.with_structured_output(IntelligenceQuery)

@traceable(name="query_generation")
async def generate_intelligence_queries(primary_data):

    prompt = f"""
    You are a market intelligence query generator.

    Primary Data:
    {primary_data}

    Task:
    1. Create a live technical market query incorporating:
       - current trend
       - momentum
       - intraday bias
       - volatility context

    2. Create a book knowledge query incorporating:
       - relevant trading strategy
       - trend continuation or reversal theory
       - risk management principle

    Return structured output only.
    """

    print(f"Prompt: {prompt}")
    print("=========================================== Prompt ================================================")

    queries = await intelligence_llm.ainvoke(prompt)

    return queries