from .views import *
from ._navigation__transaction_carousel import transaction_carousel
from .. import customtkinter, assets


class navigation:

    def __init__(self, parent_frame: customtkinter.CTkFrame, username: str) -> None:

        self.frame__navigation: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame, width=200, height=630, fg_color="#0a0a0a"
        )
        self.frame__navigation.place(x=10, y=10)

        self.current_frame: tuple[
            overview
            | users_and_access
            | issues_and_broadcasts
            | activity_and_history
            | settings,
            customtkinter.CTkButton,
        ]

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
        self.users_and_access: users_and_access = users_and_access(
            parent_frame, username
        )
        self.issues_and_broadcasts: issues_and_broadcasts = issues_and_broadcasts(
            parent_frame, username
        )
        self.activity_and_history: activity_and_history = activity_and_history(
            parent_frame
        )
        self.settings: settings = settings(parent_frame, username)

        self._overview_button: customtkinter.CTkButton = customtkinter.CTkButton(
            self.frame__navigation,
            text="Overview",
            width=190,
            height=44,
            fg_color="#0a0a0a",
            hover_color="#1a1a1a",
            text_color_disabled="#DCE4EE",
            font=("Segoe UI", 14),
            image=customtkinter.CTkImage(
                light_image=assets.icons.material.overview,
                dark_image=assets.icons.material.overview,
                size=(20, 20),
            ),
            command=lambda: self.place_views(self._overview_button, self.overview),
            compound="left",
            border_spacing=10,
            anchor="w",
        )
        self._overview_button.place(x=5, y=270)

        self.place_views(self._overview_button, self.overview)

        self._users_and_access_button: customtkinter.CTkButton = (
            customtkinter.CTkButton(
                self.frame__navigation,
                text="Users & Access",
                width=190,
                height=44,
                fg_color="#0a0a0a",
                hover_color="#1a1a1a",
                text_color_disabled="#DCE4EE",
                font=("Segoe UI", 14),
                image=customtkinter.CTkImage(
                    light_image=assets.icons.material.groups,
                    dark_image=assets.icons.material.groups,
                    size=(20, 20),
                ),
                command=lambda: self.place_views(
                    self._users_and_access_button, self.users_and_access
                ),
                compound="left",
                border_spacing=10,
                anchor="w",
            )
        )
        self._users_and_access_button.place(x=5, y=319)

        self._issues_and_broadcasts_button: customtkinter.CTkButton = (
            customtkinter.CTkButton(
                self.frame__navigation,
                text="Issues & Broadcasts",
                width=190,
                height=44,
                fg_color="#0a0a0a",
                hover_color="#1a1a1a",
                text_color_disabled="#DCE4EE",
                font=("Segoe UI", 14),
                image=customtkinter.CTkImage(
                    light_image=assets.icons.material.campaign,
                    dark_image=assets.icons.material.campaign,
                    size=(20, 20),
                ),
                command=lambda: self.place_views(
                    self._issues_and_broadcasts_button, self.issues_and_broadcasts
                ),
                compound="left",
                border_spacing=10,
                anchor="w",
            )
        )
        self._issues_and_broadcasts_button.place(x=5, y=368)

        self._activity_and_history_button: customtkinter.CTkButton = (
            customtkinter.CTkButton(
                self.frame__navigation,
                text="Activity & History",
                width=190,
                height=44,
                fg_color="#0a0a0a",
                hover_color="#1a1a1a",
                text_color_disabled="#DCE4EE",
                font=("Segoe UI", 14),
                image=customtkinter.CTkImage(
                    light_image=assets.icons.material.history_toggle_off,
                    dark_image=assets.icons.material.history_toggle_off,
                    size=(20, 20),
                ),
                command=lambda: self.place_views(
                    self._activity_and_history_button, self.activity_and_history
                ),
                compound="left",
                border_spacing=10,
                anchor="w",
            )
        )
        self._activity_and_history_button.place(x=5, y=417)

        self._settings_button: customtkinter.CTkButton = customtkinter.CTkButton(
            self.frame__navigation,
            text="Settings",
            width=190,
            height=44,
            fg_color="#0a0a0a",
            hover_color="#1a1a1a",
            text_color_disabled="#DCE4EE",
            font=("Segoe UI", 14),
            image=customtkinter.CTkImage(
                light_image=assets.icons.material.settings,
                dark_image=assets.icons.material.settings,
                size=(20, 20),
            ),
            command=lambda: self.place_views(self._settings_button, self.settings),
            compound="left",
            border_spacing=10,
            anchor="w",
        )
        self._settings_button.place(x=5, y=466)

        transaction_carousel(self.frame__navigation)

    def place_views(
        self,
        _button: customtkinter.CTkButton,
        view_object: (
            overview
            | users_and_access
            | issues_and_broadcasts
            | activity_and_history
            | settings
        ),
    ) -> None:

        if hasattr(self, "current_frame"):

            self.current_frame[0].hide_frame()
            self.current_frame[1].configure(fg_color="#0a0a0a", state="normal")

        _button.configure(fg_color="#1a1a1a", state="disabled")
        view_object.show_frame()

        self.current_frame = (view_object, _button)
