from .views import *
from ._navigation__transaction_carousel import transaction_carousel
from .. import customtkinter, assets


class navigation:

    def __init__(self, parent_frame: customtkinter.CTkFrame, username: str) -> None:

        self.frame__navigation: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame, width=200, height=630, fg_color="#0a0a0a"
        )
        self.frame__navigation.place(x=10, y=10)

        self.current_frame: customtkinter.CTkFrame

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

        self.overview: overview = overview(parent_frame, username)
        self.settings: settings = settings(parent_frame, username)

        self._overview_button: customtkinter.CTkButton = customtkinter.CTkButton(
            self.frame__navigation,
            text="Overview",
            width=190,
            height=44,
            fg_color="#0a0a0a",
            hover_color="#1a1a1a",
            font=("Segoe UI", 14),
            image=customtkinter.CTkImage(
                light_image=assets.icons.material.overview,
                dark_image=assets.icons.material.overview,
                size=(20, 20),
            ),
            compound="left",
            border_spacing=10,
            anchor="w",
        )
        self._overview_button.place(x=5, y=270)

        self._2_button: customtkinter.CTkButton = customtkinter.CTkButton(
            self.frame__navigation,
            text="Button 2",
            width=190,
            height=44,
            fg_color="#0a0a0a",
            hover_color="#1a1a1a",
            font=("Segoe UI", 14),
            image=customtkinter.CTkImage(
                light_image=assets.icons.material.overview,
                dark_image=assets.icons.material.overview,
                size=(20, 20),
            ),
            compound="left",
            border_spacing=10,
            anchor="w",
        )
        self._2_button.place(x=5, y=319)

        self._3_button: customtkinter.CTkButton = customtkinter.CTkButton(
            self.frame__navigation,
            text="Button 3",
            width=190,
            height=44,
            fg_color="#0a0a0a",
            hover_color="#1a1a1a",
            font=("Segoe UI", 14),
            image=customtkinter.CTkImage(
                light_image=assets.icons.material.overview,
                dark_image=assets.icons.material.overview,
                size=(20, 20),
            ),
            compound="left",
            border_spacing=10,
            anchor="w",
        )
        self._3_button.place(x=5, y=368)

        self._4_button: customtkinter.CTkButton = customtkinter.CTkButton(
            self.frame__navigation,
            text="Button 4",
            width=190,
            height=44,
            fg_color="#0a0a0a",
            hover_color="#1a1a1a",
            font=("Segoe UI", 14),
            image=customtkinter.CTkImage(
                light_image=assets.icons.material.overview,
                dark_image=assets.icons.material.overview,
                size=(20, 20),
            ),
            compound="left",
            border_spacing=10,
            anchor="w",
        )
        self._4_button.place(x=5, y=417)

        self._settings_button: customtkinter.CTkButton = customtkinter.CTkButton(
            self.frame__navigation,
            text="Settings",
            width=190,
            height=44,
            fg_color="#0a0a0a",
            hover_color="#1a1a1a",
            font=("Segoe UI", 14),
            image=customtkinter.CTkImage(
                light_image=assets.icons.material.overview,
                dark_image=assets.icons.material.overview,
                size=(20, 20),
            ),
            compound="left",
            border_spacing=10,
            anchor="w",
        )
        self._settings_button.place(x=5, y=466)

        transaction_carousel(self.frame__navigation)
