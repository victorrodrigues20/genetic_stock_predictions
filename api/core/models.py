from pydantic import BaseModel

class PredictPayload(BaseModel):
    ticker: str
    volume: float
    prev_close: float