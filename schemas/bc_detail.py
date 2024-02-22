from typing import Optional

from pydantic import BaseModel


class BCDetailBase(BaseModel):
    browser_user: Optional[str] = None
    serial_number: Optional[str] = None
    account_id: Optional[str] = None
    vpn_used: Optional[str] = None
    vpn_id: Optional[str] = None
    ip_used: Optional[str] = None
    ip_country: Optional[str] = None


class BCDetailCreate(BCDetailBase):
    pass


class BCDetailUpdate(BCDetailBase):
    pass


class BCDetailRead(BCDetailBase):
    id: int

    model_config = {
        "from_attributes": True,
    }
