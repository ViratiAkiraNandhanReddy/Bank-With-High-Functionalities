lazy import json
lazy from pathlib import Path

lazy from .browser import browser
lazy from .greetings import greetings
lazy from .network import connection
lazy from .privacy import masking
lazy from .theme import colors

root: Path = Path(__file__).resolve().parent.parent.parent


def save_configuration_json(configuration: dict) -> bool:

    try:
        config_path = root / "database" / "config.json"
        temporary_path = config_path.with_suffix(".json.tmp")
        with temporary_path.open("w", encoding="utf-8") as config:
            json.dump(configuration, config, indent=4)
            config.write("\n")
        temporary_path.replace(config_path)
        return True
    except OSError, TypeError, ValueError:
        return False


__all__ = [
    "root",
    "colors",
    "browser",
    "masking",
    "greetings",
    "connection",
    "save_configuration_json",
]
