from abc import abstractmethod

from src.contexts.shared.domain.DomainEvent import DomainEvent
from src.contexts.shared.domain.Interface import Interface


class EventSubscriber(Interface):

    @abstractmethod
    def subscribed_to(self) -> list[str]:
        raise NotImplementedError()

    @abstractmethod
    async def on(self, domain_event: DomainEvent):
        raise NotImplementedError()
