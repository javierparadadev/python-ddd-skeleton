from abc import abstractmethod

from src.contexts.shared.domain.Interface import Interface


class Logger(Interface):

    @abstractmethod
    def debug(self, log) -> None:
        raise NotImplementedError()

    @abstractmethod
    def info(self, log) -> None:
        raise NotImplementedError()

    @abstractmethod
    def warning(self, log) -> None:
        raise NotImplementedError()

    @abstractmethod
    def error(self, log) -> None:
        raise NotImplementedError()

    @abstractmethod
    def critical(self, log) -> None:
        raise NotImplementedError()
