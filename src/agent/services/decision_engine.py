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
    Trading decision engine.

    Signal:
    {signal}

    All Market Intelligence:
    {final_data}

    Return:
    - BUY or SELL
    - Confidence (0-1)
    - Concise reasoning
    JSON only.
    """

    result = await structured_llm.ainvoke(prompt)

    return result