from typing import Optional

from pydantic import BaseModel, Field


class SongBase(BaseModel):
    title: Optional[str] = None
    duration: Optional[str] = None
    album_id: Optional[int] = Field(
        gt=0, description="Album ID must be greater than 0", default=None
    )


class SongCreate(SongBase):
    pass


class SongUpdate(SongBase):
    pass


class SongRead(SongBase):
    id: int

    model_config = {
        "from_attributes": True,
    }
