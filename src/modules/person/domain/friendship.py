from datetime import datetime

from pydantic import BaseModel, EmailStr, Field

from .validations import FriendshipLevelEnum


class Friendship(BaseModel):
    email: EmailStr = Field(..., description="Email of the person")
    friend_email: EmailStr = Field(..., description="Email of the friend")
    level: FriendshipLevelEnum = Field(..., description="Friendship level")
    since: datetime = Field(
        default_factory=datetime.now, description="Date when the friendship started"
    )
