from . import *


class activation:

    def __init__(self, _keys: list[str]) -> None:
        self._keys = _keys

        self.window = customtkinter.CTk()
        self.window.title("Bank With High Functionalities")
        self.window.geometry("800x400")

        apply_style(self.window, "transparent")
        title_bar.hide(self.window)

        self.window.minsize(800, 400)
        self.window.maxsize(800, 400)

        self.window.bind(
            "<Button-1>",
            lambda event: move_tk_with_no_titlebar_winos_native_ctypes(
                event, self.window
            ),
        )

        self.window.mainloop()
