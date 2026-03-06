from src.agent.trading_signal.decision_schema import DecisionOutput
from src.agent.services.data_collector import collect_data
from src.utils.model_loaders import ModelLoader
from src.agent.services.intell_ret import collect_intelligence_data
from src.agent.services.query_generation import generate_intelligence_queries
from langsmith import traceable

loader = ModelLoader()
llm = loader.load_llm()
structured_llm = llm.with_structured_output(DecisionOutput)

# @traceable(name="make_decision")
# async def make_decision(signal: dict):

#     data = await collect_data(signal)

#     prompt = f"""
#     Trading decision engine.

#     Signal:
#     {signal}

#     Market Data:
#     {data}

#     Return:
#     - BUY or SELL
#     - Confidence (0-1)
#     - Concise reasoning within 50 words
#     JSON only.
#     """

#     return await structured_llm.ainvoke(prompt)

@traceable(name="make_decision")
async def make_decision(signal):

    # Agent 1
    primary_data = await collect_data(signal)
    # print(f"Primary Data: {primary_data}")
    print("================================== Up Data Collector =====================================")

    # Query generator
    intelligence_queries = await generate_intelligence_queries(primary_data)
    # print(f"Intelligence Queries: {intelligence_queries}")
    print("================================== Up Data Intelligence Queries =====================================")

    # Agent 2
    intelligence_data = await collect_intelligence_data(intelligence_queries)
    # print(f"Intelligence Data: {intelligence_data}")
    print("================================== Up Data Intelligence Data =====================================")

    final_data = {
        "primary": primary_data,
        "intelligence": intelligence_data
    }

    prompt = f"""
You are a 50-year veteran stock market trader with deep expertise in:

• Futures & Options (FnO)
• Intraday options trading
• Market sentiment analysis
• Institutional flow and liquidity behavior

You have traded through multiple market cycles and specialize in identifying high-probability **intraday options trades (CALL / PUT)**.

Your task is to analyze market intelligence and determine the best **intraday options action**.

\nTrading Signal:
{signal}

\nMarket Intelligence Data:
{final_data}

Core Principle:

Market sentiment ALWAYS has higher priority than the trading signal.

The signal should be treated only as a **secondary confirmation**, not the primary driver of the decision.

Decision Priority Order:

1️⃣ **Overall Market Sentiment (Most Important)**

* News sentiment
* Institutional activity
* Sector momentum
* Liquidity and volatility conditions

2️⃣ **Contextual Risk Factors**

* Macro events
* Regulatory announcements
* Unexpected market news

3️⃣ **Trading Signal (Least Important)**

* Use the signal only if it aligns with the broader market sentiment.
* If the signal contradicts strong market sentiment, **ignore the signal**.

Instructions:

1. Carefully read ALL the provided data.
2. Some information may be irrelevant or noisy — ignore it.
3. Focus on the information that impacts **intraday price movement and sentiment**.
4. First determine the **overall market sentiment** (bullish, bearish, neutral).
5. Then check if the trading signal supports that sentiment.

Decision Framework:

• Strong bullish sentiment → BUY CALL
• Strong bearish sentiment → BUY PUT
• Weak, mixed, or unclear sentiment → HOLD

Risk Management Rule:

If market sentiment is unclear or conflicting, **choose HOLD** to protect capital.

Think like an experienced intraday options trader who prioritizes **market psychology, liquidity flow, and sentiment over mechanical signals**.

Return ONLY valid JSON in the following format:

{{
"decision": "BUY_CALL | BUY_PUT | HOLD",
"confidence": 0.0-1.0,
"reasoning": "brief explanation emphasizing market sentiment and why the decision was taken"
}}
"""


    # print(prompt)
    result = await structured_llm.ainvoke(prompt)

    return result