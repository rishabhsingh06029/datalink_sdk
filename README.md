# DataLink SDK

A lightweight, unified database connector SDK for Python. Connect to MySQL, PostgreSQL, MongoDB, and Redis using a single consistent interface.

---

## Installation

```bash
pip install datalink-sdk
```

---

## Supported Databases

| Driver     | Key         |
|------------|-------------|
| MySQL      | `mysql`     |
| PostgreSQL | `postgres`  |
| MongoDB    | `mongodb`   |
| Redis      | `redis`     |

---

## Quick Start

```python
from datalink_sdk import DataLinkClient

# MySQL
conn = DataLinkClient.get_connection("mysql", {
    "host": "localhost",
    "user": "root",
    "password": "secret",
    "database": "mydb",
    "port": 3306,
})

# PostgreSQL
conn = DataLinkClient.get_connection("postgres", {
    "host": "localhost",
    "user": "postgres",
    "password": "secret",
    "database": "mydb",
    "port": 5432,
})

# MongoDB
conn = DataLinkClient.get_connection("mongodb", {
    "uri": "mongodb://localhost:27017",
})

# Redis
conn = DataLinkClient.get_connection("redis", {
    "host": "localhost",
    "port": 6379,
    "password": None,
})
```

---

## Exception Handling

```python
from datalink_sdk import DataLinkClient, DataLinkConnectionError, UnsupportedDriverError

try:
    conn = DataLinkClient.get_connection("mysql", config)
except DataLinkConnectionError as e:
    print(f"Connection failed: {e}")
except UnsupportedDriverError as e:
    print(f"Unknown driver: {e}")
```

---

## Exceptions Reference

| Exception                  | When raised                                      |
|----------------------------|--------------------------------------------------|
| `DataLinkException`        | Base exception for all DataLink SDK errors       |
| `DataLinkConnectionError`  | Connection to the database failed                |
| `UnsupportedDriverError`   | Driver type not recognised                       |
| `DataLinkConfigError`      | Configuration is invalid or missing fields       |

---

## Project Structure

```
datalink_sdk/
├── core/
│   ├── base_driver.py       # Abstract base class for all drivers
│   ├── client.py            # DataLinkClient — main entry point
│   └── exceptions.py        # All SDK exceptions
├── drivers/
│   ├── mysql.py
│   ├── postgres.py
│   ├── mongodb.py
│   └── redis.py
└── config/
    └── settings.py
```

---

## License

MIT
