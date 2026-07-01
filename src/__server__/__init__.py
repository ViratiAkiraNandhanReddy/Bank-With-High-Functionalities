import json
import logging
from ..utils import root
from ._json import SERVER as JSONServer
from ._mysql import SERVER as MySQLServer
from ._sqlite3 import SERVER as SQLite3Server

try:

    with open(root / "database" / "config.json") as config:
        CONFIGURATION_JSON: dict = json.load(config)

except FileNotFoundError, json.JSONDecodeError:

    CONFIGURATION_JSON = {}

# ---  --- #

match CONFIGURATION_JSON.get("DATABASE TYPE"):

    case "JSON":
        SERVER = JSONServer
    case "MySQL":
        SERVER = MySQLServer
    case "SQLite3":
        SERVER = SQLite3Server

__all__ = ["SERVER"]
