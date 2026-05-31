from .views import *
from .. import customtkinter, assets


class navigation:

    def __init__(self, parent_frame: customtkinter.CTkFrame, username: str) -> None:

        self.frame__navigation: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame, width=200, height=630, fg_color="#0a0a0a"
        )
        self.frame__navigation.place(x=10, y=10)

        customtkinter.CTkLabel(
            self.frame__navigation,
            text="",
            image=customtkinter.CTkImage(
                light_image=assets.icons.material.manage_accounts,
                dark_image=assets.icons.material.manage_accounts,
                size=(64, 64),
            ),
            width=0,
            height=0,
        ).place(x=68, y=20)
