from minio import Minio

from src.contexts.shared.Infrastructure.persistence.minio.MinioConfiguration import MinioConfiguration
from src.contexts.shared.Infrastructure.persistence.mongo.PyMongoConfiguration import PyMongoConfiguration


class MinioClientFactory:

    _clients: dict[str, Minio] = {}

    @staticmethod
    def _get_client(context_name: str):
        return MinioClientFactory._clients.get(context_name)

    @staticmethod
    def _add_client(context_name: str, client: Minio):
        MinioClientFactory._clients[context_name] = client

    @staticmethod
    def create_instance(context_name: str, config: PyMongoConfiguration = None):
        client = MinioClientFactory._get_client(context_name)
        if client is not None:
            return client

        if config is None:
            config = MinioConfiguration()
        client = config.create_client_from_config()
        MinioClientFactory._add_client(context_name, client)
        return client
