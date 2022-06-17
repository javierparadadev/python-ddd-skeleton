from enum import Enum

from src.contexts.shared.domain.errors.ValueObjectValidationError import ValueObjectValidationError


class OrderDirectionValues(Enum):
    ASC = 'asc'
    DESC = 'desc'


class OrderDirection:

    _allowed_values = [e.value for e in OrderDirectionValues]

    def __init__(self, order_dir: str):
        if order_dir not in self._allowed_values:
            raise ValueObjectValidationError(f'Order direction must be one of {self._allowed_values} '
                                             f'but {order_dir} found.')
        self.value = order_dir
