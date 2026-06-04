from .. import customtkinter, Callable


class users_and_access:

    def __init__(self, parent_frame: customtkinter.CTkFrame, username: str) -> None:

        self.frame__users_and_access: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame, width=870, height=590, fg_color="#0a0a0a"
        )

        self.show_frame: Callable = lambda: self.frame__users_and_access.place(
            x=220, y=50
        )
        self.hide_frame: Callable = lambda: self.frame__users_and_access.place_forget()
