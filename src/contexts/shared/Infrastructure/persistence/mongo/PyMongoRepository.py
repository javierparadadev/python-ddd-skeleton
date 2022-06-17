from abc import ABC, abstractmethod
from typing import Any, Tuple

from pymongo import MongoClient

from src.contexts.shared.Infrastructure.persistence.mongo.parse_criteria_to_mongo_query import \
    parse_criteria_to_mongo_query
from src.contexts.shared.domain.criteria.Criteria import Criteria


class PyMongoRepository(ABC):

    def __init__(self, client: MongoClient):
        self._client = client
        self._database = self._client.get_database(self.get_database_name())
        self._collection = self._database.get_collection(self.get_collection_name())

    @abstractmethod
    def get_database_name(self):
        raise NotImplementedError()

    @abstractmethod
    def get_collection_name(self):
        raise NotImplementedError()

    def _get_collection(self):
        return self._collection

    async def _find_one(self, raw_query: dict[str, Any]) -> Any:
        return self._collection.find_one(raw_query)

    async def _find_many(self, raw_query: dict[str, Any]) -> Any:
        cursor = self._collection.find(raw_query)
        data = list(cursor)
        return data

    async def _find_by_criteria(self, criteria: Criteria) -> Tuple[Any, Any]:
        raw_query, options = parse_criteria_to_mongo_query(criteria)
        data = list(self._collection.find(raw_query, **options))
        count = self._collection.find(raw_query, **options).count(with_limit_and_skip=True)
        return data, count

    async def _create_one(self, raw_obj: dict[str, Any]) -> Any:
        self._collection.insert_one(raw_obj)
