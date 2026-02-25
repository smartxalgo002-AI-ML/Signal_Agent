import asyncio
import json

from src.agent.tools.market_tools import (
    news_vector_db,
    financial_data,
    historical_model,
    market_live_data,
    book_data,
)
from src.agent.tools.tavily_tool import get_tavily
from datetime import datetime

tavily_tool = get_tavily()

# async def collect_data(signal: dict):

#     symbol = signal.get("underlyingSymbol", "")
#     exchange = signal.get("exch", "")
#     date = signal.get("lttDate", "")

#     query = f"Latest news about {symbol} stock on {exchange} market around {date}"
    
#     results = await asyncio.gather(
#         news_vector_db.ainvoke({"query": query}),
#         financial_data.ainvoke({"query": symbol}),
#         tavily_tool.ainvoke(query),
#         historical_model.ainvoke({"query": json.dumps(signal)}),
#         market_live_data.ainvoke({"query": query}),
#         book_data.ainvoke({"query": query}),
#         return_exceptions=True
#     )

#     return {
#         "news": results[0],
#         "financial": results[1],
#         "search": results[2],
#         "historical": results[3],
#         "live_market": results[4],
#         "book": results[5],
#     }

from langsmith import traceable

@traceable(name="collect_data")
async def collect_data(signal: dict):

    instrument = signal.get("signal", {}).get("instrument", {})
    market_data = instrument.get("marketData", {})

    symbol = market_data.get("displayName") or market_data.get("underlyingSymbol", "")
    exchange = market_data.get("exch", "")

    # Current date and time
    now = datetime.now()

    # Extract date
    current_date = now.date()   

    query = f"""
    Latest macro news, FII/DII activity, derivatives positioning 
    and market sentiment for {symbol} index on {exchange} exchange 
    around {now}. 
    Trading date: {current_date}.
    Include derivatives positioning and volatility context.
    """
    print(query)

    results = await asyncio.gather(
        news_vector_db.ainvoke({"query": query}),
        financial_data.ainvoke({"query": symbol}),
        tavily_tool.ainvoke(query),
        historical_model.ainvoke({"query": json.dumps(signal)}),
        market_live_data.ainvoke({"query": query}),
        book_data.ainvoke({"query": query}),
        return_exceptions=True
    )

    return {
        "news": results[0],
        "financial": results[1],
        "search": results[2],
        "historical": results[3],
        "live_market": results[4],
        "book": results[5],
    }