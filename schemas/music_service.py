import datetime
from typing import Optional

from pydantic import BaseModel, Field


class MusicServiceBase(BaseModel):
    service_name: Optional[str] = None
    plan_type: Optional[str] = None
    payment_method_used: Optional[str] = None
    first_payment_date: Optional[datetime.date] = None
    adspower_serial: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    phone_number: Optional[str] = None
    sms_inbox_link: Optional[str] = None
    cc_details_url: Optional[str] = None
    user_id: Optional[int] = Field(
        gt=0, description="User ID must be greater than 0", default=None
    )


class MusicServiceCreate(MusicServiceBase):
    pass


class MusicServiceUpdate(MusicServiceBase):
    pass


class MusicServiceRead(MusicServiceBase):
    id: int

    model_config = {
        "from_attributes": True,
    }
