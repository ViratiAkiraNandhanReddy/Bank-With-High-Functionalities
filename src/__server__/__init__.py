import os
import json
import logging

DIR_PATH: str = str(os.environ.get("LOCALAPPDATA")) + r"\Bank-With-High-Functionalities"

MYSQL__DB_PASSWORD: str | None = os.getenv("MYSQL__DB_PASSWORD")

try:

    with open(rf"{DIR_PATH}\database\config.json") as config:
        CONFIGURATION_JSON: dict = json.load(config)

except FileNotFoundError, json.JSONDecodeError:

    CONFIGURATION_JSON = {}

# ---  --- #

match CONFIGURATION_JSON.get("DATABASE TYPE"):

    case "JSON":
        from .JSON import SERVER
    case "MySQL":
        from .MySQL import SERVER
    case "SQLite3":
        from .SQLite3 import SERVER

__all__ = ["SERVER"]
