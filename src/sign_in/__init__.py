from . import *
from .dashboard import dashboard
from .signup import signup_interface
from .administrator import administrator


class login_interface:
    """
    Docstring for login_interface
    """

    def __init__(self) -> None:
        pass

    class login:
        """
        Docstring for login
        """

        def __init__(self) -> None:  # Initialize The Login Interface

            # --- X-Axis Configuration For Animation --- #

            self.x_axis_rtl = (
                +1110
            )  # login screen frame starts from right to left (initially outside the window) -- rtl
            self.x_axis_ltr = (
                -910
            )  # reset password screen frame starts from left to right (initially outside the window) -- ltr

            # --- Main Window Configuration --- #

            self.window = customtkinter.CTk()
            self.window.title(" ")
            self.window.geometry("1100x650+100+40")

            apply_style(self.window, "transparent")
            title_bar.hide(self.window, no_span=True)

            self.window.minsize(1100, 650)
            self.window.maxsize(1100, 650)

            self.window.bind(
                "<Button-1>",
                lambda event: move_tk_with_no_titlebar_winos_native_ctypes(
                    event, self.window
                ),
            )

            self.window.after(800, self.show_login_rtl)

            self.more_button = customtkinter.CTkButton(
                self.window,
                text="",
                image=customtkinter.CTkImage(
                    light_image=icon__more_horiz,
                    dark_image=icon__more_horiz,
                    size=(12, 12),
                ),
                width=0,
                height=0,
                corner_radius=0,
                hover_color="#43545F",
                fg_color="black",
                command=self.popup_at_exit_root,
            )

            self.more_button.place(x=1080, y=0)

            # --- Login Screen Configuration --- #

            self.frame__login = customtkinter.CTkFrame(self.window, corner_radius=0)
            self.frame__login.configure(width=900, height=610)
            self.frame__login.place(x=self.x_axis_rtl, y=20)

            self.internal_frame_00__login = customtkinter.CTkFrame(
                self.frame__login,
                width=450,
                height=610,
                fg_color="#000000",
                corner_radius=0,
            )

            # self.internal_frame_00__login.place(x=0, y=0)

            set_opacity(self.internal_frame_00__login.winfo_id(), 1)

            self.__login_banner = customtkinter.CTkLabel(
                self.internal_frame_00__login,
                text="",
                image=customtkinter.CTkImage(
                    light_image=image__banner_login,
                    dark_image=image__banner_login,
                    size=(450, 610),
                ),
            )

            self.__login_banner.place(x=0, y=0)

            set_opacity(self.__login_banner.winfo_id(), 1)

            self.internal_frame_01__login = customtkinter.CTkFrame(
                self.frame__login,
                width=450,
                height=610,
                fg_color="transparent",
                corner_radius=0,
            )

            # self.internal_frame_01__login.place(x=450, y=0)

            customtkinter.CTkLabel(
                self.internal_frame_01__login,
                text="Sign in to BWHF!",
                font=("Segoe UI", 29, "bold"),
                text_color="#FFFFFF",
                image=customtkinter.CTkImage(
                    light_image=icon__assured_workload,
                    dark_image=icon__assured_workload,
                    size=(64, 64),
                ),
                compound="top",
                height=0,
                width=0,
            ).place(x=109, y=88)

            # --- Username Entry --- #

            container_frame__username_login = customtkinter.CTkFrame(
                self.internal_frame_01__login,
                width=350,
                height=40,
                fg_color="transparent",
                border_width=1,
                border_color="#FFFFFF",
                corner_radius=6,
            )

            container_frame__username_label_login = customtkinter.CTkLabel(
                self.internal_frame_01__login,
                text="username or uuid",
                font=("Roboto", 10),
                height=12,
                width=83,  # 77
                text_color="#FFFFFF",
            )

            customtkinter.CTkLabel(
                container_frame__username_login,
                image=customtkinter.CTkImage(
                    light_image=icon__account_circle,
                    dark_image=icon__account_circle,
                    size=(20, 20),
                ),
                text="",
            ).place(x=8, rely=0.5, anchor="w")

            container_frame__username_login.place(x=50, y=280)

            self.__username = customtkinter.CTkEntry(
                container_frame__username_login,
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
                    container_frame__username_label_login.place(x=70, y=273)
                    if not self.__username.get()
                    else None
                ),
            )
            self.__username.bind(
                "<FocusOut>",
                lambda event: (
                    container_frame__username_label_login.place_forget()
                    if not self.__username.get()
                    else None
                ),
            )

            # --- Password Entry And Reset Password --- #

            container_frame__password_login = customtkinter.CTkFrame(
                self.internal_frame_01__login,
                width=350,
                height=40,
                fg_color="transparent",
                border_width=1,
                border_color="#FFFFFF",
                corner_radius=6,
            )

            container_frame__password_label_login = customtkinter.CTkLabel(
                self.internal_frame_01__login,
                text="password",
                font=("Roboto", 10),
                height=12,
                width=50,  # 44
                text_color="#FFFFFF",
            )

            customtkinter.CTkLabel(
                container_frame__password_login,
                image=customtkinter.CTkImage(
                    light_image=icon__password,
                    dark_image=icon__password,
                    size=(20, 20),
                ),
                text="",
            ).place(x=8, rely=0.5, anchor="w")

            container_frame__password_login.place(x=50, y=340)

            customtkinter.CTkButton(
                self.internal_frame_01__login,
                text="forgot password?",
                height=0,
                width=76,  # 74
                fg_color="transparent",
                hover=False,
                font=("Roboto", 9),
                text_color="#218CFF",
                border_spacing=0,
                command=self.hide_login_frame__show_reset_password_frame,
            ).place(x=302, y=371)

            self.__password = customtkinter.CTkEntry(
                container_frame__password_login,
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
                    container_frame__password_label_login.place(x=70, y=333)
                    if not self.__password.get()
                    else None
                ),
            )
            self.__password.bind(
                "<FocusOut>",
                lambda event: (
                    container_frame__password_label_login.place_forget()
                    if not self.__password.get()
                    else None
                ),
            )

            # --- Login And Sign Up Buttons --- #

            login_btn = customtkinter.CTkButton(
                self.internal_frame_01__login,
                text="Sign in",
                width=350,
                height=40,
                border_width=0,
                text_color="#000000",
                bg_color="transparent",
                fg_color="#FFFFFF",
                font=("Roboto", 16, "bold"),
                hover_color="light grey",
                corner_radius=6,
                command=self.validate_and_redirect_to_dashboard,
            )
            login_btn.place(x=50, y=430)

            set_opacity(login_btn.winfo_id(), 0.5)

            customtkinter.CTkLabel(
                self.internal_frame_01__login,
                text="New to Bank With High Functionalities? ",
                font=("Roboto", 12),
                width=0,
                height=0,
            ).place(x=65, y=480)

            customtkinter.CTkButton(
                self.internal_frame_01__login,
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
                self.window, corner_radius=0
            )

            self.frame__reset_password.configure(width=900, height=610)
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
                    light_image=image__banner_reset_password,
                    dark_image=image__banner_reset_password,
                    size=(450, 610),
                ),
            )
            self.__reset_password_banner.place(x=0, y=0)

            set_opacity(self.__reset_password_banner.winfo_id(), 1)

            self.__heading_reset_password = customtkinter.CTkLabel(
                self.frame__reset_password,
                text="Forgot Password",
                font=("Freestyle Script", 42, "bold"),
                width=5,
            )

            self.__greet_reset_password = customtkinter.CTkLabel(
                self.frame__reset_password,
                text="Get Your Account Back!",
                font=("Roboto", 20, "bold"),
                text_color="#57D956",
            )

            self.__subheading_reset_password = customtkinter.CTkLabel(
                self.frame__reset_password,
                text="Enter Required Credentials",
                font=("Roboto", 12),
                height=0,
            )

            # --- Username Entry At Reset Password Screen --- #

            self.__user_icon_label_reset_password = customtkinter.CTkLabel(
                self.frame__reset_password,
                text="Username",
                font=("Roboto", 24, "bold"),
                image=customtkinter.CTkImage(
                    light_image=icon__account_circle,
                    dark_image=icon__account_circle,
                    size=(40, 40),
                ),
                compound="top",
            )

            self.__username_at_reset_password = customtkinter.CTkEntry(
                self.frame__reset_password,
                placeholder_text="Example: Virati Akira Nandhan Reddy",
                height=40,
                width=340,
                corner_radius=5,
                font=("Roboto", 16),
            )

            # --- Security Code Entry At Reset Password Screen --- #

            self.__security_icon_label_reset_password = customtkinter.CTkLabel(
                self.frame__reset_password,
                text="Security Code",
                font=("Roboto", 24, "bold"),
                image=customtkinter.CTkImage(
                    light_image=icon__security, dark_image=icon__security, size=(40, 40)
                ),
                compound="top",
                height=0,
            )

            self.__forgot_security_code_button_reset_password = customtkinter.CTkButton(
                self.frame__reset_password,
                text="Forgot Security Code",
                height=0,
                width=0,
                fg_color="transparent",
                hover=False,
                font=("Roboto", 10),
                text_color="#218CFF",
                command=self.forgot_security_code,
            )

            self.__security_code_at_reset_password = customtkinter.CTkEntry(
                self.frame__reset_password,
                placeholder_text="Example: Viratiaki@Akki",
                height=40,
                width=340,
                corner_radius=5,
                font=("Roboto", 16),
            )

            # --- Request And Cancel Buttons At Reset Password Screen --- #

            self.__request_reset_password = customtkinter.CTkButton(
                self.frame__reset_password,
                text="Request",
                width=120,
                border_width=1,
                text_color="#3264FF",
                fg_color="transparent",
                font=("Roboto", 16, "bold"),
                hover_color="Light Blue",
                command=self.request_for_password_reset,
            )

            self.__cancel_reset_password = customtkinter.CTkButton(
                self.frame__reset_password,
                text="Cancel",
                fg_color="transparent",
                height=15,
                border_width=1,
                hover_color="#A1FB8E",
                width=45,
                command=self.hide_reset_password_frame__show_login_frame,
            )

            self.window.after(
                1500,
                lambda: [
                    self.internal_frame_00__login.place(x=0, y=0),
                    self.internal_frame_01__login.place(x=450, y=0),
                ],
            )

            # --- Miscellaneous --- #
            self.is_popped_up = False

            self.window.mainloop()

        def show_login_rtl(self) -> None:  # show login frame -- MOVE: right to left
            """
            ## Shows the login frame moving from right to left
            """

            self.x_axis_rtl -= 10

            if self.x_axis_rtl >= 180:

                self.frame__login.place(x=self.x_axis_rtl, y=20)
                self.window.after(10, self.show_login_rtl)

            if self.x_axis_rtl < 180:

                return

        def hide_login_rtl(self) -> None:  # hide login frame -- MOVE: left to right
            """
            ## Hides the login frame moving from left to right
            """

            self.x_axis_rtl += 10

            if self.x_axis_rtl <= 1110:

                self.frame__login.place(x=self.x_axis_rtl, y=20)
                self.window.after(10, self.hide_login_rtl)

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

        def hide_reset_password_frame__show_login_frame(
            self,
        ) -> (
            None
        ):  # Hides The Reset Password Screen Then Shows The Login Screen in The Window

            self.hide_contents_reset_password()
            self.hide_reset_password_ltr()
            self.show_login_rtl()

        def hide_login_frame__show_reset_password_frame(
            self,
        ) -> (
            None
        ):  # Hides The Login Screen Then Shows The Reset Password Screen in The Window

            self.hide_contents_login()
            self.hide_login_rtl()
            self.show_reset_password_ltr()

        def hide_contents_login(self) -> None:  # Hides The Contents Of The Login Screen

            for widget in []:

                widget.place_forget()

            else:

                self.window.after(900, self.show_contents_reset_password)

        def show_contents_reset_password(
            self,
        ) -> None:  # Shows The Contents Of The Reset Password Screen

            self.__heading_reset_password.place(x=105, y=2)
            self.__greet_reset_password.place(x=30, y=65)
            self.__subheading_reset_password.place(x=33, y=90)
            self.__user_icon_label_reset_password.place(x=140, y=140)
            self.__username_at_reset_password.place(x=30, y=204)
            self.__security_icon_label_reset_password.place(x=120, y=250)
            self.__forgot_security_code_button_reset_password.place(x=270, y=359)
            self.__security_code_at_reset_password.place(x=30, y=324)
            self.__request_reset_password.place(x=142, y=400)
            self.__cancel_reset_password.place(x=2, y=538)

        def hide_contents_reset_password(
            self,
        ) -> None:  # Hides The Contents Of The Reset Password Screen

            for widget in [
                self.__greet_reset_password,
                self.__cancel_reset_password,
                self.__heading_reset_password,
                self.__request_reset_password,
                self.__subheading_reset_password,
                self.__username_at_reset_password,
                self.__user_icon_label_reset_password,
                self.__security_code_at_reset_password,
                self.__security_icon_label_reset_password,
                self.__forgot_security_code_button_reset_password,
            ]:

                widget.place_forget()

            else:

                self.window.after(
                    900,
                    lambda: [
                        self.internal_frame_00__login.place(x=0, y=0),
                        self.internal_frame_01__login.place(x=450, y=0),
                    ],
                )

        def redirect_to_signup(self) -> None:  # Redirects To The Signup Module

            try:

                signup_window = signup_interface.signup(
                    self.window
                )  # Opening The Signup Window
                self.hide_contents_login()
                self.hide_login_rtl()

                def cancel_signup_action():
                    signup_window.hide_frame()
                    self.show_login_rtl()
                    self.window.after(
                        900,
                        lambda: [
                            self.internal_frame_00__login.place(x=0, y=0),
                            self.internal_frame_01__login.place(x=450, y=0),
                        ],
                    )

                self.window.after(480, signup_window.show_frame)
                customtkinter.CTkButton(
                    signup_window.frame__signup,
                    text="",
                    image=customtkinter.CTkImage(
                        light_image=icon__close, dark_image=icon__close, size=(20, 20)
                    ),
                    command=cancel_signup_action,
                    width=0,
                    corner_radius=0,
                    hover_color="#C42B1C",
                    fg_color="transparent",
                ).place(x=1032, y=0)
                # self.window.wait_window(signup_window.window__signup)

            except:

                self.window.deiconify()  # Re-Opening The Login Window If Any Error Occurs

        def validate_and_redirect_to_dashboard(
            self,
        ) -> None:  # Validates The User Credentials And Redirects To The Dashboard

            username = self.__username.get()
            password = self.__password.get()

            def redirect_to_dashboard():  # Redirects To The Dashboard

                try:

                    if SERVER.traversal().is_user_exists(username):

                        self.window.withdraw()
                        dashboard_window = dashboard(username, self.window)
                        self.window.wait_window(dashboard_window.window__dashboard)
                        self.window.deiconify()

                except:

                    ...

            if (not username) and password:  # username: false -- password: true
                auth__username_error = customtkinter.CTkLabel(
                    self.frame__login,
                    text="USERNAME IS INCOMPLETE",
                    text_color="Orange",
                )
                auth__username_error.place(x=133, y=442)
                auth__username_error.after(2000, auth__username_error.destroy)

            elif (
                username and not SERVER.traversal().is_user_exists(username)
            ) and password:  # username: true (not exists) -- password: true
                auth__username_not_exists_error = customtkinter.CTkLabel(
                    self.frame__login,
                    text="THE GIVEN USERNAME DOES NOT EXISTS",
                    text_color="Orange",
                )
                auth__username_not_exists_error.place(x=98, y=442)
                auth__username_not_exists_error.after(
                    2000, auth__username_not_exists_error.destroy
                )

            elif (not username) and (
                not password
            ):  # username: false -- password: false
                auth__username_password_error = customtkinter.CTkLabel(
                    self.frame__login,
                    text="USERNAME AND PASSWORD IS INCOMPLETE",
                    text_color="Orange",
                )
                auth__username_password_error.place(x=96, y=442)
                auth__username_password_error.after(
                    2000, auth__username_password_error.destroy
                )

            elif (not password) and username:  # username: true -- password: false
                auth__password_error = customtkinter.CTkLabel(
                    self.frame__login,
                    text="PASSWORD IS INCOMPLETE",
                    text_color="Orange",
                )
                auth__password_error.place(x=133, y=442)
                auth__password_error.after(2000, auth__password_error.destroy)

            elif username and (
                not SERVER.authentication().authenticate_password(username, password)
            ):  # username: true -- password: true (wrong)
                auth__password_rule_error = customtkinter.CTkLabel(
                    self.frame__login,
                    text="THE PASSWORD IS INCORRECT. TRY AGAIN!",
                    text_color="Orange",
                )
                auth__password_rule_error.place(x=100, y=442)
                auth__password_rule_error.after(2000, auth__password_rule_error.destroy)

            else:  # passed all the criteria
                auth__processing = customtkinter.CTkLabel(
                    self.frame__login, text="PROCESSING...", text_color="Orange"
                )
                auth__processing.place(x=166, y=442)
                auth__processing.after(2000, redirect_to_dashboard)

        def popup_at_exit_root(self) -> None:

            if self.is_popped_up:
                return

            def reset_popup() -> None:
                self.is_popped_up = False
                exit_root__popup.destroy()

            # Shows The Developer Window
            def Show_Developer_Window():
                reset_popup()

                # raise NotImplementedError('build a auth for developer')
                self.window.withdraw()
                developer_window = administrator(self.window)
                self.window.wait_window(developer_window.window__developer)
                self.window.deiconify()

            # Main Window For The License, Developer, Documentation
            exit_root__popup = customtkinter.CTkToplevel()
            exit_root__popup.geometry("220x182")
            exit_root__popup.resizable(False, False)
            exit_root__popup.protocol("WM_DELETE_WINDOW", reset_popup)
            exit_root__popup.title("")
            exit_root__popup.attributes("-topmost", True)

            # self.frame__login For The License, Developer, Documentation
            frame__exit_root__popup = customtkinter.CTkFrame(exit_root__popup)
            frame__exit_root__popup.configure(width=200, height=162)
            frame__exit_root__popup.place(x=10, y=10)

            customtkinter.CTkButton(
                frame__exit_root__popup,
                text="Developer",
                font=("Roboto", 16, "bold"),
                fg_color="Orange",
                hover_color="Yellow",
                text_color="Black",
                width=180,
                height=38,
                command=Show_Developer_Window,
            ).place(x=10, y=12)

            customtkinter.CTkButton(
                frame__exit_root__popup,
                text="Documentation",
                font=("Roboto", 16, "bold"),
                width=180,
                height=38,
                fg_color="#E63B60",
                hover_color="#067FD0",
                command=lambda: utils.Open_Browser_For_Specified_Internal_File(
                    rf"{DIR_PATH}\docs\index.html"
                ),
            ).place(x=10, y=62)
            self.is_popped_up = True

        def forgot_security_code(self):  # Handles The Forgot Security Code Action

            for widget in [
                self.__heading_reset_password,
                self.__greet_reset_password,
                self.__subheading_reset_password,
                self.__user_icon_label_reset_password,
                self.__username_at_reset_password,
                self.__security_icon_label_reset_password,
                self.__forgot_security_code_button_reset_password,
                self.__security_code_at_reset_password,
                self.__request_reset_password,
            ]:

                widget.place_forget()

        def request_for_password_reset(
            self,
        ):  # Handles The Request To Reset The Password

            username_at_reset_password = self.__username_at_reset_password.get()
            user_security_code_at_reset_password = (
                self.__security_code_at_reset_password.get()
            )

            def security_code_accepted():  # If The Security Code is Accepted Then Change The Password

                for widget in [
                    self.__greet_reset_password,
                    self.__cancel_reset_password,
                    self.__request_reset_password,
                    self.__heading_reset_password,
                    self.__subheading_reset_password,
                    self.__username_at_reset_password,
                    self.__user_icon_label_reset_password,
                    self.__security_code_at_reset_password,
                    self.__security_icon_label_reset_password,
                    self.__forgot_security_code_button_reset_password,
                ]:

                    widget.place_forget()

                self.__username_at_reset_password.delete(0, "end")
                self.__security_code_at_reset_password.delete(0, "end")

                def hide_contents_change_password():  # Hides The Contents Of The Change Password Screen

                    for widget in [
                        greet_change_password,
                        heading_change_password,
                        subeading_change_password,
                        cancel_reset_change_password,
                        new_password_reset_change_password,
                        new_password_label_change_password,
                        confirm_password_reset_change_password,
                        change_password_button_change_password,
                        confirm_password_label_change_password,
                    ]:

                        widget.place_forget()

                    self.__username_at_reset_password.delete(0, "end")
                    self.__security_code_at_reset_password.delete(0, "end")

                    self.hide_reset_password_frame__show_login_frame()

                def change_password():

                    new_password = new_password_reset_change_password.get()
                    confirm_password = confirm_password_reset_change_password.get()

                    if (not new_password) and confirm_password:  # np: false -- cp: true
                        New_Password_Error = customtkinter.CTkLabel(
                            self.frame__reset_password,
                            text="NEW PASSWORD IS INCOMPLETE",
                            text_color="Orange",
                        )
                        New_Password_Error.place(x=117, y=442)
                        New_Password_Error.after(2000, New_Password_Error.destroy)

                        return

                    elif new_password and (
                        not confirm_password
                    ):  # np: true -- cp: false
                        Confirm_Password_Error = customtkinter.CTkLabel(
                            self.frame__reset_password,
                            text="CONFIRM PASSWORD IS INCOMPLETE",
                            text_color="Orange",
                        )
                        Confirm_Password_Error.place(x=110, y=442)
                        Confirm_Password_Error.after(
                            2000, Confirm_Password_Error.destroy
                        )

                        return

                    elif (
                        new_password != confirm_password
                    ):  # np: true -- cp: true (np != cp)
                        Pass_differ_Error = customtkinter.CTkLabel(
                            self.frame__reset_password,
                            text="NEW PASSWORD AND CONFIRM PASSWORD IS DIFFERENT",
                            text_color="Orange",
                        )
                        Pass_differ_Error.place(x=58, y=442)
                        Pass_differ_Error.after(2000, Pass_differ_Error.destroy)

                        return

                    elif (not new_password) and (
                        not confirm_password
                    ):  # np: false -- cp: false
                        New_Confirm_Password_Error = customtkinter.CTkLabel(
                            self.frame__reset_password,
                            text="NEW PASSWORD AND CONFIRM PASSWORD ARE INCOMPLETE",
                            text_color="Orange",
                        )
                        New_Confirm_Password_Error.place(x=48, y=442)
                        New_Confirm_Password_Error.after(
                            2000, New_Confirm_Password_Error.destroy
                        )

                        return

                    elif (len(new_password) < 6) and (
                        not len(new_password) == 0
                    ):  # np: true ( < 6 chars ) -- cp: true
                        auth__password_rule_error = customtkinter.CTkLabel(
                            self.frame__reset_password,
                            text="PASSWORD MUST CONTAIN AT LEAST 6 CHARACTERS",
                            text_color="Orange",
                        )
                        auth__password_rule_error.place(x=70, y=442)
                        auth__password_rule_error.after(
                            2000, auth__password_rule_error.destroy
                        )

                        return

                    try:

                        is_password_changed = SERVER.accountactions().change_password(
                            username_at_reset_password, new_password
                        )

                        if is_password_changed:

                            Change_Successful = customtkinter.CTkLabel(
                                self.frame__reset_password,
                                text="PASSWORD CHANGED SUCCESSFULLU!\nREDIRECTING TO LOGIN SCREEN",
                                text_color="Orange",
                            )
                            Change_Successful.place(x=105, y=442)
                            Change_Successful.after(5000, Change_Successful.destroy)
                            self.frame__reset_password.after(
                                5000, hide_contents_change_password
                            )

                        else:
                            raise Exception

                    except:

                        Change_Pass_Error = customtkinter.CTkLabel(
                            self.frame__reset_password,
                            text="SOME ERROR OCCURRED ; PLEASE TRY AGAIN LATER!",
                            text_color="Orange",
                        )
                        Change_Pass_Error.place(x=77, y=442)
                        Change_Pass_Error.after(5000, Change_Pass_Error.destroy)
                        self.frame__reset_password.after(
                            5000, hide_contents_change_password
                        )

                # --- Change Password Configuration --- #

                greet_change_password = customtkinter.CTkLabel(
                    self.frame__reset_password,
                    text="Request Accepted",
                    font=("Roboto", 28, "bold"),
                    text_color="#57D956",
                )
                greet_change_password.place(x=75, y=10)

                heading_change_password = customtkinter.CTkLabel(
                    self.frame__reset_password,
                    text="You Are One Step Away",
                    font=("Roboto", 20, "bold"),
                    text_color="#57D956",
                )
                heading_change_password.place(x=30, y=75)

                subeading_change_password = customtkinter.CTkLabel(
                    self.frame__reset_password,
                    text="Enter Required Credentials To Log into Your Account",
                    font=("Roboto", 9),
                    height=0,
                )
                subeading_change_password.place(x=33, y=99)

                new_password_label_change_password = customtkinter.CTkLabel(
                    self.frame__reset_password,
                    text="New Password",
                    font=("Roboto", 18, "bold"),
                )
                new_password_label_change_password.place(x=30, y=208)

                new_password_reset_change_password = customtkinter.CTkEntry(
                    self.frame__reset_password,
                    placeholder_text="Example: johndoe@abc[123]",
                    height=40,
                    width=340,
                    corner_radius=5,
                    font=("Roboto", 16),
                )
                new_password_reset_change_password.place(x=30, y=230)

                confirm_password_label_change_password = customtkinter.CTkLabel(
                    self.frame__reset_password,
                    text="Confirm Password",
                    font=("Roboto", 18, "bold"),
                )
                confirm_password_label_change_password.place(x=30, y=288)

                confirm_password_reset_change_password = customtkinter.CTkEntry(
                    self.frame__reset_password,
                    placeholder_text="Example: johndoe@abc[123]",
                    height=40,
                    width=340,
                    corner_radius=5,
                    font=("Roboto", 16),
                )
                confirm_password_reset_change_password.place(x=30, y=310)

                change_password_button_change_password = customtkinter.CTkButton(
                    self.frame__reset_password,
                    text="Change Password",
                    width=140,
                    border_width=1,
                    text_color="#3264FF",
                    fg_color="transparent",
                    font=("Roboto", 16, "bold"),
                    hover_color="Light Blue",
                    command=change_password,
                )
                change_password_button_change_password.place(x=122, y=400)

                cancel_reset_change_password = customtkinter.CTkButton(
                    self.frame__reset_password,
                    text="Cancel",
                    fg_color="transparent",
                    height=15,
                    border_width=1,
                    hover_color="#A1FB8E",
                    width=45,
                    command=hide_contents_change_password,
                )
                cancel_reset_change_password.place(x=2, y=538)

            if (
                not username_at_reset_password
            ) and user_security_code_at_reset_password:  # username: false -- code: true
                auth__username_error = customtkinter.CTkLabel(
                    self.frame__reset_password,
                    text="USERNAME IS INCOMPLETE",
                    text_color="Orange",
                )
                auth__username_error.place(x=133, y=442)
                auth__username_error.after(2000, auth__username_error.destroy)

            elif (
                username_at_reset_password
                and not SERVER.traversal().is_user_exists(username_at_reset_password)
            ) and user_security_code_at_reset_password:  # username: true (not exists) -- password: true
                Username_Exists_Error = customtkinter.CTkLabel(
                    self.frame__reset_password,
                    text=f"THE GIVEN USERNAME DOES NOT EXISTS",
                    text_color="Orange",
                )
                Username_Exists_Error.place(x=98, y=442)
                Username_Exists_Error.after(2000, Username_Exists_Error.destroy)

            elif (not username_at_reset_password) and (
                not user_security_code_at_reset_password
            ):  # username: false -- code: false
                auth__username_password_error = customtkinter.CTkLabel(
                    self.frame__reset_password,
                    text="USERNAME AND SECURITY CODE IS INCOMPLETE",
                    text_color="Orange",
                )
                auth__username_password_error.place(x=85, y=442)
                auth__username_password_error.after(
                    2000, auth__username_password_error.destroy
                )

            elif (
                not user_security_code_at_reset_password
            ) and username_at_reset_password:  # username: true -- code: false
                auth__password_error = customtkinter.CTkLabel(
                    self.frame__reset_password,
                    text="SECURITY CODE IS INCOMPLETE",
                    text_color="Orange",
                )
                auth__password_error.place(x=126, y=442)
                auth__password_error.after(2000, auth__password_error.destroy)

            elif username_at_reset_password and (
                not SERVER.authentication().authenticate_security_code(
                    username_at_reset_password, user_security_code_at_reset_password
                )
            ):  # username: true -- code: true (wrong)
                auth__password_rule_error = customtkinter.CTkLabel(
                    self.frame__reset_password,
                    text="THE SECURITY CODE IS INCORRECT. TRY AGAIN!",
                    text_color="Orange",
                )
                auth__password_rule_error.place(x=87, y=442)
                auth__password_rule_error.after(2000, auth__password_rule_error.destroy)

            else:  # passed all the criteria
                auth__processing = customtkinter.CTkLabel(
                    self.frame__reset_password,
                    text="REQUESTING...",
                    text_color="Orange",
                )
                auth__processing.place(x=166, y=442)
                auth__processing.after(2000, auth__processing.place_forget)
                auth__processing.after(2000, security_code_accepted)
