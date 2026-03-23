"""
DataLink SDK
============
A lightweight, unified database connector SDK for Python.
Supports MySQL, PostgreSQL, MongoDB, and Redis out of the box.

Usage:
    from datalink_sdk import DataLinkClient

    conn = DataLinkClient.get_connection("mysql", {
        "host": "localhost",
        "user": "root",
        "password": "secret",
        "database": "mydb",
    })
"""

from datalink_sdk.core.client import DataLinkClient
from datalink_sdk.core.exceptions import (
    DataLinkException,
    UnsupportedDriverError,
    DataLinkConnectionError,
    DataLinkConfigError,
)

__version__ = "1.0.0"
__author__ = "DataLink SDK Contributors"

__all__ = [
    "DataLinkClient",
    "DataLinkException",
    "UnsupportedDriverError",
    "DataLinkConnectionError",
    "DataLinkConfigError",
]
