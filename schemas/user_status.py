import datetime
from typing import Optional

from pydantic import BaseModel, Field


class UserStatusBase(BaseModel):
    am_password: Optional[str] = None
    active: Optional[str] = None
    device_type: Optional[str] = None
    device_id: Optional[str] = None
    previous_device_connected: Optional[str] = None
    register_date: Optional[datetime.date] = None
    registration_device: Optional[str] = None
    age_in_no_of_days: Optional[int] = None
    user_id: Optional[int] = Field(
        gt=0, description="User ID must be greater than 0", default=None
    )


class UserStatusCreate(UserStatusBase):
    pass


class UserStatusUpdate(UserStatusBase):
    pass


class UserStatusRead(UserStatusBase):
    id: int

    model_config = {
        "from_attributes": True,
    }
