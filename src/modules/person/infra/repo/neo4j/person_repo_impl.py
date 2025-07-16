from logging import Logger
from typing import Union

from neomodel import DoesNotExist  # type: ignore

from ....domain.friendship import FriendshipLevelEnum
from ....domain.person import JobEnum, Person, ProfessionEnum
from ....domain.person_repo import PersonRepository
from .person_orm import Person as Neo4jPersonORM


class Neo4jPersonRepoImpl(PersonRepository):
    def __init__(self, logger: Logger) -> None:
        self.logger: Logger = logger
        self.logger.info(f"[{self.__class__.__name__}]Neo4jPersonRepoImpl initialized")

    def save(self, person: Person) -> bool:
        """
        Save a person entity to the Neo4j database.
        """
        # Implementation for saving a person to Neo4j
        person_orm = Neo4jPersonORM(
            first_name=person.first_name,
            last_name=person.last_name,
            dob=person.dob,
            email=person.email,
            job=person.job.value,
            profession=person.profession.value,
        )
        try:
            person_orm.save()  # type: ignore
            self.logger.info(f"Person {person.email} saved successfully.")
            return True
        except Exception as e:
            self.logger.warning(f"Error saving person: {e}")
            return False  # or handle the exception as needed

    def get_by_email(self, email: str) -> Union[Person, None]:
        """
        Retrieve a person by their email address from the Neo4j database.
        """
        try:
            person_orm: Neo4jPersonORM = Neo4jPersonORM.nodes.get(email=email)
            return Person(
                first_name=str(person_orm.first_name),
                last_name=str(person_orm.last_name),
                dob=str(person_orm.dob),
                email=str(person_orm.email),
                job=JobEnum(person_orm.job),
                profession=ProfessionEnum(person_orm.profession),
            )
        except DoesNotExist:
            self.logger.info(f"Person with email {email} does not exist.")
            return None

    def create_friendship(
        self, person: Neo4jPersonORM, friend: Neo4jPersonORM, level: FriendshipLevelEnum
    ) -> bool:
        """
        Create a friendship between two persons in the Neo4j database.
        """
        try:
            # Assuming Friendship is a relationship defined in your ORM
            person.friends.connect(friend, {"level": level})  # type: ignore
            self.logger.info(
                f"Friendship created between {person.email} and {friend.email}."
            )
            return True
        except DoesNotExist as e:
            self.logger.warning(f"Error creating friendship: {e}")
            return False
