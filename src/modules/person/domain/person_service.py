from logging import Logger
from typing import Union

from ..infra import Neo4jPersonRepoImpl as PersonRepoImpl
from .person import Person
from .validations import FriendshipLevelEnum


class PersonService:
    def __init__(self, logger: Logger, repo: PersonRepoImpl) -> None:
        self.logger: Logger = logger
        self.repo: PersonRepoImpl = repo

    def save_person(self, person: Person) -> bool:
        """
        Save a person entity using the repository.
        """
        self.logger.info(f"Saving person: {person}")
        return self.repo.save(person)

    def get_person_by_email(self, email: str) -> Union[Person, None]:
        """
        Retrieve a person by their email address using the repository.
        """
        self.logger.info(f"Retrieving person by email: {email}")
        return self.repo.get_by_email(email)

    def create_friendship(
        self, person_email: str, friend_email: str, level: FriendshipLevelEnum
    ) -> bool:
        """
        Create a friendship between two persons using the repository.
        :param person_email: Email of the person creating the friendship.
        :param friend_email: Email of the friend to be added.
        :param level: Level of the friendship.
        :raises ValueError: If the friendship level is invalid.
        """
        self.logger.info(
            f"Creating friendship from {person_email} to {friend_email} with level {level}"
        )
        return self.repo.create_friendship(person_email, friend_email, level)
