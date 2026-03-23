import psycopg2
from ..core.base_driver import BaseDriver
from ..core.exceptions import DataLinkConnectionError


class PostgresDriver(BaseDriver):

    def connect(self):
        try:
            connection = psycopg2.connect(
                host=self.config.get("host"),
                user=self.config.get("user"),
                password=self.config.get("password"),
                dbname=self.config.get("database"),
                port=self.config.get("port", 5432),
            )
            return connection

        except psycopg2.Error as e:
            raise DataLinkConnectionError(f"PostgreSQL connection failed: {e}")
