from src.agent.tools.market_tools import (
    market_live_data,
    book_data,
)
import asyncio

async def collect_intelligence_data(intelligence_queries):

    results = await asyncio.gather(
        market_live_data.ainvoke({"query": intelligence_queries.live_market_query}),
        book_data.ainvoke({"query": intelligence_queries.book_query}),
        return_exceptions=True
    )

    return {
        "live_market": results[0],
        "book": results[1],
    }