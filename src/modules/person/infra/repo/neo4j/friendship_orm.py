from datetime import datetime

from neomodel import DateProperty, StringProperty, StructuredRel  # type: ignore

from ....domain import FriendshipLevelEnum


class Friendship(StructuredRel):
    """
    Represents a friendship relationship between two persons in Neo4j.
    """

    created_at = DateProperty(default=datetime.now())
    updated_at = DateProperty(default=datetime.now())
    level = StringProperty(
        default=FriendshipLevelEnum.ACQUAINTANCE.value,
        choices=FriendshipLevelEnum.choices(),
        required=True,
    )

    def __str__(self):
        return f"Friendship(created_at={self.created_at}, updated_at={self.updated_at})"
