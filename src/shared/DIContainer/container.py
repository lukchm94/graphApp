from logging import Logger, getLogger
from typing import Any, Dict, TypeVar

from src.modules.person import Neo4jPersonRepoImpl as PersonRepoImpl
from src.modules.person import PersonService, SavePersonUseCase

T = TypeVar("T")


class DIContainer:
    """
    Dependency Injection Container
    """

    def __init__(self):
        self._services: Dict[str, Any] = {}
        self._logger: Logger = getLogger(__name__)
        self.register("logger", self._logger)
        self.register("person_repo", PersonRepoImpl(self._logger))
        self.register(
            "person_service", PersonService(self._logger, self.get("person_repo"))
        )
        self.register(
            "save_person_use_case",
            SavePersonUseCase(self._logger, self.get("person_service")),
        )

    def register(self, name: str, service: Any) -> None:
        """
        Register a service in the container
        """
        self._services[name] = service

    def get(self, name: str) -> Any:
        """
        Get a service from the container
        """
        return self._services.get(name)


container: DIContainer = DIContainer()
