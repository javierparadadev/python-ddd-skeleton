from abc import abstractmethod, ABC

from src.contexts.shared.domain.DomainEvent import DomainEvent


class AggregateRoot(ABC):

    def __init__(self):
        self.__domain_events: list[DomainEvent] = []

    @abstractmethod
    def to_primitives(self) -> dict:
        raise NotImplementedError()

    def record_event(self, event: DomainEvent) -> None:
        self.__domain_events.append(event)
