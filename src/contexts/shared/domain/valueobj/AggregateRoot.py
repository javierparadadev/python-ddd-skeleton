from abc import abstractmethod, ABC

from src.contexts.shared.domain.event_sourcing.DomainEvent import DomainEvent


class AggregateRoot(ABC):

    def __init__(self):
        self._domain_events: list[DomainEvent] = []

    @abstractmethod
    def to_primitives(self) -> dict:
        raise NotImplementedError()

    def record_event(self, event: DomainEvent) -> None:
        self._domain_events.append(event)
