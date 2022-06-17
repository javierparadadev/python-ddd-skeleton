from abc import abstractmethod
from typing import NoReturn

from src.contexts.shared.domain.Command import Command
from src.contexts.shared.domain.Interface import Interface


class CommandBus(Interface):

    @abstractmethod
    async def dispatch(self, command: Command) -> NoReturn:
        raise NotImplementedError()
