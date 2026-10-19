lazy import ctypes
lazy import json
lazy import os
lazy import threading
lazy from typing import Any, Callable

lazy import customtkinter
lazy from dotenv import load_dotenv
lazy from hPyT import get_accent_color, title_bar
lazy from pywinstyles import apply_style, set_opacity

lazy from . import assets, utils
lazy from .__mail__ import (
    email_verification,
    forgot_password,
    two_factor_authentication,
    welcome,
)
lazy from .__server__ import SERVER

CONSTANTS: dict[str, dict[str, Any]] = {
    "website": {
        "home": "https://viratiakiranandhanreddy.github.io/Bank-With-High-Functionalities/",
    },
    "github": {
        "repository": "https://github.com/ViratiAkiraNandhanReddy/Bank-With-High-Functionalities",
        "issues": "https://github.com/ViratiAkiraNandhanReddy/Bank-With-High-Functionalities/issues",
        "discussions": "https://github.com/ViratiAkiraNandhanReddy/Bank-With-High-Functionalities/discussions",
    },
}

try:

    with open(utils.root / "database" / "config.json", "r") as config:
        CONFIGURATION_JSON: dict[str, Any] = json.load(config)

except FileNotFoundError, json.JSONDecodeError:

    CONFIGURATION_JSON = {}

load_dotenv(utils.root / ".env")


class borderless_window_utils:

    @staticmethod
    def enable_native_window_drag_via_win32_message(_event, window: customtkinter.CTk):

        hwnd: int = ctypes.windll.user32.GetParent(window.winfo_id())
        ctypes.windll.user32.ReleaseCapture()
        ctypes.windll.user32.PostMessageW(hwnd, 0xA1, 2, 0)

    @staticmethod
    def disable_minimize_btn_and_force_window_frame_refresh(
        _event, window: customtkinter.CTk
    ):

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
