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

__dir_path: str = (
    str(os.environ.get("LOCALAPPDATA")) + r"\Bank-With-High-Functionalities"
)


class images:

    class icons:

        @staticmethod
        def get(icon_name: str, icon_type: str) -> Image.Image:

            return Image.open(rf"assets\icons\{icon_type}\{icon_name}.png")


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

        ## --- image assets --- ##

        self.icon__close: Image.Image = images.icons.get("close", "material-icons")
        self.icon__remove: Image.Image = images.icons.get("remove", "material-icons")

        self.frame__title_bar: customtkinter.CTkFrame = customtkinter.CTkFrame(
            self.window,
            width=650,
            height=20,
            fg_color="#0f0f0f",
            bg_color="black",
            corner_radius=0,
        )
        self.frame__title_bar.place(x=0, y=0)

        customtkinter.CTkButton(
            self.frame__title_bar,
            text="",
            width=0,
            height=0,
            fg_color="transparent",
            image=customtkinter.CTkImage(
                light_image=self.icon__close, dark_image=self.icon__close, size=(14, 14)
            ),
            corner_radius=0,
            border_spacing=0,
            hover_color="#ff0000",
        ).place(x=630, y=0)

        customtkinter.CTkButton(
            self.frame__title_bar,
            text="",
            width=0,
            height=0,
            fg_color="transparent",
            image=customtkinter.CTkImage(
                light_image=self.icon__remove,
                dark_image=self.icon__remove,
                size=(14, 14),
            ),
            corner_radius=0,
            border_spacing=0,
            hover_color="#202020",
        ).place(x=610, y=0)

        self.window.mainloop()
