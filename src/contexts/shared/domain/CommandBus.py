from abc import abstractmethod
from typing import Any

from src.contexts.shared.domain.Command import Command
from src.contexts.shared.domain.Interface import Interface


class CommandBus(Interface):

    @abstractmethod
    async def dispatch(self, command: Command) -> Any:
        raise NotImplementedError()
