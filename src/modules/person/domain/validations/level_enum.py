from enum import Enum


class FriendshipLevelEnum(Enum):
    """
    Enum representing the friendship levels.
    """

    ACQUAINTANCE = "acquaintance"
    FRIEND = "friend"
    BEST_FRIEND = "best_friend"
    FAMILY = "family"

    @classmethod
    def choices(cls):
        """
        Returns a list of tuples containing the enum member names and their values.
        """
        return [(member.value, member.value.capitalize()) for member in cls]
