import pytest
from unittest.mock import patch, MagicMock
from datalink_sdk import DataLinkClient, UnsupportedDriverError, DataLinkConnectionError


def test_unsupported_driver():
    with pytest.raises(UnsupportedDriverError):
        DataLinkClient.get_connection("oracle", {"host": "localhost"})


def test_mysql_driver_called():
    with patch("datalink_sdk.drivers.mysql.mysql.connector.connect") as mock_connect:
        mock_connect.return_value = MagicMock()
        conn = DataLinkClient.get_connection("mysql", {
            "host": "localhost",
            "user": "root",
            "password": "secret",
            "database": "testdb",
        })
        assert conn is not None
        mock_connect.assert_called_once()


def test_postgres_driver_called():
    with patch("datalink_sdk.drivers.postgres.psycopg2.connect") as mock_connect:
        mock_connect.return_value = MagicMock()
        conn = DataLinkClient.get_connection("postgres", {
            "host": "localhost",
            "user": "postgres",
            "password": "secret",
            "database": "testdb",
        })
        assert conn is not None
        mock_connect.assert_called_once()


def test_mongodb_driver_called():
    with patch("datalink_sdk.drivers.mongodb.MongoClient") as mock_client:
        mock_client.return_value = MagicMock()
        conn = DataLinkClient.get_connection("mongodb", {
            "uri": "mongodb://localhost:27017",
        })
        assert conn is not None
        mock_client.assert_called_once()


def test_redis_driver_called():
    with patch("datalink_sdk.drivers.redis.redis.Redis") as mock_redis:
        mock_instance = MagicMock()
        mock_redis.return_value = mock_instance
        conn = DataLinkClient.get_connection("redis", {
            "host": "localhost",
            "port": 6379,
            "password": None,
        })
        assert conn is not None
        mock_instance.ping.assert_called_once()
