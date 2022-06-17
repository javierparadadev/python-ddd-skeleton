from abc import abstractmethod
from typing import Any

from src.contexts.shared.domain.Interface import Interface


class Logger(Interface):

    @abstractmethod
    def debug(self, log: Any) -> None:
        raise NotImplementedError()

    @abstractmethod
    def info(self, log: Any) -> None:
        raise NotImplementedError()

    @abstractmethod
    def error(self, log: Any) -> None:
        raise NotImplementedError()

    @abstractmethod
    def critical(self, log: Any) -> None:
        raise NotImplementedError()
