from abc import abstractmethod
from typing import Any, NoReturn

from src.contexts.shared.domain.Interface import Interface


class Logger(Interface):

    @abstractmethod
    def debug(self, log: Any) -> NoReturn:
        raise NotImplementedError()

    @abstractmethod
    def info(self, log: Any) -> NoReturn:
        raise NotImplementedError()

    @abstractmethod
    def error(self, log: Any) -> NoReturn:
        raise NotImplementedError()

    @abstractmethod
    def critical(self, log: Any) -> NoReturn:
        raise NotImplementedError()
