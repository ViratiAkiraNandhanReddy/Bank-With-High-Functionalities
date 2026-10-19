lazy from pathlib import Path

lazy from .browser import browser
lazy from .greetings import greetings
lazy from .network import connection
lazy from .privacy import masking
lazy from .theme import colors

root: Path = Path(__file__).resolve().parent.parent.parent

__all__ = [
    "root",
    "colors",
    "browser",
    "masking",
    "greetings",
    "connection",
]
