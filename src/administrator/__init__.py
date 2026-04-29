from .. import *


class administrator_interface:

    def __init__(self) -> None:
        pass

    class administrator:

        def __init__(
            self, parent_window: customtkinter.CTk, _btn: customtkinter.CTkButton
        ):

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

            self.frame__developer = customtkinter.CTkFrame(
                self.frame__administrator, width=980, height=480
            )
            self.frame__developer.place(x=10, y=10)
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
            customtkinter.CTkButton(
                self.frame__developer,
                text="Exit",
                command=self.frame__administrator.destroy,
            ).place(x=200, y=300)

            dev.bind("<Leave>", lambda _: self.frame.place_forget())
