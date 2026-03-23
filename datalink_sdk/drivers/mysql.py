import mysql.connector
from ..core.base_driver import BaseDriver
from ..core.exceptions import DataLinkConnectionError


class MySQLDriver(BaseDriver):

    def connect(self):
        try:
            connection = mysql.connector.connect(
                host=self.config.get("host"),
                user=self.config.get("user"),
                password=self.config.get("password"),
                database=self.config.get("database"),
                port=self.config.get("port", 3306),
            )
            return connection

        except mysql.connector.Error as e:
            raise DataLinkConnectionError(f"MySQL connection failed: {e}")
