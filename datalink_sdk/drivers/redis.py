import redis
from ..core.base_driver import BaseDriver
from ..core.exceptions import DataLinkConnectionError


class RedisDriver(BaseDriver):

    def connect(self):
        try:
            connection = redis.Redis(
                host=self.config.get("host"),
                port=self.config.get("port", 6379),
                password=self.config.get("password"),
                decode_responses=True,
            )
            connection.ping()  # Verify connection is alive
            return connection

        except redis.RedisError as e:
            raise DataLinkConnectionError(f"Redis connection failed: {e}")
