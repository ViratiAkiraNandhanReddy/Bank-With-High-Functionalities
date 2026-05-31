from os import environ
from pathlib import Path

from .theme import colors
from .browser import browser
from .privacy import masking
from .network import connection

root: Path = Path(environ.get("LOCALAPPDATA", "")) / "Bank-With-High-Functionalities"

__all__ = [
    "root",
    "colors",
    "browser",
    "masking",
    "connection",
]
