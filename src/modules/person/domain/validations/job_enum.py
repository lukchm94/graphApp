from enum import Enum


class JobEnum(Enum):
    """Enum for job types."""

    FULL_TIME = "full_time"
    PART_TIME = "part_time"
    CONTRACT = "contract"
    TEMPORARY = "temporary"
    INTERN = "intern"
    FREELANCE = "freelance"

    @classmethod
    def choices(cls):
        """Return a list of tuples for choices."""
        return [(job.value, job.name.replace("_", " ").title()) for job in cls]
