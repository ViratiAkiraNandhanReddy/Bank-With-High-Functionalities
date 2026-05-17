import os
import json
import ctypes
import logging
from . import utils
import customtkinter
from . import __mail__
from ._assets import *
from dotenv import load_dotenv
from typing import Any, Callable
from .__server__ import SERVER, _uuids
from hPyT import title_bar, get_accent_color
from pywinstyles import apply_style, set_opacity

CONSTANTS: dict[str, dict[str, Any]] = {
    "website": {
        "home": "https://viratiakiranandhanreddy.github.io/Bank-With-High-Functionalities/",
    },
    "socials": {
        "github": "https://github.com/ViratiAkiraNandhanReddy",
        "instagram": "https://www.instagram.com/viratiakiranandhanreddy",
        "twitter": "https://twitter.com/akiranandhan_",
        "linkedin": "https://www.linkedin.com/in/viratiakiranandhanreddy",
        "youtube": "https://www.youtube.com/@ViratiAkiraNandhanReddy",
    },
    "github": {
        "repository": "https://github.com/ViratiAkiraNandhanReddy/Bank-With-High-Functionalities",
        "issues": "https://github.com/ViratiAkiraNandhanReddy/Bank-With-High-Functionalities/issues",
        "discussions": "https://github.com/ViratiAkiraNandhanReddy/Bank-With-High-Functionalities/discussions",
    },
}

DIR_PATH: str = str(os.environ.get("LOCALAPPDATA")) + r"\Bank-With-High-Functionalities"

try:

    with open(rf"{DIR_PATH}\database\config.json", "r") as config:
        CONFIGURATION_JSON: dict[str, Any] = json.load(config)

except FileNotFoundError, json.JSONDecodeError:

    CONFIGURATION_JSON = {}

load_dotenv(rf"{DIR_PATH}\.env")


class borderless_window_utils:

    @staticmethod
    def enable_native_window_drag_via_win32_message(_event, window: customtkinter.CTk):

        hwnd = ctypes.windll.user32.GetParent(window.winfo_id())
        ctypes.windll.user32.ReleaseCapture()
        ctypes.windll.user32.PostMessageW(hwnd, 0xA1, 2, 0)

    @staticmethod
    def disable_minimize_btn_and_force_window_frame_refresh(window: customtkinter.CTk):

        hwnd: int = ctypes.windll.user32.GetParent(window.winfo_id())
        style = ctypes.windll.user32.GetWindowLongW(hwnd, -16)

        style &= ~0x00020000

        ctypes.windll.user32.SetWindowLongW(hwnd, -16, style)
        ctypes.windll.user32.SetWindowPos(
            hwnd,
            None,
            0,
            0,
            0,
            0,
            0x0002 | 0x0001 | 0x0020,  # SWP_NOMOVE | SWP_NOSIZE | SWP_FRAMECHANGED
        )
