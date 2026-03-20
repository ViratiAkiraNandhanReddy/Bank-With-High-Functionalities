from ..sign_in import *
from ..administrator import administrator_interface


class more_actions_interface:

    def __init__(self) -> None:
        pass

    class frame__administrator:

        def __init__(self, parent_frame: customtkinter.CTkFrame):

            self.internal_frame_00_more_actions = customtkinter.CTkFrame(
                parent_frame,
                width=300,
                height=400,
                border_width=2,
                border_color="gray",
                fg_color="transparent",
            )

            self.internal_frame_00_more_actions.place(x=730, y=30)

            container_frame__password_admin_sign_in = customtkinter.CTkFrame(
                self.internal_frame_00_more_actions,
                width=260,
                height=40,
                fg_color="transparent",
                border_width=1,
                border_color="#FFFFFF",
                corner_radius=6,
            )

            container_frame__password_label_admin_sign_in = customtkinter.CTkLabel(
                self.internal_frame_00_more_actions,
                text="password",
                font=("Roboto", 10),
                height=12,
                width=50,  # 44
                text_color="#FFFFFF",
            )

            customtkinter.CTkLabel(
                container_frame__password_admin_sign_in,
                image=customtkinter.CTkImage(
                    light_image=icon__password,
                    dark_image=icon__password,
                    size=(20, 20),
                ),
                text="",
            ).place(x=8, rely=0.5, anchor="w")

            container_frame__password_admin_sign_in.place(x=20, y=260)

            customtkinter.CTkButton(
                self.internal_frame_00_more_actions,
                text="forgot password?",
                height=0,
                width=76,  # 74
                fg_color="transparent",
                hover=False,
                font=("Roboto", 9),
                text_color="#218CFF",
                border_spacing=0,
                command=self.forgot_administrator_password,
            ).place(x=182, y=291)

            self.__password = customtkinter.CTkEntry(
                container_frame__password_admin_sign_in,
                placeholder_text="password",
                width=260 - 40,
                height=40 - 8,
                corner_radius=0,
                border_width=0,
                fg_color="transparent",
                font=("Roboto", 16),
                show="•",
            )
            self.__password.place(x=28, rely=0.5, anchor="w")

            self.__password.bind(
                "<FocusIn>",
                lambda event: (
                    container_frame__password_label_admin_sign_in.place(x=40, y=253)
                    if not self.__password.get()
                    else None
                ),
            )
            self.__password.bind(
                "<FocusOut>",
                lambda event: (
                    container_frame__password_label_admin_sign_in.place_forget()
                    if not self.__password.get()
                    else None
                ),
            )

            administrator_sign_in_btn = customtkinter.CTkButton(
                self.internal_frame_00_more_actions,
                text="Sign in",
                width=260,
                height=40,
                border_width=0,
                text_color="#000000",
                bg_color="transparent",
                fg_color="#FFFFFF",
                font=("Roboto", 16, "bold"),
                hover_color="light grey",
                corner_radius=6,
                command=self.validate_administrator_password,
            )
            administrator_sign_in_btn.place(x=20, y=340)

            set_opacity(administrator_sign_in_btn.winfo_id(), 0.5)

        def forgot_administrator_password(self):
            pass

        def validate_administrator_password(self):
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

            more_actions_interface.frame__administrator(self.frame__more_actions)
