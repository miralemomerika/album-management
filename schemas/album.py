import datetime
from typing import Optional

from pydantic import BaseModel, Field


class AlbumBase(BaseModel):
    name: Optional[str] = None
    band_name: Optional[str] = None
    band_members: Optional[str] = None
    album_details_url: Optional[str] = None
    music_type: Optional[str] = None
    creation_date: Optional[datetime.date] = None
    upload_date: Optional[datetime.date] = None
    approval_date: Optional[datetime.date] = None
    status: Optional[str] = None
    distributor_id: Optional[int] = Field(
        gt=0, description="Distributor ID must be greater than 0", default=None
    )
    music_services_id: Optional[int] = Field(
        gt=0,
        description="Music Services ID must be greater than 0",
        default=None,
    )


class AlbumCreate(AlbumBase):
    pass


class AlbumUpdate(AlbumBase):
    pass


class AlbumRead(AlbumBase):
    id: int

    model_config = {
        "from_attributes": True,
    }
