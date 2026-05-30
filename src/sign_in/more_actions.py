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
            _btn: customtkinter.CTkButton,
        ) -> None:

            self.parent_frame: customtkinter.CTkFrame = parent_frame
            self.parent_window: customtkinter.CTk = parent_window
            self.hide_overlay_callback: Callable = _callback
            self._btn: customtkinter.CTkButton = _btn

            self.internal_frame_00_more_actions: customtkinter.CTkFrame = (
                customtkinter.CTkFrame(
                    self.parent_frame,
                    width=306,
                    height=406,
                    border_width=2,
                    border_color="gray",
                    fg_color="transparent",
                )
            )

            self.internal_frame_00_more_actions.place(x=724, y=30)

            self.if_00_container_frame_admin_sign_in: customtkinter.CTkFrame = (
                customtkinter.CTkFrame(
                    self.internal_frame_00_more_actions,
                    width=300,
                    height=400,
                    fg_color="transparent",
                )
            )
            self.if_00_container_frame_admin_sign_in.place(x=3, y=3)

            customtkinter.CTkLabel(
                self.if_00_container_frame_admin_sign_in,
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

            self.container_frame__username_admin_sign_in: customtkinter.CTkFrame = (
                customtkinter.CTkFrame(
                    self.if_00_container_frame_admin_sign_in,
                    width=260,
                    height=40,
                    fg_color="transparent",
                    border_width=1,
                    border_color="#FFFFFF",
                    corner_radius=6,
                )
            )

            self.container_frame__username_label_admin_sign_in: (
                customtkinter.CTkLabel
            ) = customtkinter.CTkLabel(
                self.if_00_container_frame_admin_sign_in,
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

            self.__username: customtkinter.CTkEntry = customtkinter.CTkEntry(
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

            self.container_frame__password_admin_sign_in: customtkinter.CTkFrame = (
                customtkinter.CTkFrame(
                    self.if_00_container_frame_admin_sign_in,
                    width=260,
                    height=40,
                    fg_color="transparent",
                    border_width=1,
                    border_color="#FFFFFF",
                    corner_radius=6,
                )
            )

            self.container_frame__password_label_admin_sign_in: (
                customtkinter.CTkLabel
            ) = customtkinter.CTkLabel(
                self.if_00_container_frame_admin_sign_in,
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
                self.if_00_container_frame_admin_sign_in,
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

            self.__password: customtkinter.CTkEntry = customtkinter.CTkEntry(
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

            administrator_sign_in_btn: customtkinter.CTkButton = (
                customtkinter.CTkButton(
                    self.if_00_container_frame_admin_sign_in,
                    text="Sign in",
                    width=260,
                    height=40,
                    border_width=0,
                    text_color="#000000",
                    bg_color="transparent",
                    fg_color="#818181",
                    font=("Roboto", 16, "bold"),
                    hover_color="#929090",
                    corner_radius=6,
                    command=self.validate_administrator_password,
                )
            )
            administrator_sign_in_btn.place(x=20, y=340)

        def forgot_administrator_password(self) -> None:

            self.if_00_container_frame_admin_sign_in.place_forget()

            _is_internet_connection_available: bool = utils.connection.is_connected()

            def _password_reset() -> None:

                pass

            def opted_email_verification_via_otp() -> None:

                self.if_01_container_frame_admin_sign_in.place_forget()

                if_emailotp_container_frame_admin_sign_in: customtkinter.CTkFrame = (
                    customtkinter.CTkFrame(
                        self.internal_frame_00_more_actions,
                        width=300,
                        height=400,
                        fg_color="transparent",
                    )
                )
                if_emailotp_container_frame_admin_sign_in.place(x=3, y=3)

                customtkinter.CTkLabel(
                    if_emailotp_container_frame_admin_sign_in,
                    text="Verify Account Ownership",
                    font=("Segoe UI", 16, "bold"),
                    text_color="#FFFFFF",
                    image=customtkinter.CTkImage(
                        light_image=icon__shield_lock,
                        dark_image=icon__shield_lock,
                        size=(42, 42),
                    ),
                    compound="top",
                    height=0,
                    width=0,
                ).place(x=50, y=53)

                customtkinter.CTkLabel(
                    if_emailotp_container_frame_admin_sign_in,
                    text="""Use the registered recovery email associated
with your administrator account to continue
secure OTP verification.""",
                    font=("Roboto", 11),
                    text_color="#FFFFFF",
                    height=0,  # 39
                    width=260,
                ).place(x=20, y=169)

                def _recovery_confirmation_state_emailotp(_email: str) -> None:

                    if_emailotp_confirmation_state_container_frame_admin_sign_in: (
                        customtkinter.CTkFrame
                    ) = customtkinter.CTkFrame(
                        self.internal_frame_00_more_actions,
                        width=300,
                        height=400,
                        fg_color="transparent",
                    )
                    if_emailotp_confirmation_state_container_frame_admin_sign_in.place(
                        x=3, y=3
                    )

                    customtkinter.CTkLabel(
                        if_emailotp_confirmation_state_container_frame_admin_sign_in,
                        text="Recovery Email Confirmation",
                        font=("Segoe UI", 16, "bold"),
                        text_color="#FFFFFF",
                        image=customtkinter.CTkImage(
                            light_image=icon__mail,
                            dark_image=icon__mail,
                            size=(42, 42),
                        ),
                        compound="top",
                        height=0,  # 63
                        width=0,  # 223
                    ).place(x=38, y=53)

                    customtkinter.CTkLabel(
                        if_emailotp_confirmation_state_container_frame_admin_sign_in,
                        text="""A verification OTP will be sent to the
registered recovery email associated with
your administrator account.""",
                        font=("Roboto", 11),
                        text_color="#FFFFFF",
                        height=0,  # 39
                        width=260,
                    ).place(x=20, y=169)

                    entry__container_masked_email_address_emailotp_confirmation_state: (
                        customtkinter.CTkEntry
                    ) = customtkinter.CTkEntry(
                        if_emailotp_confirmation_state_container_frame_admin_sign_in,
                        width=260,
                        height=40,
                        font=("Consolas", 16),
                        fg_color="transparent",
                        border_width=1,
                        border_color="#FFFFFF",
                        corner_radius=6,
                        justify="center",
                    )
                    entry__container_masked_email_address_emailotp_confirmation_state.place(
                        x=20, y=260
                    )

                    entry__container_masked_email_address_emailotp_confirmation_state.insert(
                        0,
                        utils.masking.mask_email(_email),
                    )
                    entry__container_masked_email_address_emailotp_confirmation_state.configure(
                        state="readonly"
                    )

                    if (
                        len(_email) > 27
                    ):  # if email length exceeds entry width, show scroll buttons

                        moveleft_btn = customtkinter.CTkButton(
                            if_emailotp_confirmation_state_container_frame_admin_sign_in,
                            text="",
                            height=0,
                            width=0,
                            border_spacing=0,
                            fg_color="transparent",
                            hover=False,
                            image=customtkinter.CTkImage(
                                light_image=icon__chevron_backward,
                                dark_image=icon__chevron_backward,
                                size=(14, 14),
                            ),
                            command=lambda: entry__container_masked_email_address_emailotp_confirmation_state.xview_scroll(
                                -5, "units"
                            ),
                        )
                        moveleft_btn.place(x=120, y=300)

                        moveright_btn = customtkinter.CTkButton(
                            if_emailotp_confirmation_state_container_frame_admin_sign_in,
                            text="",
                            height=0,
                            width=0,
                            border_spacing=0,
                            fg_color="transparent",
                            hover=False,
                            image=customtkinter.CTkImage(
                                light_image=icon__chevron_forward,
                                dark_image=icon__chevron_forward,
                                size=(14, 14),
                            ),
                            command=lambda: entry__container_masked_email_address_emailotp_confirmation_state.xview_scroll(
                                5, "units"
                            ),
                        )
                        moveright_btn.place(x=160, y=300)

                    btn__back_if_emailotp_confirmation_state: (
                        customtkinter.CTkButton
                    ) = customtkinter.CTkButton(
                        if_emailotp_confirmation_state_container_frame_admin_sign_in,
                        text="",
                        width=0,  # 28
                        height=0,  # 28
                        fg_color="transparent",
                        hover=False,
                        image=customtkinter.CTkImage(
                            light_image=icon__arrow_back,
                            dark_image=icon__arrow_back,
                            size=(20, 20),
                        ),
                        command=lambda: (
                            if_emailotp_container_frame_admin_sign_in.place(x=3, y=3),
                            if_emailotp_confirmation_state_container_frame_admin_sign_in.place_forget(),
                            if_emailotp_confirmation_state_container_frame_admin_sign_in.destroy(),
                        ),
                    )
                    btn__back_if_emailotp_confirmation_state.place(x=20, y=352)

                    btn__forward_if_emailotp_confirmation_state: (
                        customtkinter.CTkButton
                    ) = customtkinter.CTkButton(
                        if_emailotp_confirmation_state_container_frame_admin_sign_in,
                        text="",
                        width=0,  # 28
                        height=0,  # 28
                        fg_color="transparent",
                        hover=False,
                        image=customtkinter.CTkImage(
                            light_image=icon__arrow_forward,
                            dark_image=icon__arrow_forward,
                            size=(20, 20),
                        ),
                    )
                    btn__forward_if_emailotp_confirmation_state.place(x=252, y=352)

                def validate_email_address() -> None:

                    username: str = __username.get().strip()
                    email_address: str = __email_address.get().strip()

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
                    __email_address.bind(
                        "<KeyPress>",
                        lambda event: container_frame__email_address_admin_reset_password.configure(
                            border_color="#FFFFFF"
                        )
                        or container_frame__email_address_label_admin_reset_password.configure(
                            text_color="#FFFFFF"
                        )
                        or container_frame__email_address_label_admin_reset_password.configure(
                            text="email address",
                            width=66,  # 60
                        )
                        or __email_address.unbind("<KeyPress>"),
                    )

                    if (
                        not username
                    ) and email_address:  # username: false -- email_address: true

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
                        not email_address
                    ):  # username: true -- email_address: false

                        container_frame__email_address_admin_reset_password.configure(
                            border_color="#FF0000"
                        )
                        container_frame__email_address_label_admin_reset_password.configure(
                            text_color="#FF0000"
                        )
                        container_frame__email_address_label_admin_reset_password.configure(
                            text="invalid email address", width=96
                        )

                        return

                    elif (not username) and (
                        not email_address
                    ):  # username: false -- email_address: false

                        container_frame__username_admin_reset_password.configure(
                            border_color="#FF0000"
                        )
                        container_frame__email_address_admin_reset_password.configure(
                            border_color="#FF0000"
                        )
                        container_frame__username_label_admin_reset_password.configure(
                            text="invalid username", width=81
                        )

                        container_frame__username_label_admin_reset_password.configure(
                            text_color="#FF0000"
                        )
                        container_frame__email_address_label_admin_reset_password.configure(
                            text_color="#FF0000"
                        )
                        container_frame__email_address_label_admin_reset_password.configure(
                            text="invalid email address", width=96
                        )

                        return

                    elif (username and email_address) and (
                        (not SERVER.traversal().is_admin_exists(username))
                        or (
                            not SERVER.authentication().authenticate_admin_email_address(
                                username, email_address
                            )
                        )
                    ):
                        # username: true (not exists) -- email_address: true [or]
                        # username: true (exists) -- email_address: true (wrong)

                        container_frame__username_admin_reset_password.configure(
                            border_color="#FF0000"
                        )
                        container_frame__username_label_admin_reset_password.configure(
                            text_color="#FF0000"
                        )
                        container_frame__username_label_admin_reset_password.configure(
                            text="invalid username or email address", width=153
                        )

                        container_frame__email_address_admin_reset_password.configure(
                            border_color="#FF0000"
                        )
                        container_frame__email_address_label_admin_reset_password.configure(
                            text_color="#FF0000"
                        )
                        container_frame__email_address_label_admin_reset_password.configure(
                            text="invalid username or email address", width=153
                        )

                        return

                    else:
                        _recovery_confirmation_state_emailotp(email_address)
                        if_emailotp_container_frame_admin_sign_in.place_forget()

                container_frame__username_admin_reset_password: (
                    customtkinter.CTkFrame
                ) = customtkinter.CTkFrame(
                    if_emailotp_container_frame_admin_sign_in,
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
                    if_emailotp_container_frame_admin_sign_in,
                    text="username",
                    font=("Roboto", 10),
                    height=12,
                    width=50,  # 44
                    text_color="#FFFFFF",
                )

                customtkinter.CTkLabel(
                    container_frame__username_admin_reset_password,
                    image=customtkinter.CTkImage(
                        light_image=icon__account_circle,
                        dark_image=icon__account_circle,
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

                container_frame__email_address_admin_reset_password: (
                    customtkinter.CTkFrame
                ) = customtkinter.CTkFrame(
                    if_emailotp_container_frame_admin_sign_in,
                    width=260,
                    height=40,
                    fg_color="transparent",
                    border_width=1,
                    border_color="#FFFFFF",
                    corner_radius=6,
                )

                container_frame__email_address_label_admin_reset_password: (
                    customtkinter.CTkLabel
                ) = customtkinter.CTkLabel(
                    if_emailotp_container_frame_admin_sign_in,
                    text="email address",
                    font=("Roboto", 10),
                    height=12,
                    width=66,  # 60
                    text_color="#FFFFFF",
                )

                customtkinter.CTkLabel(
                    container_frame__email_address_admin_reset_password,
                    image=customtkinter.CTkImage(
                        light_image=icon__mail,
                        dark_image=icon__mail,
                        size=(20, 20),
                    ),
                    text="",
                ).place(x=8, rely=0.5, anchor="w")

                container_frame__email_address_admin_reset_password.place(x=20, y=292)

                __email_address: customtkinter.CTkEntry = customtkinter.CTkEntry(
                    container_frame__email_address_admin_reset_password,
                    placeholder_text="email address",
                    width=260 - 40,
                    height=40 - 8,
                    corner_radius=0,
                    border_width=0,
                    fg_color="transparent",
                    font=("Roboto", 16),
                    show="•",
                )
                __email_address.place(x=28, rely=0.5, anchor="w")

                __email_address.bind(
                    "<FocusIn>",
                    lambda event: (
                        container_frame__email_address_label_admin_reset_password.place(
                            x=40, y=285
                        )
                        if not __email_address.get()
                        else None
                    ),
                )
                __email_address.bind(
                    "<FocusOut>",
                    lambda event: (
                        container_frame__email_address_label_admin_reset_password.place_forget()
                        if not __email_address.get()
                        else None
                    ),
                )

                btn__back_if_emailotp: customtkinter.CTkButton = (
                    customtkinter.CTkButton(
                        if_emailotp_container_frame_admin_sign_in,
                        text="",
                        width=0,
                        height=0,
                        fg_color="transparent",
                        hover=False,
                        image=customtkinter.CTkImage(
                            light_image=icon__arrow_back,
                            dark_image=icon__arrow_back,
                            size=(20, 20),
                        ),
                        command=lambda: (
                            self.if_01_container_frame_admin_sign_in.place(x=3, y=3),
                            if_emailotp_container_frame_admin_sign_in.place_forget(),
                            if_emailotp_container_frame_admin_sign_in.destroy(),
                        ),
                    )
                )
                btn__back_if_emailotp.place(x=20, y=352)

                btn__forward_if_emailotp: customtkinter.CTkButton = (
                    customtkinter.CTkButton(
                        if_emailotp_container_frame_admin_sign_in,
                        text="",
                        width=0,  # 28
                        height=0,  # 28
                        fg_color="transparent",
                        hover=False,
                        image=customtkinter.CTkImage(
                            light_image=icon__arrow_forward,
                            dark_image=icon__arrow_forward,
                            size=(20, 20),
                        ),
                        command=validate_email_address,
                    )
                )
                btn__forward_if_emailotp.place(x=252, y=352)

            def opted_backup_code_verification() -> None:

                self.if_01_container_frame_admin_sign_in.place_forget()

                if_backupcode_container_frame_admin_sign_in: customtkinter.CTkFrame = (
                    customtkinter.CTkFrame(
                        self.internal_frame_00_more_actions,
                        width=300,
                        height=400,
                        fg_color="transparent",
                    )
                )
                if_backupcode_container_frame_admin_sign_in.place(x=3, y=3)

                customtkinter.CTkLabel(
                    if_backupcode_container_frame_admin_sign_in,
                    text="Verify Account Ownership",
                    font=("Segoe UI", 16, "bold"),
                    text_color="#FFFFFF",
                    image=customtkinter.CTkImage(
                        light_image=icon__shield_lock,
                        dark_image=icon__shield_lock,
                        size=(42, 42),
                    ),
                    compound="top",
                    height=0,
                    width=0,
                ).place(x=50, y=53)

                customtkinter.CTkLabel(
                    if_backupcode_container_frame_admin_sign_in,
                    text="""Use the permanent backup recovery code
associated with your administrator account
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
                        (not SERVER.traversal().is_admin_exists(username))
                        or (
                            not SERVER.authentication().authenticate_admin_backup_code(
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
                        _password_reset()
                        if_backupcode_container_frame_admin_sign_in.place_forget()
                        if_backupcode_container_frame_admin_sign_in.destroy()

                container_frame__username_admin_reset_password: (
                    customtkinter.CTkFrame
                ) = customtkinter.CTkFrame(
                    if_backupcode_container_frame_admin_sign_in,
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
                    if_backupcode_container_frame_admin_sign_in,
                    text="username",
                    font=("Roboto", 10),
                    height=12,
                    width=50,  # 44
                    text_color="#FFFFFF",
                )

                customtkinter.CTkLabel(
                    container_frame__username_admin_reset_password,
                    image=customtkinter.CTkImage(
                        light_image=icon__account_circle,
                        dark_image=icon__account_circle,
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
                    if_backupcode_container_frame_admin_sign_in,
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
                    if_backupcode_container_frame_admin_sign_in,
                    text="backup code",
                    font=("Roboto", 10),
                    height=12,
                    width=63,  # 57
                    text_color="#FFFFFF",
                )

                customtkinter.CTkLabel(
                    container_frame__backup_code_admin_reset_password,
                    image=customtkinter.CTkImage(
                        light_image=icon__password,
                        dark_image=icon__password,
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
                        if_backupcode_container_frame_admin_sign_in,
                        text="",
                        width=0,  # 28
                        height=0,  # 28
                        fg_color="transparent",
                        hover=False,
                        image=customtkinter.CTkImage(
                            light_image=icon__arrow_back,
                            dark_image=icon__arrow_back,
                            size=(20, 20),
                        ),
                        command=lambda: (
                            self.if_01_container_frame_admin_sign_in.place(x=3, y=3),
                            if_backupcode_container_frame_admin_sign_in.place_forget(),
                            if_backupcode_container_frame_admin_sign_in.destroy(),
                        ),
                    )
                )
                btn__back_if_backupcode.place(x=20, y=352)

                btn__forward_if_backupcode: customtkinter.CTkButton = (
                    customtkinter.CTkButton(
                        if_backupcode_container_frame_admin_sign_in,
                        text="",
                        width=0,  # 28
                        height=0,  # 28
                        fg_color="transparent",
                        hover=False,
                        image=customtkinter.CTkImage(
                            light_image=icon__arrow_forward,
                            dark_image=icon__arrow_forward,
                            size=(20, 20),
                        ),
                        command=validate_backup_code,
                    )
                )
                btn__forward_if_backupcode.place(x=252, y=352)

            self.if_01_container_frame_admin_sign_in: customtkinter.CTkFrame = (
                customtkinter.CTkFrame(
                    self.internal_frame_00_more_actions,
                    width=300,
                    height=400,
                    fg_color="transparent",
                )
            )
            self.if_01_container_frame_admin_sign_in.place(x=3, y=3)

            customtkinter.CTkLabel(
                self.if_01_container_frame_admin_sign_in,
                text="Choose a Verification Method",
                font=("Segoe UI", 16, "bold"),
                text_color="#FFFFFF",
                image=customtkinter.CTkImage(
                    light_image=icon__lock_person,
                    dark_image=icon__lock_person,
                    size=(42, 42),
                ),
                compound="top",
                height=0,
                width=0,
            ).place(x=36, y=68)

            self.btn__email_verification_via_otp: customtkinter.CTkButton = (
                customtkinter.CTkButton(
                    self.if_01_container_frame_admin_sign_in,
                    text="""Verify administrator account ownership using the
one-time password sent to your email address.""",
                    width=260,
                    height=60,
                    border_width=0,
                    text_color="#FFFFFF",
                    bg_color="transparent",
                    fg_color="#1B1B1B",
                    font=("Roboto", 9),
                    hover_color="#252525",
                    corner_radius=6,
                    image=customtkinter.CTkImage(
                        light_image=icon__chevron_forward,
                        dark_image=icon__chevron_forward,
                        size=(30, 30),
                    ),
                    compound="right",
                    command=opted_email_verification_via_otp,
                )
            )
            self.btn__email_verification_via_otp.place(x=20, y=200)

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
                        light_image=icon__wifi_off,
                        dark_image=icon__wifi_off,
                        size=(12, 12),
                    ),
                    compound="left",
                ).place(x=58, y=46)

            self.btn__backup_code_verification: customtkinter.CTkButton = (
                customtkinter.CTkButton(
                    self.if_01_container_frame_admin_sign_in,
                    text="""Verify administrator account ownership using the
backup recovery code linked to your account.""",
                    width=260,
                    height=60,
                    border_width=0,
                    text_color="#FFFFFF",
                    bg_color="transparent",
                    fg_color="#1B1B1B",
                    font=("Roboto", 9),
                    hover_color="#252525",
                    corner_radius=6,
                    image=customtkinter.CTkImage(
                        light_image=icon__chevron_forward,
                        dark_image=icon__chevron_forward,
                        size=(30, 30),
                    ),
                    compound="right",
                    command=opted_backup_code_verification,
                )
            )
            self.btn__backup_code_verification.place(x=20, y=272)

            self.btn__back_if_01: customtkinter.CTkButton = customtkinter.CTkButton(
                self.if_01_container_frame_admin_sign_in,
                text="",
                width=0,  # 28
                height=0,  # 28
                fg_color="transparent",
                hover=False,
                image=customtkinter.CTkImage(
                    light_image=icon__arrow_back,
                    dark_image=icon__arrow_back,
                    size=(20, 20),
                ),
                command=lambda: (
                    self.if_00_container_frame_admin_sign_in.place(x=3, y=3),
                    self.if_01_container_frame_admin_sign_in.place_forget(),
                    self.if_01_container_frame_admin_sign_in.destroy(),
                ),
            )
            self.btn__back_if_01.place(x=20, y=352)

        def validate_administrator_password(self) -> None:

            admin_username: str = self.__username.get().strip()
            admin_password: str = self.__password.get().strip()

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

            if (
                not admin_username
            ) and admin_password:  # admin_username: false -- admin_password: true

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

            elif admin_username and (
                not admin_password
            ):  # admin_username: true -- admin_password: false

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

            elif (not admin_username) and (
                not admin_password
            ):  # admin_username: false -- admin_password: false

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
                # admin_username: true (not exists) -- admin_password: true [or]
                # admin_username: true (exists) -- admin_password: true (wrong)

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
                self.overlay_frame__admin_dashboard = (
                    administrator_interface.administrator(
                        self.parent_window, self._btn, admin_username
                    )
                )
                self.overlay_frame__admin_dashboard.show_frame()
                self.parent_frame.after(800, self.hide_overlay_callback)

    class more_actions:

        def __init__(
            self, parent_window: customtkinter.CTk, _btn: customtkinter.CTkButton
        ) -> None:

            self.frame__more_actions: customtkinter.CTkFrame = customtkinter.CTkFrame(
                parent_window,
                corner_radius=6,
                width=1060,
                height=610,
                fg_color="#0a0a0a",
                background_corner_colors=(
                    "#000000",
                    "#0a0a0a",
                    "#000000",
                    "#000000",
                ),  # type: ignore[arg-type]
            )

            self.show_frame: Callable = lambda: (
                self.frame__more_actions.place(x=20, y=20),
                _btn.configure(state="disabled"),
            )
            self.hide_frame: Callable = lambda: (
                self.frame__more_actions.destroy(),
                _btn.configure(state="normal"),
            )

            more_actions_interface.frame__administrator(
                self.frame__more_actions, parent_window, self.hide_frame, _btn
            )
