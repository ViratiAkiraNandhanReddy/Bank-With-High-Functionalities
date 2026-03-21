from ..sign_in import *
from ..administrator import administrator_interface


class more_actions_interface:

    def __init__(self) -> None:
        pass

    class frame__administrator:

        def __init__(
            self,
            parent_frame: customtkinter.CTkFrame,
            parent_window: customtkinter.CTk,
            _callback: Callable,
        ) -> None:

            self.parent_frame: customtkinter.CTkFrame = parent_frame
            self.parent_window: customtkinter.CTk = parent_window
            self.hide_overlay_callback: Callable = _callback

            self.internal_frame_00_more_actions = customtkinter.CTkFrame(
                self.parent_frame,
                width=306,
                height=406,
                border_width=2,
                border_color="gray",
                fg_color="transparent",
            )

            self.internal_frame_00_more_actions.place(x=724, y=30)

            self.if_00_container_frame_admin_sign_in__flow_sign_in = (
                customtkinter.CTkFrame(
                    self.internal_frame_00_more_actions,
                    width=300,
                    height=400,
                    fg_color="transparent",
                )
            )

            self.if_00_container_frame_admin_sign_in__flow_sign_in.place(x=3, y=3)

            customtkinter.CTkLabel(
                self.if_00_container_frame_admin_sign_in__flow_sign_in,
                text="Sign in to Admin's Dashboard",
                font=("Segoe UI", 16, "bold"),
                text_color="#FFFFFF",
                image=customtkinter.CTkImage(
                    light_image=icon__manage_accounts,
                    dark_image=icon__manage_accounts,
                    size=(42, 42),
                ),
                compound="top",
                height=0,
                width=0,
            ).place(x=36, y=68)

            self.container_frame__username_admin_sign_in = customtkinter.CTkFrame(
                self.if_00_container_frame_admin_sign_in__flow_sign_in,
                width=260,
                height=40,
                fg_color="transparent",
                border_width=1,
                border_color="#FFFFFF",
                corner_radius=6,
            )

            self.container_frame__username_label_admin_sign_in = customtkinter.CTkLabel(
                self.if_00_container_frame_admin_sign_in__flow_sign_in,
                text="username",
                font=("Roboto", 10),
                height=12,
                width=50,  # 44
                text_color="#FFFFFF",
            )

            customtkinter.CTkLabel(
                self.container_frame__username_admin_sign_in,
                image=customtkinter.CTkImage(
                    light_image=icon__account_circle,
                    dark_image=icon__account_circle,
                    size=(20, 20),
                ),
                text="",
            ).place(x=8, rely=0.5, anchor="w")

            self.container_frame__username_admin_sign_in.place(x=20, y=200)

            self.__username = customtkinter.CTkEntry(
                self.container_frame__username_admin_sign_in,
                placeholder_text="username",
                width=260 - 40,
                height=40 - 8,
                corner_radius=0,
                border_width=0,
                fg_color="transparent",
                font=("Roboto", 16),
            )
            self.__username.place(x=28, rely=0.5, anchor="w")

            self.__username.bind(
                "<FocusIn>",
                lambda event: (
                    self.container_frame__username_label_admin_sign_in.place(
                        x=40, y=193
                    )
                    if not self.__username.get()
                    else None
                ),
            )
            self.__username.bind(
                "<FocusOut>",
                lambda event: (
                    self.container_frame__username_label_admin_sign_in.place_forget()
                    if not self.__username.get()
                    else None
                ),
            )

            self.container_frame__password_admin_sign_in = customtkinter.CTkFrame(
                self.if_00_container_frame_admin_sign_in__flow_sign_in,
                width=260,
                height=40,
                fg_color="transparent",
                border_width=1,
                border_color="#FFFFFF",
                corner_radius=6,
            )

            self.container_frame__password_label_admin_sign_in = customtkinter.CTkLabel(
                self.if_00_container_frame_admin_sign_in__flow_sign_in,
                text="password",
                font=("Roboto", 10),
                height=12,
                width=50,  # 44
                text_color="#FFFFFF",
            )

            customtkinter.CTkLabel(
                self.container_frame__password_admin_sign_in,
                image=customtkinter.CTkImage(
                    light_image=icon__password,
                    dark_image=icon__password,
                    size=(20, 20),
                ),
                text="",
            ).place(x=8, rely=0.5, anchor="w")

            self.container_frame__password_admin_sign_in.place(x=20, y=260)

            customtkinter.CTkButton(
                self.if_00_container_frame_admin_sign_in__flow_sign_in,
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
                self.container_frame__password_admin_sign_in,
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
                    self.container_frame__password_label_admin_sign_in.place(
                        x=40, y=253
                    )
                    if not self.__password.get()
                    else None
                ),
            )
            self.__password.bind(
                "<FocusOut>",
                lambda event: (
                    self.container_frame__password_label_admin_sign_in.place_forget()
                    if not self.__password.get()
                    else None
                ),
            )

            administrator_sign_in_btn = customtkinter.CTkButton(
                self.if_00_container_frame_admin_sign_in__flow_sign_in,
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
            self.if_00_container_frame_admin_sign_in__flow_sign_in.place_forget()

        def validate_administrator_password(self) -> None:

            admin_username = self.__username.get().strip()
            admin_password = self.__password.get().strip()

            self.__username.bind(
                "<KeyPress>",
                lambda event: self.container_frame__username_admin_sign_in.configure(
                    border_color="#FFFFFF"
                )
                or self.container_frame__username_label_admin_sign_in.configure(
                    text_color="#FFFFFF"
                )
                or self.container_frame__username_label_admin_sign_in.configure(
                    text="username",
                    width=50,  # 44
                )
                or self.__username.unbind("<KeyPress>"),
            )

            self.__password.bind(
                "<KeyPress>",
                lambda event: self.container_frame__password_admin_sign_in.configure(
                    border_color="#FFFFFF"
                )
                or self.container_frame__password_label_admin_sign_in.configure(
                    text_color="#FFFFFF"
                )
                or self.container_frame__password_label_admin_sign_in.configure(
                    text="password",
                    width=50,  # 44
                )
                or self.__password.unbind("<KeyPress>"),
            )

            if (not admin_username) and admin_password:

                self.container_frame__username_admin_sign_in.configure(
                    border_color="#FF0000"
                )
                self.container_frame__username_label_admin_sign_in.configure(
                    text_color="#FF0000"
                )
                self.container_frame__username_label_admin_sign_in.configure(
                    text="invalid username", width=81
                )

                return

            elif admin_username and (not admin_password):

                self.container_frame__password_admin_sign_in.configure(
                    border_color="#FF0000"
                )
                self.container_frame__password_label_admin_sign_in.configure(
                    text_color="#FF0000"
                )
                self.container_frame__password_label_admin_sign_in.configure(
                    text="invalid password", width=81
                )

                return

            elif (not admin_username) and (not admin_password):

                self.container_frame__username_admin_sign_in.configure(
                    border_color="#FF0000"
                )
                self.container_frame__password_admin_sign_in.configure(
                    border_color="#FF0000"
                )
                self.container_frame__username_label_admin_sign_in.configure(
                    text="invalid username", width=81
                )

                self.container_frame__username_label_admin_sign_in.configure(
                    text_color="#FF0000"
                )
                self.container_frame__password_label_admin_sign_in.configure(
                    text_color="#FF0000"
                )
                self.container_frame__password_label_admin_sign_in.configure(
                    text="invalid password", width=81
                )

                return

            elif (admin_username and admin_password) and (
                (not SERVER.traversal().is_admin_exists(admin_username))
                or (
                    not SERVER.authentication().authenticate_admin(
                        admin_username, admin_password
                    )
                )
            ):

                self.container_frame__username_admin_sign_in.configure(
                    border_color="#FF0000"
                )
                self.container_frame__username_label_admin_sign_in.configure(
                    text_color="#FF0000"
                )
                self.container_frame__username_label_admin_sign_in.configure(
                    text="invalid username or password", width=137
                )

                self.container_frame__password_admin_sign_in.configure(
                    border_color="#FF0000"
                )
                self.container_frame__password_label_admin_sign_in.configure(
                    text_color="#FF0000"
                )
                self.container_frame__password_label_admin_sign_in.configure(
                    text="invalid username or password", width=137
                )

                return

            else:
                self.parent_window.withdraw()
                self.hide_overlay_callback()
                self.toplevel__admin_dashboard = administrator_interface.administrator(
                    self.parent_window
                )
                self.parent_window.wait_window(
                    self.toplevel__admin_dashboard.window__developer
                )
                self.parent_window.deiconify()

    class more_actions:

        def __init__(
            self, parent_window: customtkinter.CTk, _btn: customtkinter.CTkButton
        ) -> None:

            self.frame__more_actions = customtkinter.CTkFrame(
                parent_window, corner_radius=0
            )
            self.frame__more_actions.configure(width=1060, height=610)

            self.show_frame: Callable = lambda: (
                self.frame__more_actions.place(x=20, y=20),
                _btn.configure(state="disabled"),
            )
            self.hide_frame: Callable = lambda: (
                self.frame__more_actions.destroy(),
                _btn.configure(state="normal"),
            )

            more_actions_interface.frame__administrator(
                self.frame__more_actions, parent_window, self.hide_frame
            )
