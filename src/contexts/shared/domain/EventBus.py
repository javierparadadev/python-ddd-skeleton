from abc import abstractmethod

from src.contexts.shared.domain.DomainEvent import DomainEvent
from src.contexts.shared.domain.EventSubscriber import EventSubscriber
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
