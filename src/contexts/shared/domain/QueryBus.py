from abc import abstractmethod

from src.contexts.shared.domain.Interface import Interface
from src.contexts.shared.domain.Query import Query
from src.contexts.shared.domain.Response import Response


class QueryBus(Interface):

    @abstractmethod
    async def ask(self, query: Query) -> Response:
        raise NotImplementedError()
