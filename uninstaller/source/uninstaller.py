import os
import ctypes
import shutil
import subprocess
import customtkinter
from PIL import Image
from hPyT import title_bar
from pywinstyles import apply_style

__dir_path: str = (
    str(os.environ.get("LOCALAPPDATA")) + r"\Bank-With-High-Functionalities"
)


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
            _event,
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


class uninstaller:

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

        self.window.bind(
            # Enables native Win32 window dragging for the borderless window by simulating a standard title bar drag operation.
            # This restores default Windows drag behavior, including smooth movement and proper DWM-managed window interactions
            # despite the absence of a native title bar.
            "<Button-1>",
            lambda _event: utils.borderless_window_utils.enable_native_window_drag_via_win32_message(
                _event, self.window
            ),
        )

        self.window.bind(
            # Fixes the hPyT title_bar.hide(no_span=True) side effect where Windows restores the window with stale non-client
            # frame metrics after minimization, causing unintended geometry expansion and an extra bottom gap. Reapplying the
            # modified window styles and forcing a native frame recalculation on the <Map> event ensures the borderless window
            # is restored with the correct dimensions and frame layout.
            "<Map>",
            lambda _event: utils.borderless_window_utils.disable_minimize_btn_and_force_window_frame_refresh(
                _event, self.window
            ),
        )

        self.window.mainloop()
