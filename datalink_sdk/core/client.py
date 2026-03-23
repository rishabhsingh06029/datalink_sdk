from datalink_sdk.drivers.mysql import MySQLDriver
from datalink_sdk.drivers.postgres import PostgresDriver
from datalink_sdk.drivers.mongodb import MongoDriver
from datalink_sdk.drivers.redis import RedisDriver
from .exceptions import UnsupportedDriverError


class DataLinkClient:
    """
    Central client for DataLink SDK.
    Resolves and returns a live database connection based on the driver type.
    """

    DRIVER_REGISTRY = {
        "mysql": MySQLDriver,
        "postgres": PostgresDriver,
        "mongodb": MongoDriver,
        "redis": RedisDriver,
    }

    @staticmethod
    def get_connection(driver_type: str, config: dict):
        """
        Returns a live connection for the specified driver type.

        :param driver_type: One of 'mysql', 'postgres', 'mongodb', 'redis'
        :param config: Dictionary containing connection parameters
        :return: Active database connection object
        """
        driver_type = driver_type.lower()

        if driver_type not in DataLinkClient.DRIVER_REGISTRY:
            raise UnsupportedDriverError(
                f"Unsupported driver type: '{driver_type}'. "
                f"Available drivers: {list(DataLinkClient.DRIVER_REGISTRY.keys())}"
            )

        driver_class = DataLinkClient.DRIVER_REGISTRY[driver_type]
        driver = driver_class(config)

        return driver.connect()
