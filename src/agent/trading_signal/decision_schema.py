from pydantic import BaseModel, Field

class DecisionOutput(BaseModel):
    decision: str = Field(description="BUY or SELL")
    confidence: float = Field(description="Confidence between 0 and 1")
    reason: str = Field(description="Concise reasoning")
