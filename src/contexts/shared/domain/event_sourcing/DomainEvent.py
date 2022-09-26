import uuid
from abc import ABC, abstractmethod
from datetime import datetime


class DomainEvent(ABC):

    def __init__(
            self,
            event_id: str,
            occurred_on: datetime = None):
        self.name = self.get_event_type_name()
        self.event_id = event_id
        if self.event_id is None:
            self.event_id = uuid.uuid4()
        self.id = event_id
        self.occurred_on = occurred_on
        self.created_at = datetime.now()
        if self.occurred_on is None:
            self.occurred_on = self.created_at

    @abstractmethod
    def get_event_type_name(self) -> str:
        raise NotImplementedError()

    def to_primitives(self) -> dict:
        event = {
            'data': {
                'id': self.id,
                'type': self.name,
                'occurred_on': self.occurred_on.isoformat(),
                'created_at': self.created_at.isoformat(),
            },
            'meta': {}
        }
        return event
