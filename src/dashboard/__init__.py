from .. import *
from .tiles import actions, messages, account_info, security


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

            customtkinter.CTkButton(
                self.frame__dashboard,
                text="",
                image=customtkinter.CTkImage(
                    light_image=assets.icons.material.exit_to_app,
                    dark_image=assets.icons.material.exit_to_app,
                    size=(25, 25),
                ),
                width=0,
                height=0,
                corner_radius=0,
                hover=False,
                fg_color="black",
                border_spacing=0,
                command=self.hide_frame,
            ).place(x=1060, y=10)

            self.frame__status_greeting: customtkinter.CTkFrame = (
                customtkinter.CTkFrame(
                    self.frame__dashboard, width=800, height=30, fg_color="#0a0a0a"
                )
            )
            self.frame__status_greeting.place(x=10, y=10)

            self.full_name = SERVER.lookup.user.full_name(username)

            customtkinter.CTkLabel(
                self.frame__status_greeting,
                text=(
                    utils.greetings.current()
                    + ", "
                    + (
                        self.full_name
                        if len(self.full_name) < 96
                        else self.full_name[:93] + "..."
                    )
                ),
                font=("Roboto", 14),
                height=30,
                width=780,
                anchor="w",
            ).place(x=10, y=0)

            self.frame__status_utilities: customtkinter.CTkFrame = (
                customtkinter.CTkFrame(
                    self.frame__dashboard, width=230, height=30, fg_color="#0a0a0a"
                )
            )
            self.frame__status_utilities.place(x=820, y=10)

            self.actions = actions(self.frame__dashboard, username)

            self.messages = messages(self.frame__dashboard, username)

            self.security = security(self.frame__dashboard, username)

            self.account_info = account_info(self.frame__dashboard, username)
