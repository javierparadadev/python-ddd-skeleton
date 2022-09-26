from abc import abstractmethod, ABC


class AggregateRoot(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def to_primitives(self) -> dict:
        raise NotImplementedError()
