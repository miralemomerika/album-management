import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class UserCreate(UserBase):
    dob: Optional[datetime.date] = None
    business_name: Optional[str] = None
    created_by: Optional[str] = None
    date_created: Optional[datetime.date] = None
    subscription_type: Optional[str] = None
    subscription_status: Optional[str] = None
    cancellation_date: Optional[datetime.date] = None
    skip_trial: Optional[str] = None
    country: Optional[str] = None
    warmup_phase_until: Optional[datetime.date] = None
    address_line_1: Optional[str] = None
    city: Optional[str] = None
    province: Optional[str] = None
    postal_code: Optional[int] = None
    foreign_TIN: Optional[str] = None


class UserUpdate(UserCreate):
    pass


class UserRead(UserCreate):
    id: int

    model_config = {
        "from_attributes": True,
    }
