import os
import ctypes
import socket
import shutil
import zipfile
import requests
import subprocess
import customtkinter
from PIL import Image
from hPyT import title_bar
from pywinstyles import apply_style


class images:

    pass


class utils:

    class borderless_window_utils:

        @staticmethod
        def enable_native_window_drag_via_win32_message(
            _event, window: customtkinter.CTk
        ):

            hwnd: int = ctypes.windll.user32.GetParent(window.winfo_id())
            ctypes.windll.user32.ReleaseCapture()
            ctypes.windll.user32.PostMessageW(hwnd, 0xA1, 2, 0)

        @staticmethod
        def disable_minimize_btn_and_force_window_frame_refresh(
            window: customtkinter.CTk,
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


class installer:

    def __init__(self) -> None:

        self.window: customtkinter.CTk = customtkinter.CTk()

        _width, _height = 650, 400
        _x_pos: int = int((self.window.winfo_screenwidth() / 2) - (_width / 2))
        _y_pos: int = int((self.window.winfo_screenheight() / 2) - (_height / 2))

        self.window.title("Bank With High Functionalities")
        self.window.geometry(f"{_width}x{_height}+{_x_pos}+{_y_pos}")
        # self.window.iconbitmap("favicon.ico")

        apply_style(self.window, "transparent")
        title_bar.hide(self.window, no_span=True)

        self.window.minsize(_width, _height)
        self.window.maxsize(_width, _height)
        utils.borderless_window_utils.disable_minimize_btn_and_force_window_frame_refresh(
            self.window
        )

        self.window.bind(  # Allowing the user to move the window by dragging anywhere on it, since there is no title bar.
            "<Button-1>",
            lambda _event: utils.borderless_window_utils.enable_native_window_drag_via_win32_message(
                _event, self.window
            ),
        )

        self.window.mainloop()
