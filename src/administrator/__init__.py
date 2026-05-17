from .. import *
from ._navigation import navigation
from ._status_panel import status_panel


class administrator_interface:

    def __init__(self) -> None:
        pass

    class administrator:

        def __init__(
            self, parent_window: customtkinter.CTk, _btn: customtkinter.CTkButton
        ) -> None:

            self.frame__administrator = customtkinter.CTkFrame(
                parent_window, corner_radius=0, fg_color="black"
            )
            self.frame__administrator.configure(width=1100, height=650)

            self.show_frame: Callable = lambda: (
                self.frame__administrator.place(x=0, y=0),
                _btn.place_forget(),
            )
            self.hide_frame: Callable = lambda: (
                self.frame__administrator.place_forget(),
                _btn.place(x=1080, y=0),
            )

            navigation(self.frame__administrator)
            status_panel(self.frame__administrator)

            customtkinter.CTkButton(
                self.frame__administrator,
                text="",
                image=customtkinter.CTkImage(
                    light_image=icon__exit_to_app,
                    dark_image=icon__exit_to_app,
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

            self.frame__developer = customtkinter.CTkFrame(
                self.frame__administrator, width=870, height=480
            )
            self.frame__developer.place(x=220, y=50)
            self.frame = customtkinter.CTkFrame(
                self.frame__developer, width=100, height=100
            )

            dev = customtkinter.CTkButton(
                self.frame__developer,
                text="",
                image=customtkinter.CTkImage(
                    light_image=icon__developer_mode_tv,
                    dark_image=icon__developer_mode_tv,
                    size=(10, 10),
                ),
                fg_color="transparent",
                hover=False,
                width=0,
                height=0,
            )
            dev.place(x=89, y=100)
            dev.bind("<Motion>", lambda _: self.frame.place(x=0, y=0))
            dev.bind("<Leave>", lambda _: self.frame.place_forget())
