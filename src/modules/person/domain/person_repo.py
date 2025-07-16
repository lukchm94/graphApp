from abc import ABC, abstractmethod
from typing import Union

from ..infra import Neo4jPersonORM
from .person import Person
from .validations import FriendshipLevelEnum


class PersonRepository(ABC):
    @abstractmethod
    def save(self, person: Person) -> bool:
        """Save a person entity."""
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Union[Person, None]:
        """Retrieve a person by their email address."""
        pass

    @abstractmethod
    def create_friendship(
        self, person: Neo4jPersonORM, friend: Neo4jPersonORM, level: FriendshipLevelEnum
    ) -> bool:
        """Create a friendship between two persons."""
        pass
