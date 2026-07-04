from ... import customtkinter
from .balance import balance


class actions:

    def __init__(self, parent_frame: customtkinter.CTkFrame, username: str) -> None:

        self.balance = balance(parent_frame, username)

        self.frame__actions: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame, width=350, height=40, fg_color="#0a0a0a"
        )
        self.frame__actions.place(x=740, y=200)

        self.frame__action_view: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame, width=350, height=390, fg_color="#0a0a0a"
        )
        self.frame__action_view.place(x=740, y=250)
