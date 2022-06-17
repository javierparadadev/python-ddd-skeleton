from pymongo import MongoClient

from src.contexts.shared.Infrastructure.persistence.mongo.PyMongoConfiguration import PyMongoConfiguration


class PyMongoClientFactory:

    _clients: dict[str, MongoClient] = {}

    @staticmethod
    def _get_client(context_name: str):
        return PyMongoClientFactory._clients.get(context_name)

    @staticmethod
    def _add_client(context_name: str, client: MongoClient):
        PyMongoClientFactory._clients[context_name] = client

    @staticmethod
    def create_instance(context_name: str, config: PyMongoConfiguration = None):
        client = PyMongoClientFactory._get_client(context_name)
        if client is not None:
            return client

        if config is None:
            config = PyMongoConfiguration()
        client = config.create_client_from_config()
        PyMongoClientFactory._add_client(context_name, client)
        return client
