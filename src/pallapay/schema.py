import datetime
from typing import Any
from pydantic import BaseModel


class CreatePaymentRequestModel(BaseModel):
    merchant: str
    order: str
    amount: float
    currency: str
    first_name: str
    last_name: str
    email: str
    custom: Any = None

    class Config:
        fields = {
            'type': 'payment_type'
        }


class CreatePaymentResponseModel(BaseModel):
    redirect_to_url: str
