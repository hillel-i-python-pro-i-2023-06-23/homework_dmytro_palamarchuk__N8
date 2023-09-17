"""DBConnection service"""

import sqlite3

from app.config import DB_DIR


class DBConnection:
    """DBConnection class"""

    def __init__(self):
        self._connection: sqlite3.Connection | None = None

    def __enter__(self):
        self._connection = sqlite3.connect(DB_DIR)
        self._connection.row_factory = sqlite3.Row
        return self._connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._connection.close()


def create_table():
    """Create a table phones"""
    with DBConnection() as connection:
        with connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS phones (
                    phone_id INTEGER NOT NULL PRIMARY KEY,
                    contact_name VARCHAR NOT NULL,
                    phone_value INTEGER NOT NULL
                )
            """
            )
