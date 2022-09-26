from abc import abstractmethod


class DomainError(BaseException):

    @abstractmethod
    def to_primitives(self) -> dict | list:
        raise NotImplementedError()

    @abstractmethod
    def get_id(self) -> str:
        raise NotImplementedError()
