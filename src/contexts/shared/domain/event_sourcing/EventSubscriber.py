from abc import abstractmethod

from src.contexts.shared.domain.event_sourcing.DomainEvent import DomainEvent
from src.contexts.shared.domain.Interface import Interface


class EventSubscriber(Interface):

    @abstractmethod
    def subscribed_to(self) -> list[str]:
        raise NotImplementedError()

    @abstractmethod
    async def on(self, domain_event: DomainEvent) -> None:
        raise NotImplementedError()
