import uuid
from abc import ABC, abstractmethod
from datetime import datetime


class DomainEvent(ABC):

    def __init__(
            self,
            event_id: str,
            aggregate_id: str,
            occurred_on: datetime = None):
        self.name = self.get_event_type_name()
        self.aggregate_id = aggregate_id
        if self.aggregate_id is None:
            self.aggregate_id = uuid.uuid4()
        self.id = event_id
        self.occurred_on = occurred_on
        self.created_at = datetime.now()
        if self.occurred_on is None:
            self.occurred_on = self.created_at

    def get_event_type_name(self) -> str:
        return self.name

    @abstractmethod
    def to_primitives(self) -> dict:
        event = {
            'data': {
                'id': self.id,
                'type': self.name,
                'attributes': {
                    'id': self.aggregate_id,
                },
                'occurred_on': self.occurred_on.isoformat(),
                'created_at': self.created_at.isoformat(),
            },
            'meta': {}
        }
        return event
