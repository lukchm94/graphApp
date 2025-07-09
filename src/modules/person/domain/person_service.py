from logging import Logger

from ..infra import Neo4jPersonRepoImpl as PersonRepoImpl
from .person import Person


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

    def get_person_by_email(self, email: str) -> Person:
        """
        Retrieve a person by their email address using the repository.
        """
        self.logger.info(f"Retrieving person by email: {email}")
        return self.repo.get_by_email(email)
