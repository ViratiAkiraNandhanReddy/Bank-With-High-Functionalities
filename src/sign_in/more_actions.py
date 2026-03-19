from ..sign_in import *
from ..administrator import administrator_interface


class more_actions_interface:

    def __init__(self) -> None:
        pass

    class more_actions:

        def __init__(
            self, parent_window: customtkinter.CTk, _btn: customtkinter.CTkButton
        ) -> None:

            self.frame__more_actions = customtkinter.CTkFrame(
                parent_window, corner_radius=0
            )
            self.frame__more_actions.configure(width=1060, height=610)

            self.show_frame = lambda: (
                self.frame__more_actions.place(x=20, y=20),
                _btn.configure(state="disabled"),
            )
            self.hide_frame = lambda: (
                self.frame__more_actions.place_forget(),
                _btn.configure(state="normal"),
            )
