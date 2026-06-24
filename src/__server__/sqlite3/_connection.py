import sqlite3
from os import environ
from pathlib import Path

root: Path = Path(environ.get("LOCALAPPDATA", "")) / "Bank-With-High-Functionalities"

db_path = root / "database" / "sqlite3" / "database.sqlite3"

connection: sqlite3.Connection = sqlite3.connect(db_path)
