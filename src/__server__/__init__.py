import json
import logging
from ..utils import root

try:

    with open(root / "database" / "config.json") as config:
        CONFIGURATION_JSON: dict = json.load(config)

except FileNotFoundError, json.JSONDecodeError:

    CONFIGURATION_JSON = {}

# ---  --- #

match CONFIGURATION_JSON.get("DATABASE TYPE"):

    case "JSON":

        from ._json import SERVER as JSONServer

        SERVER = JSONServer

    case "MySQL":

        from ._mysql import SERVER as MySQLServer

        SERVER = MySQLServer

    case "SQLite3":

        from ._sqlite3 import SERVER as SQLite3Server

        SERVER = SQLite3Server

__all__ = ["SERVER"]
