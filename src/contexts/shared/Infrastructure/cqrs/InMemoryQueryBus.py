from typing import Any

from src.contexts.shared.domain.BaseObject import BaseObject
from src.contexts.shared.domain.cqrs.query.Query import Query
from src.contexts.shared.domain.cqrs.query.QueryBus import QueryBus
from src.contexts.shared.domain.cqrs.query.QueryHandler import QueryHandler
from src.contexts.shared.domain.cqrs.query.QueryNoRegisteredError import QueryNotRegisteredError


class InMemoryQueryBus(BaseObject, QueryBus):

    def __init__(self, *handlers: QueryHandler):
        handler_mapping = {}
        for handler in handlers:
            handler_mapping[handler.subscribed_to()] = handler
        self._handler_mapping: dict[str, QueryHandler] = handler_mapping

    def _search(self, query_name: str):
        if query_name not in self._handler_mapping:
            raise QueryNotRegisteredError()
        return self._handler_mapping[query_name]

    async def ask(self, query: Query) -> Any:
        query_type: str = query.get_query_type_name()
        handler = self._search(query_type)
        return await handler.handle(query)
