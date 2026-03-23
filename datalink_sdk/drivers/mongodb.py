from pymongo import MongoClient
from ..core.base_driver import BaseDriver
from ..core.exceptions import DataLinkConnectionError


class MongoDriver(BaseDriver):

    def connect(self):
        try:
            uri = self.config.get("uri")
            client = MongoClient(uri)
            return client

        except Exception as e:
            raise DataLinkConnectionError(f"MongoDB connection failed: {e}")
