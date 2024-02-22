from typing import Optional

from pydantic import BaseModel, Field


class DistributorBase(BaseModel):
    name: Optional[str] = None
    details: Optional[dict] = None
    pricing_per_year: Optional[str] = None
    recommended: Optional[bool] = None
    paypal_support: Optional[bool] = None
    sepa_support: Optional[bool] = None
    commission_percentage: Optional[float] = None
    approval_time_no_days_on_avg: Optional[float] = None
    closes_account_on_copyright_strike: Optional[bool] = None
    warns_on_excessive_streaming: Optional[bool] = None
    offers_label_accounts: Optional[bool] = None
    browser_details_id: Optional[int] = Field(
        gt=0,
        description="Browser Details ID must be greater than 0",
        default=None,
    )


class DistributorCreate(DistributorBase):
    pass


class DistributorUpdate(DistributorBase):
    pass


class DistributorRead(DistributorBase):
    id: int

    model_config = {
        "from_attributes": True,
    }
