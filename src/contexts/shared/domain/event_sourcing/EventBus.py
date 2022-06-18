from abc import abstractmethod

from src.contexts.shared.domain.event_sourcing.DomainEvent import DomainEvent
from src.contexts.shared.domain.event_sourcing.EventSubscriber import EventSubscriber
from src.contexts.shared.domain.Interface import Interface


class EventBus(Interface):

    @abstractmethod
    async def publish(self, events: list[DomainEvent]) -> None:
        raise NotImplementedError()

    @abstractmethod
    def add_subscribers(self, subscribers: list[EventSubscriber]) -> None:
        raise NotImplementedError()

    @abstractmethod
    def start(self) -> None:
        raise NotImplementedError()
