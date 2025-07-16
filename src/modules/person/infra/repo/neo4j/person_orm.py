from neomodel import RelationshipTo  # type: ignore
from neomodel import StringProperty  # type: ignore
from neomodel import EmailProperty, StructuredNode, UniqueIdProperty  # type: ignore

from ....domain.validations import JobEnum, ProfessionEnum
from .friendship_orm import Friendship


class Person(StructuredNode):
    """
    Represents a person in the Neo4j database.
    """

    __primarykey__ = "email"

    uid = UniqueIdProperty()
    first_name = StringProperty(required=True)
    last_name = StringProperty(required=True)
    dob = StringProperty(required=True)  # Date of birth in YYYY-MM-DD format
    email = EmailProperty(unique_index=True, required=True)
    job = StringProperty(
        required=True, choices=[(job.value, job.value.capitalize()) for job in JobEnum]
    )
    profession = StringProperty(
        required=True,
        choices=[
            (profession.value, profession.value.capitalize())
            for profession in ProfessionEnum
        ],
    )
    friends = RelationshipTo("self", "FRIEND", model=Friendship)

    def __str__(self):
        return f"Person(first_name={self.first_name}, last_name={self.last_name}, email={self.email})"

    def __repr__(self):
        return f"Person(first_name={self.first_name}, last_name={self.last_name}, email={self.email})"
