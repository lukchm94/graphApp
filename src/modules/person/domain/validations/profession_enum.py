from enum import Enum


class ProfessionEnum(Enum):
    """Enum for profession types."""

    DOCTOR = "doctor"
    ENGINEER = "engineer"
    TEACHER = "teacher"
    NURSE = "nurse"
    LAWYER = "lawyer"
    ARTIST = "artist"

    @classmethod
    def choices(cls):
        """Return a list of tuples for choices."""
        return [
            (profession.value, profession.name.replace("_", " ").title())
            for profession in cls
        ]
