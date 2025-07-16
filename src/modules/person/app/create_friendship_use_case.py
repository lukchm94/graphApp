from logging import Logger

from ..domain import Friendship, Person, PersonService


class CreateFriendshipUseCase:
    def __init__(self, logger: Logger, service: PersonService) -> None:
        self.logger: Logger = logger
        self.person_service: PersonService = service

    def execute(self, friendship: Friendship) -> bool:
        """
        Create a friendship between two persons.

        :param person_email: Email of the person creating the friendship.
        :param friend_email: Email of the friend to be added.
        :param level: Level of the friendship.
        :raises ValueError: If the friendship level is invalid.
        """
        person: Person = self.person_service.get_person_by_email(friendship.email)
        friend: Person = self.person_service.get_person_by_email(
            friendship.friend_email
        )
        pass
