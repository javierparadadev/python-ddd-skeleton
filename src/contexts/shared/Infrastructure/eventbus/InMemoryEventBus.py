from src.contexts.shared.domain.BaseObject import BaseObject
from src.contexts.shared.domain.event_sourcing.DomainEvent import DomainEvent
from src.contexts.shared.domain.event_sourcing.EventBus import EventBus
from src.contexts.shared.domain.event_sourcing.EventSubscriber import EventSubscriber


class InMemoryEventBus(BaseObject, EventBus):

    def __init__(self, *subscribers: EventSubscriber):
        event_subscriber_mapping: dict[str, list[EventSubscriber]] = {}
        for subscriber in subscribers:
            for event in subscriber.subscribed_to():
                if event not in event_subscriber_mapping:
                    event_subscriber_mapping[event] = []
                event_subscriber_mapping[event].append(subscriber)
        self._subscriptions = event_subscriber_mapping

    def start(self):
        pass

    async def publish(self, events: list[DomainEvent]) -> None:
        for event in events:
            event_type = event.get_event_type_name()
            if event_type not in self._subscriptions:
                continue
            subscribers = self._subscriptions[event_type]
            for subscriber in subscribers:
                try:
                    await subscriber.on(event)  # TODO: add gather or future
                except Exception as e:
                    pass  # TODO: print error

    def add_subscribers(self, subscribers: list[EventSubscriber]) -> None:
        for subscriber in subscribers:
            self.add_subscriber(subscriber)

    def add_subscriber(self, subscriber: EventSubscriber) -> None:
        event_types = subscriber.subscribed_to()
        for event_type in event_types:
            if event_type not in self._subscriptions:
                self._subscriptions[event_type] = []
            self._subscriptions[event_type].append(subscriber)
