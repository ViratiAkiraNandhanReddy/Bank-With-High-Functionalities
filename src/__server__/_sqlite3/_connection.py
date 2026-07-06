import sqlite3
from ...utils import root

connection: sqlite3.Connection = sqlite3.connect(
    root / "database" / "sqlite3" / "database.sqlite3"
)

connection.execute("""
                   
    PRAGMA foreign_keys = ON
                   
    """)
