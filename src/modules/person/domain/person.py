from pydantic import BaseModel, Field, EmailStr, field_validator
from datetime import datetime
from .validations import JobEnum, ProfessionEnum


class Person(BaseModel):
    """
    Represents a person with a name and an age.
    """

    first_name: str = Field(..., description="The first name of the person")
    last_name: str = Field(..., description="The last name of the person")
    dob: str = Field(
        ..., description="The date of birth of the person in YYYY-MM-DD format"
    )
    email: EmailStr = Field(..., description="The email address of the person")
    job: JobEnum = Field(..., description="The job title of the person")
    profession: ProfessionEnum = Field(..., description="The profession of the person")

    @field_validator("dob")
    def validate_dob(cls, value: str) -> str:
        """
        Validates the date of birth to ensure it is in the correct format.
        """
        try:
            datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date of birth must be in YYYY-MM-DD format")
        return value
