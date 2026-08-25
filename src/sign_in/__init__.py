from .. import *
from ..sign_up import sign_up_interface
from ..dashboard import dashboard_interface
from .more_actions import more_actions_interface


class sign_in_interface:
    """
    Docstring for sign_in_interface
    """

    def __init__(self) -> None:
        pass

    class sign_in:
        """
        Docstring for sign_in
        """

        def __init__(self) -> None:  # Initialize The Sign In Interface

            # --- X-Axis Configuration For Animation --- #

            self.x_axis_rtl = (
                +1110
            )  # sign in screen frame starts from right to left (initially outside the window) -- rtl
            self.x_axis_ltr = (
                -910
            )  # reset password screen frame starts from left to right (initially outside the window) -- ltr

            # --- Main Window Configuration --- #

            self.window: customtkinter.CTk = customtkinter.CTk()

            _width, _height = 1100, 650
            _x_pos: int = int((self.window.winfo_screenwidth() / 2) - (_width / 2))
            _y_pos: int = int((self.window.winfo_screenheight() / 2) - (_height / 2))

            self.window.title("Bank With High Functionalities")
            self.window.geometry(f"{_width}x{_height}+{_x_pos}+{_y_pos}")
            self.window.iconbitmap(
                utils.root / "assets" / "brand" / "logo" / "favicon.ico"
            )

            apply_style(self.window, "transparent")
            title_bar.hide(self.window, no_span=True)

            self.window.minsize(_width, _height)
            self.window.maxsize(_width, _height)

            self.window.bind(
                # Enables native Win32 window dragging for the borderless window by simulating a standard title bar drag operation.
                # This restores default Windows drag behavior, including smooth movement and proper DWM-managed window interactions
                # despite the absence of a native title bar.
                "<Button-1>",
                lambda _event: borderless_window_utils.enable_native_window_drag_via_win32_message(
                    _event, self.window
                ),
            )

            self.window.bind(
                # Fixes the hPyT title_bar.hide(no_span=True) side effect where Windows restores the window with stale non-client
                # frame metrics after minimization, causing unintended geometry expansion and an extra bottom gap. Reapplying the
                # modified window styles and forcing a native frame recalculation on the <Map> event ensures the borderless window
                # is restored with the correct dimensions and frame layout.
                "<Map>",
                lambda _event: borderless_window_utils.disable_minimize_btn_and_force_window_frame_refresh(
                    _event, self.window
                ),
            )

            self.window.after(800, self.show_sign_in_rtl)

            self.more_button: customtkinter.CTkButton = customtkinter.CTkButton(
                self.window,
                text="",
                image=customtkinter.CTkImage(
                    light_image=assets.icons.material.more_horiz,
                    dark_image=assets.icons.material.more_horiz,
                    size=(12, 12),
                ),
                width=0,
                height=0,
                corner_radius=0,
                hover_color="#43545F",
                fg_color="black",
                command=self.more_action__overlay_frame,
            )

            self.more_button.place(x=1080, y=0)

            # --- Sign In Screen Configuration --- #

            self.frame__sign_in: customtkinter.CTkFrame = customtkinter.CTkFrame(
                self.window, corner_radius=0, width=900, height=610
            )
            self.frame__sign_in.place(x=self.x_axis_rtl, y=20)

            self.internal_frame_00__sign_in: customtkinter.CTkFrame = (
                customtkinter.CTkFrame(
                    self.frame__sign_in,
                    width=450,
                    height=610,
                    fg_color="#000000",
                    corner_radius=0,
                )
            )

            # self.internal_frame_00__sign_in.place(x=0, y=0)

            set_opacity(self.internal_frame_00__sign_in.winfo_id(), 1)

            self.__sign_in_banner: customtkinter.CTkLabel = customtkinter.CTkLabel(
                self.internal_frame_00__sign_in,
                text="",
                image=customtkinter.CTkImage(
                    light_image=assets.banners.signin_sidebar_bg,
                    dark_image=assets.banners.signin_sidebar_bg,
                    size=(450, 610),
                ),
            )

            self.__sign_in_banner.place(x=0, y=0)

            set_opacity(self.__sign_in_banner.winfo_id(), 1)

            self.internal_frame_01__sign_in: customtkinter.CTkFrame = (
                customtkinter.CTkFrame(
                    self.frame__sign_in,
                    width=450,
                    height=610,
                    fg_color="transparent",
                    corner_radius=0,
                )
            )

            # self.internal_frame_01__sign_in.place(x=450, y=0)

            customtkinter.CTkLabel(
                self.internal_frame_01__sign_in,
                text="Sign in to BWHF!",
                font=("Segoe UI", 29, "bold"),
                text_color="#FFFFFF",
                image=customtkinter.CTkImage(
                    light_image=assets.icons.material.assured_workload,
                    dark_image=assets.icons.material.assured_workload,
                    size=(64, 64),
                ),
                compound="top",
                height=0,
                width=0,
            ).place(x=109, y=88)

            # --- Username Entry --- #

            self.container_frame__username_sign_in: customtkinter.CTkFrame = (
                customtkinter.CTkFrame(
                    self.internal_frame_01__sign_in,
                    width=350,
                    height=40,
                    fg_color="transparent",
                    border_width=1,
                    border_color="#FFFFFF",
                    corner_radius=6,
                )
            )

            self.container_frame__username_label_sign_in: customtkinter.CTkLabel = (
                customtkinter.CTkLabel(
                    self.internal_frame_01__sign_in,
                    text="username or uuid",
                    font=("Roboto", 10),
                    height=12,
                    width=83,  # 77
                    text_color="#FFFFFF",
                )
            )

            customtkinter.CTkLabel(
                self.container_frame__username_sign_in,
                image=customtkinter.CTkImage(
                    light_image=assets.icons.material.account_circle,
                    dark_image=assets.icons.material.account_circle,
                    size=(20, 20),
                ),
                text="",
            ).place(x=8, rely=0.5, anchor="w")

            self.container_frame__username_sign_in.place(x=50, y=280)

            self.__username: customtkinter.CTkEntry = customtkinter.CTkEntry(
                self.container_frame__username_sign_in,
                placeholder_text="username or uuid",
                width=350 - 40,
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
                    self.container_frame__username_label_sign_in.place(x=70, y=273)
                    if not self.__username.get()
                    else None
                ),
            )
            self.__username.bind(
                "<FocusOut>",
                lambda event: (
                    self.container_frame__username_label_sign_in.place_forget()
                    if not self.__username.get()
                    else None
                ),
            )

            # --- Password Entry And Reset Password --- #

            self.container_frame__password_sign_in = customtkinter.CTkFrame(
                self.internal_frame_01__sign_in,
                width=350,
                height=40,
                fg_color="transparent",
                border_width=1,
                border_color="#FFFFFF",
                corner_radius=6,
            )

            self.container_frame__password_label_sign_in = customtkinter.CTkLabel(
                self.internal_frame_01__sign_in,
                text="password",
                font=("Roboto", 10),
                height=12,
                width=50,  # 44
                text_color="#FFFFFF",
            )

            customtkinter.CTkLabel(
                self.container_frame__password_sign_in,
                image=customtkinter.CTkImage(
                    light_image=assets.icons.material.password,
                    dark_image=assets.icons.material.password,
                    size=(20, 20),
                ),
                text="",
            ).place(x=8, rely=0.5, anchor="w")

            self.container_frame__password_sign_in.place(x=50, y=340)

            customtkinter.CTkButton(
                self.internal_frame_01__sign_in,
                text="forgot password?",
                height=0,
                width=76,  # 74
                fg_color="transparent",
                hover=False,
                font=("Roboto", 9),
                text_color="#218CFF",
                border_spacing=0,
                command=self.hide_sign_in_frame__show_reset_password_frame,
            ).place(x=302, y=371)

            self.__password = customtkinter.CTkEntry(
                self.container_frame__password_sign_in,
                placeholder_text="password",
                width=350 - 40,
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
                    self.container_frame__password_label_sign_in.place(x=70, y=333)
                    if not self.__password.get()
                    else None
                ),
            )
            self.__password.bind(
                "<FocusOut>",
                lambda event: (
                    self.container_frame__password_label_sign_in.place_forget()
                    if not self.__password.get()
                    else None
                ),
            )

            # --- Sign In And Sign Up Buttons --- #

            sign_in_btn = customtkinter.CTkButton(
                self.internal_frame_01__sign_in,
                text="Sign in",
                width=350,
                height=40,
                border_width=0,
                text_color="#000000",
                bg_color="transparent",
                fg_color="#818181",
                font=("Roboto", 16, "bold"),
                hover_color="#929090",
                corner_radius=6,
                command=self.validate_and_redirect_to_dashboard,
            )
            sign_in_btn.place(x=50, y=430)

            customtkinter.CTkLabel(
                self.internal_frame_01__sign_in,
                text="New to Bank With High Functionalities? ",
                font=("Roboto", 12),
                width=0,
                height=0,
            ).place(x=65, y=480)

            customtkinter.CTkButton(
                self.internal_frame_01__sign_in,
                text="Create an account",
                width=0,
                height=0,
                text_color="#218CFF",
                fg_color="transparent",
                font=("Roboto", 12),
                hover=False,
                border_spacing=0,
                command=self.redirect_to_signup,
            ).place(x=281, y=478)

            # --- Reset Password Screen Configuration --- #

            self.frame__reset_password = customtkinter.CTkFrame(
                self.window, corner_radius=0, width=900, height=610
            )

            self.frame__reset_password.place(x=self.x_axis_ltr, y=20)

            self.internal_frame_00__reset_password = customtkinter.CTkFrame(
                self.frame__reset_password,
                width=450,
                height=610,
                fg_color="#000000",
                corner_radius=0,
            )
            self.internal_frame_00__reset_password.place(x=450, y=0)

            set_opacity(self.internal_frame_00__reset_password.winfo_id(), 1)

            self.__reset_password_banner = customtkinter.CTkLabel(
                self.internal_frame_00__reset_password,
                text="",
                image=customtkinter.CTkImage(
                    light_image=assets.banners.reset_pwd_sidebar_bg,
                    dark_image=assets.banners.reset_pwd_sidebar_bg,
                    size=(450, 610),
                ),
            )
            self.__reset_password_banner.place(x=0, y=0)

            set_opacity(self.__reset_password_banner.winfo_id(), 1)

            self.internal_frame_01__reset_password = customtkinter.CTkFrame(
                self.frame__reset_password,
                width=450,
                height=610,
                corner_radius=0,
            )
            self.internal_frame_01__reset_password.place(x=0, y=0)

            self.window.after(
                1500,
                lambda: [
                    self.internal_frame_00__sign_in.place(x=0, y=0),
                    self.internal_frame_01__sign_in.place(x=450, y=0),
                ],
            )

            self.window.mainloop()

        def show_sign_in_rtl(self) -> None:  # show sign in frame -- MOVE: right to left
            """
            ## Shows the sign in frame moving from right to left
            """

            self.x_axis_rtl -= 10

            if self.x_axis_rtl >= 180:

                self.frame__sign_in.place(x=self.x_axis_rtl, y=20)
                self.window.after(10, self.show_sign_in_rtl)

            if self.x_axis_rtl < 180:

                return

        def hide_sign_in_rtl(self) -> None:  # hide sign in frame -- MOVE: left to right
            """
            ## Hides the sign in frame moving from left to right
            """

            self.x_axis_rtl += 10

            if self.x_axis_rtl <= 1110:

                self.frame__sign_in.place(x=self.x_axis_rtl, y=20)
                self.window.after(10, self.hide_sign_in_rtl)

            if self.x_axis_rtl > 1110:

                return

        def show_reset_password_ltr(
            self,
        ) -> None:  # show reset password frame -- MOVE: left to right
            """
            ## Shows the reset password frame moving from left to right
            """

            self.x_axis_ltr += 10

            if self.x_axis_ltr <= 20:

                self.frame__reset_password.place(x=self.x_axis_ltr, y=20)
                self.window.after(10, self.show_reset_password_ltr)

            if self.x_axis_ltr >= 20:

                return

        def hide_reset_password_ltr(
            self,
        ) -> None:  # hide reset password frame -- MOVE: right to left
            """
            ## Hides the reset password frame moving from right to left
            """

            self.x_axis_ltr -= 10

            if self.x_axis_ltr >= -910:

                self.frame__reset_password.place(x=self.x_axis_ltr, y=20)
                self.window.after(10, self.hide_reset_password_ltr)

            if self.x_axis_ltr < -910:

                return

        def hide_reset_password_frame__show_sign_in_frame(
            self,
        ) -> (
            None
        ):  # Hides The Reset Password Screen Then Shows The Sign In Screen in The Window

            self.window.after(
                900,
                lambda: [
                    self.internal_frame_00__sign_in.place(x=0, y=0),
                    self.internal_frame_01__sign_in.place(x=450, y=0),
                ],
            )
            self.hide_reset_password_ltr()
            self.show_sign_in_rtl()

        def hide_sign_in_frame__show_reset_password_frame(
            self,
        ) -> (
            None
        ):  # Hides The Sign In Screen Then Shows The Reset Password Screen in The Window

            self.forgot_user_password()
            self.hide_sign_in_rtl()
            self.show_reset_password_ltr()

        def redirect_to_signup(self) -> None:  # Redirects To The Signup Module

            try:

                overlay_frame__signup = sign_up_interface.sign_up(
                    self.window
                )  # Opening The Signup Window
                self.hide_sign_in_rtl()

                def cancel_signup_action():
                    overlay_frame__signup.hide_frame()
                    self.show_sign_in_rtl()
                    self.window.after(
                        900,
                        lambda: [
                            self.internal_frame_00__sign_in.place(x=0, y=0),
                            self.internal_frame_01__sign_in.place(x=450, y=0),
                        ],
                    )

                self.window.after(1860, overlay_frame__signup.show_frame)

                customtkinter.CTkButton(
                    overlay_frame__signup.frame__signup,
                    text="",
                    image=customtkinter.CTkImage(
                        light_image=assets.icons.material.close,
                        dark_image=assets.icons.material.close,
                        size=(20, 20),
                    ),
                    command=cancel_signup_action,
                    width=0,
                    corner_radius=0,
                    hover_color="#ff0000",
                    fg_color="transparent",
                ).place(x=1032, y=0)

            except:

                raise NotImplementedError

        def validate_and_redirect_to_dashboard(
            self,
        ) -> None:  # Validates The User Credentials And Redirects To The Dashboard

            username = self.__username.get().strip()
            password = self.__password.get().strip()

            self.__username.bind(
                "<KeyPress>",
                lambda event: self.container_frame__username_sign_in.configure(
                    border_color="#FFFFFF"
                )
                or self.container_frame__username_label_sign_in.configure(
                    text_color="#FFFFFF",
                    text="username or uuid",
                    width=83,  # 77
                )
                or self.__username.unbind("<KeyPress>"),
            )

            self.__password.bind(
                "<KeyPress>",
                lambda event: self.container_frame__password_sign_in.configure(
                    border_color="#FFFFFF"
                )
                or self.container_frame__password_label_sign_in.configure(
                    text_color="#FFFFFF",
                    text="password",
                    width=50,  # 44
                )
                or self.__password.unbind("<KeyPress>"),
            )

            if (not username) and password:  # username: false -- password: true

                self.container_frame__username_sign_in.configure(border_color="#FF0000")

                self.container_frame__username_label_sign_in.configure(
                    text="invalid username or uuid",
                    width=112,
                    text_color="#FF0000",
                )

                return

            if (not password) and username:  # username: true -- password: false

                self.container_frame__password_sign_in.configure(border_color="#FF0000")

                self.container_frame__password_label_sign_in.configure(
                    text="invalid password",
                    width=81,
                    text_color="#FF0000",
                )

                return

            if (not username) and (not password):  # username: false -- password: false

                self.container_frame__username_sign_in.configure(border_color="#FF0000")
                self.container_frame__password_sign_in.configure(border_color="#FF0000")

                self.container_frame__username_label_sign_in.configure(
                    text="invalid username or uuid",
                    width=112,
                    text_color="#FF0000",
                )

                self.container_frame__password_label_sign_in.configure(
                    text="invalid password",
                    width=81,
                    text_color="#FF0000",
                )

                return

            user_exists = SERVER.lookup.user.exists(username)

            if (not user_exists) or (
                not SERVER.authentication.user.password(username, password)
            ):  # username: true (not exists) -- password: true --[or]-- username: true (exists) -- password: true (wrong)

                self.container_frame__username_sign_in.configure(border_color="#FF0000")
                self.container_frame__password_sign_in.configure(border_color="#FF0000")

                self.container_frame__username_label_sign_in.configure(
                    text="invalid username/uuid or password",
                    width=160,
                    text_color="#FF0000",
                )
                self.container_frame__password_label_sign_in.configure(
                    text="invalid username/uuid or password",
                    width=160,
                    text_color="#FF0000",
                )

                if user_exists:

                    SERVER.management.security_event.record(username, "failed_login")

                return

            SERVER.management.security_event.record(username, "login")

            self.overlay_frame__user_dashboard = dashboard_interface.dashboard(
                self.window, self.more_button, username
            )
            self.overlay_frame__user_dashboard.show_frame()

            self.__username.delete(0, "end")
            self.__password.delete(0, "end")

            self.container_frame__username_label_sign_in.place_forget()
            self.container_frame__password_label_sign_in.place_forget()

        def more_action__overlay_frame(self) -> None:

            try:

                overlay_frame__more_actions = more_actions_interface.more_actions(
                    self.window,
                    self.more_button,
                )  # Opening The More Action Overlay Frame

                self.window.after(480, overlay_frame__more_actions.show_frame)

                customtkinter.CTkButton(
                    overlay_frame__more_actions.frame__more_actions,
                    text="",
                    image=customtkinter.CTkImage(
                        light_image=assets.icons.material.close,
                        dark_image=assets.icons.material.close,
                        size=(20, 20),
                    ),
                    command=overlay_frame__more_actions.hide_frame,
                    width=0,
                    corner_radius=0,
                    hover_color="#ff0000",
                    fg_color="transparent",
                ).place(x=1032, y=0)

            except:

                raise NotImplementedError

        def forgot_user_password(self) -> None:

            _is_internet_connection_available: bool = utils.connection.is_connected()

            def _password_reset(username: str) -> None:

                pass

            def opted_email_verification_via_otp() -> None:

                pass

            def opted_backup_code_verification() -> None:

                self.if_00_container_frame__reset_password.place_forget()
                
                if_backupcode_container_frame__reset_password: customtkinter.CTkFrame = (
                    customtkinter.CTkFrame(
                        self.internal_frame_01__reset_password,
                        width=300,
                        height=400,
                        fg_color="transparent",
                    )
                )
                if_backupcode_container_frame__reset_password.place(x=0, y=0)
                
                customtkinter.CTkLabel(
                    if_backupcode_container_frame__reset_password,
                    text="Verify Account Ownership",
                    font=("Segoe UI", 16, "bold"),
                    text_color="#FFFFFF",
                    image=customtkinter.CTkImage(
                        light_image=assets.icons.material.shield_lock,
                        dark_image=assets.icons.material.shield_lock,
                        size=(42, 42),
                    ),
                    compound="top",
                    height=0,
                    width=0,
                ).place(x=50, y=53)
                
                customtkinter.CTkLabel(
                    if_backupcode_container_frame__reset_password,
                    text="""Use the permanent backup recovery code
                associated with your user account
                to continue secure recovery verification.""",
                    font=("Roboto", 11),
                    text_color="#FFFFFF",
                    height=0,  # 39
                    width=260,
                ).place(x=20, y=169)
                
                def validate_backup_code() -> None:
                
                    username: str = __username.get().strip()
                    backup_code: str = __backup_code.get().strip()
                
                    __username.bind(
                        "<KeyPress>",
                        lambda event: container_frame__username_admin_reset_password.configure(
                            border_color="#FFFFFF"
                        )
                        or container_frame__username_label_admin_reset_password.configure(
                            text_color="#FFFFFF"
                        )
                        or container_frame__username_label_admin_reset_password.configure(
                            text="username",
                            width=50,  # 44
                        )
                        or self.__username.unbind("<KeyPress>"),
                    )
                    __backup_code.bind(
                        "<KeyPress>",
                        lambda event: container_frame__backup_code_admin_reset_password.configure(
                            border_color="#FFFFFF"
                        )
                        or container_frame__backup_code_label_admin_reset_backup_code.configure(
                            text_color="#FFFFFF"
                        )
                        or container_frame__backup_code_label_admin_reset_backup_code.configure(
                            text="backup code",
                            width=63,  # 57
                        )
                        or __backup_code.unbind("<KeyPress>"),
                    )
                
                    if (
                        not username
                    ) and backup_code:  # username: false -- backup_code: true
                
                        container_frame__username_admin_reset_password.configure(
                            border_color="#FF0000"
                        )
                        container_frame__username_label_admin_reset_password.configure(
                            text_color="#FF0000"
                        )
                        container_frame__username_label_admin_reset_password.configure(
                            text="invalid username", width=81
                        )
                
                        return
                
                    elif username and (
                        not backup_code
                    ):  # username: true -- backup_code: false
                
                        container_frame__backup_code_admin_reset_password.configure(
                            border_color="#FF0000"
                        )
                        container_frame__backup_code_label_admin_reset_backup_code.configure(
                            text_color="#FF0000"
                        )
                        container_frame__backup_code_label_admin_reset_backup_code.configure(
                            text="invalid backup code", width=93
                        )
                
                        return
                
                    elif (not username) and (
                        not backup_code
                    ):  # username: false -- backup_code: false
                
                        container_frame__username_admin_reset_password.configure(
                            border_color="#FF0000"
                        )
                        container_frame__backup_code_admin_reset_password.configure(
                            border_color="#FF0000"
                        )
                        container_frame__username_label_admin_reset_password.configure(
                            text="invalid username", width=81
                        )
                
                        container_frame__username_label_admin_reset_password.configure(
                            text_color="#FF0000"
                        )
                        container_frame__backup_code_label_admin_reset_backup_code.configure(
                            text_color="#FF0000"
                        )
                        container_frame__backup_code_label_admin_reset_backup_code.configure(
                            text="invalid backup code", width=93
                        )
                
                        return
                
                    elif (username and backup_code) and (
                        (not SERVER.lookup.admin.exists(username))
                        or (
                            not SERVER.authentication.admin.backup_code(
                                username, backup_code
                            )
                        )
                    ):
                        # username: true (not exists) -- backup_code: true [or]
                        # username: true (exists) -- backup_code: true (wrong)
                
                        container_frame__username_admin_reset_password.configure(
                            border_color="#FF0000"
                        )
                        container_frame__username_label_admin_reset_password.configure(
                            text_color="#FF0000"
                        )
                        container_frame__username_label_admin_reset_password.configure(
                            text="invalid username or backup code", width=150
                        )
                
                        container_frame__backup_code_admin_reset_password.configure(
                            border_color="#FF0000"
                        )
                        container_frame__backup_code_label_admin_reset_backup_code.configure(
                            text_color="#FF0000"
                        )
                        container_frame__backup_code_label_admin_reset_backup_code.configure(
                            text="invalid username or backup code", width=150
                        )
                
                        return
                
                    else:
                        _password_reset(username)
                        if_backupcode_container_frame__reset_password.place_forget()
                        if_backupcode_container_frame__reset_password.destroy()
                
                container_frame__username_admin_reset_password: (
                    customtkinter.CTkFrame
                ) = customtkinter.CTkFrame(
                    if_backupcode_container_frame__reset_password,
                    width=260,
                    height=40,
                    fg_color="transparent",
                    border_width=1,
                    border_color="#FFFFFF",
                    corner_radius=6,
                )
                
                container_frame__username_label_admin_reset_password: (
                    customtkinter.CTkLabel
                ) = customtkinter.CTkLabel(
                    if_backupcode_container_frame__reset_password,
                    text="username",
                    font=("Roboto", 10),
                    height=12,
                    width=50,  # 44
                    text_color="#FFFFFF",
                )
                
                customtkinter.CTkLabel(
                    container_frame__username_admin_reset_password,
                    image=customtkinter.CTkImage(
                        light_image=assets.icons.material.account_circle,
                        dark_image=assets.icons.material.account_circle,
                        size=(20, 20),
                    ),
                    text="",
                ).place(x=8, rely=0.5, anchor="w")
                
                container_frame__username_admin_reset_password.place(x=20, y=232)
                
                __username: customtkinter.CTkEntry = customtkinter.CTkEntry(
                    container_frame__username_admin_reset_password,
                    placeholder_text="username",
                    width=260 - 40,
                    height=40 - 8,
                    corner_radius=0,
                    border_width=0,
                    fg_color="transparent",
                    font=("Roboto", 16),
                )
                __username.place(x=28, rely=0.5, anchor="w")
                
                __username.bind(
                    "<FocusIn>",
                    lambda event: (
                        container_frame__username_label_admin_reset_password.place(
                            x=40, y=225
                        )
                        if not __username.get()
                        else None
                    ),
                )
                __username.bind(
                    "<FocusOut>",
                    lambda event: (
                        container_frame__username_label_admin_reset_password.place_forget()
                        if not __username.get()
                        else None
                    ),
                )
                
                container_frame__backup_code_admin_reset_password: (
                    customtkinter.CTkFrame
                ) = customtkinter.CTkFrame(
                    if_backupcode_container_frame__reset_password,
                    width=260,
                    height=40,
                    fg_color="transparent",
                    border_width=1,
                    border_color="#FFFFFF",
                    corner_radius=6,
                )
                
                container_frame__backup_code_label_admin_reset_backup_code: (
                    customtkinter.CTkLabel
                ) = customtkinter.CTkLabel(
                    if_backupcode_container_frame__reset_password,
                    text="backup code",
                    font=("Roboto", 10),
                    height=12,
                    width=63,  # 57
                    text_color="#FFFFFF",
                )
                
                customtkinter.CTkLabel(
                    container_frame__backup_code_admin_reset_password,
                    image=customtkinter.CTkImage(
                        light_image=assets.icons.material.password,
                        dark_image=assets.icons.material.password,
                        size=(20, 20),
                    ),
                    text="",
                ).place(x=8, rely=0.5, anchor="w")
                
                container_frame__backup_code_admin_reset_password.place(x=20, y=292)
                
                __backup_code: customtkinter.CTkEntry = customtkinter.CTkEntry(
                    container_frame__backup_code_admin_reset_password,
                    placeholder_text="backup code",
                    width=260 - 40,
                    height=40 - 8,
                    corner_radius=0,
                    border_width=0,
                    fg_color="transparent",
                    font=("Roboto", 16),
                    show="•",
                )
                __backup_code.place(x=28, rely=0.5, anchor="w")
                
                __backup_code.bind(
                    "<FocusIn>",
                    lambda event: (
                        container_frame__backup_code_label_admin_reset_backup_code.place(
                            x=40, y=285
                        )
                        if not __backup_code.get()
                        else None
                    ),
                )
                __backup_code.bind(
                    "<FocusOut>",
                    lambda event: (
                        container_frame__backup_code_label_admin_reset_backup_code.place_forget()
                        if not __backup_code.get()
                        else None
                    ),
                )
                
                btn__back_if_backupcode: customtkinter.CTkButton = (
                    customtkinter.CTkButton(
                        if_backupcode_container_frame__reset_password,
                        text="",
                        width=0,  # 28
                        height=0,  # 28
                        fg_color="transparent",
                        hover=False,
                        image=customtkinter.CTkImage(
                            light_image=assets.icons.material.arrow_back,
                            dark_image=assets.icons.material.arrow_back,
                            size=(20, 20),
                        ),
                        command=lambda: (
                            self.if_00_container_frame__reset_password.place(x=3, y=3),
                            if_backupcode_container_frame__reset_password.place_forget(),
                            if_backupcode_container_frame__reset_password.destroy(),
                        ),
                    )
                )
                btn__back_if_backupcode.place(x=20, y=352)
                
                btn__forward_if_backupcode: customtkinter.CTkButton = (
                    customtkinter.CTkButton(
                        if_backupcode_container_frame__reset_password,
                        text="",
                        width=0,  # 28
                        height=0,  # 28
                        fg_color="transparent",
                        hover=False,
                        image=customtkinter.CTkImage(
                            light_image=assets.icons.material.arrow_forward,
                            dark_image=assets.icons.material.arrow_forward,
                            size=(20, 20),
                        ),
                        command=validate_backup_code,
                    )
                )
                btn__forward_if_backupcode.place(x=252, y=352)

            self.if_00_container_frame__reset_password: customtkinter.CTkFrame = (
                customtkinter.CTkFrame(
                    self.internal_frame_01__reset_password,
                    width=450,
                    height=610,
                    fg_color="transparent",
                )
            )
            self.if_00_container_frame__reset_password.place(x=0, y=0)

            _ = customtkinter.CTkLabel(
                self.if_00_container_frame__reset_password,
                text="Choose a Verification Method",
                font=("Segoe UI", 22, "bold"),
                text_color="#FFFFFF",
                image=customtkinter.CTkImage(
                    light_image=assets.icons.material.lock_person,
                    dark_image=assets.icons.material.lock_person,
                    size=(64, 64),
                ),
                compound="top",
                height=0,  # 104
                width=0,  # 307
            )
            _.place(x=71, y=88)  # x = 71.5, y = 88
            _.after(1000, lambda: print(_.winfo_width(), _.winfo_height()))

            self.btn__email_verification_via_otp: customtkinter.CTkButton = (
                customtkinter.CTkButton(
                    self.if_00_container_frame__reset_password,
                    text="""Verify your user account ownership using the
  one-time password sent to your email address.""",
                    width=410,
                    height=100,
                    border_width=0,
                    text_color="#FFFFFF",
                    bg_color="transparent",
                    fg_color="#1B1B1B",
                    font=("Roboto", 14),
                    hover_color="#252525",
                    corner_radius=6,
                    image=customtkinter.CTkImage(
                        light_image=assets.icons.material.chevron_forward,
                        dark_image=assets.icons.material.chevron_forward,
                        size=(30, 30),
                    ),
                    compound="right",
                    command=opted_email_verification_via_otp,
                )
            )
            self.btn__email_verification_via_otp.place(x=20, y=280)

            if not _is_internet_connection_available:

                self.btn__email_verification_via_otp.configure(
                    state="disabled",
                    fg_color="#3a3a3a",
                    text_color_disabled="#a0a0a0",
                )

                customtkinter.CTkLabel(
                    self.btn__email_verification_via_otp,
                    text="  No internet connection available",
                    font=("Segoe UI", 9),
                    text_color="#a0a0a0",
                    width=0,
                    height=0,
                    image=customtkinter.CTkImage(
                        light_image=assets.icons.material.wifi_off,
                        dark_image=assets.icons.material.wifi_off,
                        size=(12, 12),
                    ),
                    compound="left",
                ).place(x=58, y=46)

            self.btn__backup_code_verification: customtkinter.CTkButton = (
                customtkinter.CTkButton(
                    self.if_00_container_frame__reset_password,
                    text="""Verify your user account ownership using the
backup recovery code linked to your account.""",
                    width=410,
                    height=100,
                    border_width=0,
                    text_color="#FFFFFF",
                    bg_color="transparent",
                    fg_color="#1B1B1B",
                    font=("Roboto", 14),
                    hover_color="#252525",
                    corner_radius=6,
                    image=customtkinter.CTkImage(
                        light_image=assets.icons.material.chevron_forward,
                        dark_image=assets.icons.material.chevron_forward,
                        size=(30, 30),
                    ),
                    compound="right",
                    command=opted_backup_code_verification,
                )
            )
            self.btn__backup_code_verification.place(x=20, y=392)

            self.btn__back_to_sign_in: customtkinter.CTkButton = (
                customtkinter.CTkButton(
                    self.if_00_container_frame__reset_password,
                    text="",
                    width=0,  # 28
                    height=0,  # 28
                    fg_color="transparent",
                    hover=False,
                    image=customtkinter.CTkImage(
                        light_image=assets.icons.material.arrow_back,
                        dark_image=assets.icons.material.arrow_back,
                        size=(20, 20),
                    ),
                    command=self.hide_reset_password_frame__show_sign_in_frame,
                )
            )
            self.btn__back_to_sign_in.place(x=20, y=562)
