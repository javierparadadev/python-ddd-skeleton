from abc import abstractmethod

from src.contexts.shared.domain.cqrs.Command import Command
from src.contexts.shared.domain.Interface import Interface


class CommandHandler(Interface):

    @abstractmethod
    def subscribed_to(self) -> str:
        raise NotImplementedError()

    @abstractmethod
    async def handle(self, command: Command) -> None:
        raise NotImplementedError()
