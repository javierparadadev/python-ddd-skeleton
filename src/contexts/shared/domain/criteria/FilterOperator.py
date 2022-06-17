from enum import Enum

from src.contexts.shared.domain.errors.ValueObjectValidationError import ValueObjectValidationError


class FilterOperatorValues(Enum):
    EQUALS = '='


class FilterOperator:

    _allowed_values = [e.value for e in FilterOperatorValues]

    def __init__(self, value: str):
        if value not in self._allowed_values:
            raise ValueObjectValidationError(f'Filter Operator must be one of {self._allowed_values}'
                                             f' but {value} found.')
        self.value = value
