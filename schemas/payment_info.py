import datetime
from typing import Optional

from pydantic import BaseModel, Field


class PaymentInfoBase(BaseModel):
    vcc_from: Optional[str] = None
    card_type: Optional[str] = None
    revolut_card_used_no: Optional[int] = None
    card_country: Optional[str] = None
    card_address: Optional[str] = None
    multi_use_or_one_time: Optional[str] = None
    card_name_used: Optional[str] = None
    card_number: Optional[str] = None
    expiry_date: Optional[datetime.date] = None
    cvv: Optional[str] = None
    user_id: Optional[int] = Field(
        gt=0, description="User ID must be greater than 0", default=None
    )


class PaymentInfoCreate(PaymentInfoBase):
    pass


class PaymentInfoUpdate(PaymentInfoBase):
    pass


class PaymentInfoRead(PaymentInfoBase):
    id: int

    model_config = {
        "from_attributes": True,
    }
