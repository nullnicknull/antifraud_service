from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field

class LoanHistoryItem(BaseModel):
    amount: float
    loan_data: date
    is_closed: bool

class AntifraudRequest(BaseModel):
    birth_date: date
    phone_number: str
    loans_history: List[LoanHistoryItem]

class AntifraudResponse(BaseModel):
    stop_factors: List[str]
    result: bool