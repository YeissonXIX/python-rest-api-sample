from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv


class MotorClient:

    def __init__(self, db_name: str):
        load_dotenv()
        self.db_name = db_name
        
    def _set_connection_string(self):
        import os
        self.connection_string = os.getenv('MONGO_CONNECTION_STRING')

    def _set_client(self):
        self.client = AsyncIOMotorClient(self.connection_string, server_api=ServerApi('1'))

    def get_database(self):
        try:
            self._set_connection_string()
            self._set_client()
            return self.client[self.db_name]
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")
        

