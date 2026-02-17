from src.agent.trading_signal.decision_schema import DecisionOutput
from src.agent.services.data_collector import collect_data
from src.utils.model_loaders import ModelLoader

loader = ModelLoader()
llm = loader.load_llm()
structured_llm = llm.with_structured_output(DecisionOutput)

async def make_decision(signal: dict):

    data = await collect_data(signal)

    prompt = f"""
    Trading decision engine.

    Signal:
    {signal}

    Market Data:
    {data}

    Return:
    - BUY or SELL
    - Confidence (0-1)
    - Concise reasoning
    JSON only.
    """

    return await structured_llm.ainvoke(prompt)
