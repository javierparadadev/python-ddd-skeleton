from enum import Enum

from src.contexts.shared.domain.errors.ValueObjectValidationError import ValueObjectValidationError


class FilterOperatorValues(Enum):
    EQUALS = '='


class FilterOperator:

    __allowed_values = [e.value for e in FilterOperatorValues]

    def __init__(self, value: str):
        if value not in self.__allowed_values:
            raise ValueObjectValidationError(f'Filter Operator must be one of {self.__allowed_values}'
                                             f' but {value} found.')
        self.value = value
