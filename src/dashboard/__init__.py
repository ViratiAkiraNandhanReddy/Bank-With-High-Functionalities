from .. import *


class dashboard_interface:

    def __init__(self) -> None:
        pass

    class dashboard:

        def __init__(
            self,
            parent_window: customtkinter.CTk,
            _btn: customtkinter.CTkButton,
            username: str,
        ) -> None:

            self.frame__dashboard: customtkinter.CTkFrame = customtkinter.CTkFrame(
                parent_window, width=1100, height=650, corner_radius=0, fg_color="black"
            )

            self.show_frame: Callable = lambda: (
                self.frame__dashboard.place(x=0, y=0),
                _btn.place_forget(),
            )
            self.hide_frame: Callable = lambda: (
                self.frame__dashboard.place_forget(),
                _btn.place(x=1080, y=0),
            )

    class transactions:

        def __init__(self) -> None:
            pass

    class settings:

        def __init__(self) -> None:
            pass
