from src.contexts.shared.domain.Metadata import Metadata


class CriteriaQueryMetadata(Metadata):

    def __init__(self, count: int = None):
        super().__init__()
        self.count = count

    def to_primitives(self) -> dict:
        return {
            'count': self.count
        }
