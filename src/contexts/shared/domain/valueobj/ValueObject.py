from abc import ABC
from typing import Any


class ValueObject(ABC):

    def __init__(self, value: Any):
        self._value = value

    def value(self) -> Any:
        return self._value
