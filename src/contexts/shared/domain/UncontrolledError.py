from src.contexts.shared.domain.DomainError import DomainError


class UncontrolledError(DomainError):

    ERROR_ID = 'a8e58b89-f379-4ac2-b773-125d3437761a'

    def __init__(self, message: str = None):
        if message is not None:
            message = 'Uncontrolled error.'
            self.message = message

    def to_primitives(self) -> dict | list:
        return {
            'message': self.message,
            'id': self.ERROR_ID,
        }

    def get_id(self) -> str:
        return self.ERROR_ID


