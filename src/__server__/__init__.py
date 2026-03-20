import os
import json
import uuid
import logging

DIR_PATH: str = str(os.environ.get("LOCALAPPDATA")) + r"\Bank-With-High-Functionalities"

MYSQL__DB_PASSWORD: str | None = os.getenv("MYSQL__DB_PASSWORD")


class _uuids:

    UUID_NAMESPACE_BWHF = uuid.UUID(
        "71da99dc-ce4e-575e-a319-3083e9265046"
    )  # pre-generated using uuid.uuid5(uuid.NAMESPACE_URL, "https://viratiakiranandhanreddy.github.io/Bank-With-High-Functionalities/")

    @classmethod
    def generate_uuid5(cls, name: str) -> str:
        return str(uuid.uuid5(cls.UUID_NAMESPACE_BWHF, name))

    @classmethod
    def validate_uuid5(cls, uuid_to_validate: str) -> bool:
        try:
            uuid_obj = uuid.UUID(uuid_to_validate, version=5)
            return True
        except ValueError:
            return False


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
