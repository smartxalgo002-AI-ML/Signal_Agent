from typing import Annotated
from typing import Literal
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool
from langchain_experimental.utilities import PythonREPL
from typing_extensions import TypedDict
from langgraph.graph import MessagesState, END,StateGraph, START
from langgraph.types import Command
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent

import asyncio
import json
import re
from typing import Annotated
from pydantic import BaseModel, Field
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

import os
from dotenv import load_dotenv # Install with: pip install python-dotenv

load_dotenv() 
api_key = os.getenv("TAVILY_API_KEY")
print(f"Key loaded: {api_key}") # Verify it works without printing the whole key

from langchain_google_genai import ChatGoogleGenerativeAI

# llm = ChatGoogleGenerativeAI(model='gemini-2.5-pro') # Also correcting model name to a likely intended valid one
# response = llm.invoke("what is capital of USA?")
# print(response.content)
# gemini_model = llm # Keep for downstream use

from src.utils.model_loaders import ModelLoader

loader = ModelLoader()
llm = loader.load_llm()

# response = llm.invoke("What is the current stock price of Reliance Industries?")
# print(response.text)

tavaily_tool=TavilySearchResults()
news = tavaily_tool.invoke("what is a gdp?")
print(news)

@tool
def news_vector_db(query: Annotated[str, "News query"]):
    """Retrieve latest relevant news for a stock."""
    return "This is the News data"


@tool
def financial_data(query: Annotated[str, "Financial query"]):
    """Retrieve latest financial fundamentals for a stock."""
    return "This is the Financial data"


@tool
def historical_model(query: Annotated[str, "OHLCV data"]):
    """Predict next-minute movement using historical OHLCV indicators."""
    return "This is the Historical model output"


@tool
def market_live_data(query: Annotated[str, "Live market query"]):
    """Retrieve live market technical data for a stock."""
    return "This is the Market live data"


@tool
def book_data(query: Annotated[str, "Book query"]):
    """Retrieve relevant stock market book knowledge."""
    return "This is the Book data"



with open(r"src\agent\experiment\signal.txt", "r", encoding="utf-8") as file:
    raw = file.read()

# 1️⃣ Remove newlines (optional)
raw = raw.strip()

# 2️⃣ Replace single quotes with double quotes
raw = raw.replace("'", '"')

# 3️⃣ Quote unquoted keys
# symbol: → "symbol":
raw = re.sub(r'([{,]\s*)(\w+)\s*:', r'\1"\2":', raw)

# 4️⃣ Quote ISO datetime values if not quoted
# 2026-02-13T15:59:32.000Z → "2026-02-13T15:59:32.000Z"
raw = re.sub(
    r':\s*(\d{4}-\d{2}-\d{2}T[0-9:\.\-Z]+)',
    r': "\1"',
    raw
)

# 5️⃣ Replace undefined with null
raw = raw.replace("undefined", "null")

# 6️⃣ Remove trailing commas before } or ]
raw = re.sub(r',\s*([}\]])', r'\1', raw)

# Now parse
signal = json.loads(raw)

print("Parsed Signal:", signal)
print("=="*100)

class DecisionOutput(BaseModel):
    decision: str = Field(description="BUY or SELL")
    confidence: float = Field(description="Confidence between 0 and 1")
    reason: str = Field(description="Concise evidence-based reasoning")

structured_llm = llm.with_structured_output(DecisionOutput)

async def collect_data(signal):

    symbol = signal.get("underlyingSymbol", "")
    exchange = signal.get("exch", "")
    date = signal.get("lttDate", "")

    query = f"Latest news about {symbol} stock on {exchange} market around {date}"

    results = await asyncio.gather(
        news_vector_db.ainvoke({"query": query}),
        financial_data.ainvoke({"query": query}),
        tavaily_tool.ainvoke(query),
        historical_model.ainvoke({"query": json.dumps(signal)}),
        market_live_data.ainvoke({"query": query}),
        book_data.ainvoke({"query": query}),
        return_exceptions=True  # IMPORTANT
    )

    print("Results:", results)

    return {
        "news": results[0],
        "financial": results[1],
        "search": results[2],
        "historical": results[3],
        "live_market": results[4],
        "book": results[5],
    }


async def make_decision(signal):

    data = await collect_data(signal)

    prompt = f"""
    Trading decision engine.
    Evaluate signal and market intelligence.

    Signal:
    {signal}

    Market Data:
    {data}

    Return:
    - BUY or SELL
    - Confidence (0-1)
    - Concise evidence reasoning
    JSON only.
    """

    result = await structured_llm.ainvoke(prompt)

    return result

async def main():

    decision = await make_decision(signal)

    print("Final Decision:")
    print(decision.model_dump_json(indent=2))

asyncio.run(main())
