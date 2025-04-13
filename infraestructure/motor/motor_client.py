from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from typing import Any
from shared.types import Document


class MotorClient:

    db_name: str
    connection_string: str | None
    client: AsyncIOMotorClient[Document]

    def __init__(self, db_name: str):
        _ = load_dotenv()
        self.db_name = db_name
        self._set_connection_string()
        self._set_client()

    def _set_connection_string(self):
        import os

        self.connection_string = os.getenv("MONGO_CONNECTION_STRING")

    def _set_client(self):
        server_api = ServerApi("1")
        self.client = AsyncIOMotorClient(self.connection_string, server_api=server_api)

    def get_database(self) -> AsyncIOMotorDatabase[dict[str, Any]]:
        return self.client[self.db_name]
