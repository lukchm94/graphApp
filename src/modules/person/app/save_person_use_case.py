from ..domain import Person, PersonService
from logging import Logger


class SavePersonUseCase:
    def __init__(self, logger: Logger, person_service: PersonService) -> None:
        self.logger: Logger = logger
        self.person_service: PersonService = person_service

    def execute(self, person: Person):
        """
        Execute the use case to save a person entity.
        """
        self.logger.info(f"Executing SavePersonUseCase for: {person}")
        return self.person_service.save_person(person)
