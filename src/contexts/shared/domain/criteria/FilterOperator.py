from enum import Enum

from src.contexts.shared.domain.valueobj.ValueObjectValidationError import ValueObjectValidationError


class FilterOperatorValues(Enum):
    EQUALS = '='
    GREATER_THAN = '>'
    GREATER_THAN_OR_EQUALS = '>='
    LESS_THAN = '<'
    LESS_THAN_OR_EQUALS = '<='


class FilterOperator:

    _allowed_values = [e.value for e in FilterOperatorValues]

    def __init__(self, value: str):
        if value not in self._allowed_values:
            raise ValueObjectValidationError(f'Filter Operator must be one of {self._allowed_values}'
                                             f' but {value} found.')
        self.value = value
