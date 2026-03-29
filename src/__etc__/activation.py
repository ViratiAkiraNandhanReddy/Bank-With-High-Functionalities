from . import *


class activation:

    def __init__(self, _keys: list[str]) -> None:
        self._keys = _keys

        self.window = customtkinter.CTk()

        _width, _height = 532, 276
        _x_pos = int((self.window.winfo_screenwidth() / 2) - (_width / 2))
        _y_pos = int((self.window.winfo_screenheight() / 2) - (_height / 2))

        self.window.title("Bank With High Functionalities")
        self.window.geometry(f"{_width}x{_height}+{_x_pos}+{_y_pos}")

        apply_style(self.window, "transparent")
        title_bar.hide(self.window, no_span=True)

        self.window.minsize(_width, _height)
        self.window.maxsize(_width, _height)

        self.window.bind(
            "<Button-1>",
            lambda event: move_tk_with_no_titlebar_winos_native_ctypes(
                event, self.window
            ),
        )

        customtkinter.CTkLabel(
            self.window,
            text="BANK WITH HIGH FUNCTIONALITIES",
            font=("Segoe UI", 10),
            bg_color="black",
            height=0,
            width=0,
        ).place(x=5, y=5)

        self.window.mainloop()
