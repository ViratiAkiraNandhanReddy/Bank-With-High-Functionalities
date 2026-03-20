import os
import json
import ctypes
import logging
from . import utils
import customtkinter
from . import __mail__
from typing import Any
from .loadAssets import *
from dotenv import load_dotenv
from .__server__ import SERVER, _uuids
from hPyT import title_bar, get_accent_color
from pywinstyles import apply_style, set_opacity

CONSTANTS: dict[str, dict[str, Any]] = {
    "WEBSITES": {
        "GITHUB_REPOSITORY": "https://github.com/ViratiAkiraNandhanReddy/Bank-With-High-Functionalities",
        "PROJECT_WEBSITE": "https://viratiakiranandhanreddy.github.io/Bank-With-High-Functionalities/",
    },
    "SOCIALS": {
        "GITHUB": "https://github.com/ViratiAkiraNandhanReddy",
        "INSTAGRAM": "https://www.instagram.com/viratiakiranandhanreddy",
        "TWITTER": "https://twitter.com/akiranandhan_",
        "LINKEDIN": "https://www.linkedin.com/in/viratiakiranandhanreddy",
        "YOUTUBE": "https://www.youtube.com/@ViratiAkiraNandhanReddy",
    },
}

DIR_PATH: str = str(os.environ.get("LOCALAPPDATA")) + r"\Bank-With-High-Functionalities"

try:

    with open(rf"{DIR_PATH}\database\config.json", "r") as config:
        CONFIGURATION_JSON: dict[str, Any] = json.load(config)

except FileNotFoundError, json.JSONDecodeError:

    CONFIGURATION_JSON = {}

load_dotenv(rf"{DIR_PATH}\.env")


def move_tk_with_no_titlebar_winos_native_ctypes(event, window: customtkinter.CTk):

    hwnd = ctypes.windll.user32.GetParent(window.winfo_id())
    ctypes.windll.user32.ReleaseCapture()
    ctypes.windll.user32.PostMessageW(hwnd, 0xA1, 2, 0)
