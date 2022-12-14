from typing import Optional

from pydantic import BaseModel, Field

from app.user.enums.tree import (
    SongTypeEnum
)
from app.user.schemas.tree import TreeSchema


class SaveTreeRequest(TreeSchema):
    class Config:
        schema_extra = {
            "example": {
                "tree_type": "family",
                "brightness": "brightest",
                "has_santa": True,
                "weather": "snow",
                "song_type": "kpop",
            }
        }


class TreeSongRequest(BaseModel):
    song_type: SongTypeEnum = Field(
        description="어떤 노래를 듣고 싶으신가요 -> Enum string"
    )
