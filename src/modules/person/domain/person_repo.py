from abc import ABC, abstractmethod
from .person import Person


class PersonRepository(ABC):
    @abstractmethod
    def save(self, person: Person) -> bool:
        """Save a person entity."""
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Person:
        """Retrieve a person by their email address."""
        pass
