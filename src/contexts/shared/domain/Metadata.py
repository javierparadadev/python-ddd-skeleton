from abc import ABC, abstractmethod


class Metadata(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def to_primitives(self) -> dict:
        raise NotImplementedError()
