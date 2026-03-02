from pydantic import BaseModel, Field

class DecisionOutput(BaseModel):
    decision: str = Field(description="BUY or SELL")
    confidence: float = Field(description="Confidence between 0 and 1")
    reason: str = Field(description="Concise reasoning")

class IntelligenceQuery(BaseModel):
    live_market_query: str = Field(description="Query for live technical market data")
    book_query: str = Field(description="Query for trading book knowledge")