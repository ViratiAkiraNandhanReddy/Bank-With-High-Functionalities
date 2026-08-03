from .._balance import balance
from .._favorites import favorites
from .._transactions import transactions
from .... import customtkinter, assets, Callable, SERVER


class transfer:

    def __init__(
        self,
        parent_frame: customtkinter.CTkFrame,
        username: str,
        balance_instance: balance,
        transactions_instance: transactions,
        favorites_instance: favorites,
    ) -> None:

        self.username = username
        self.balance_instance = balance_instance
        self.favorites_instance = favorites_instance
        self.transactions_instance = transactions_instance

        self.frame__transfer: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame,
            width=350,
            height=390,
            fg_color="#0a0a0a",
        )

        self.show_frame: Callable = lambda: self.frame__transfer.place(x=740, y=250)

        self.hide_frame: Callable = lambda: self.frame__transfer.place_forget()

        self.if_00_transfer: customtkinter.CTkFrame = customtkinter.CTkFrame(
            self.frame__transfer,
            width=350,
            height=390,
            fg_color="#0a0a0a",
            background_corner_colors=(
                "#000000",
                "#000000",
                "#000000",
                "#000000",
            ),  # type: ignore[arg-type]
        )
        self.if_00_transfer.place(x=0, y=0)

        customtkinter.CTkLabel(
            self.if_00_transfer,
            text="Transfer Funds",
            font=("Consolas", 16, "bold"),
            text_color="#FFFFFF",
            image=customtkinter.CTkImage(
                light_image=assets.icons.material.arrow_circle_up,
                dark_image=assets.icons.material.arrow_circle_up,
                size=(42, 42),
            ),
            compound="top",
            height=0,  # 61
            width=0,  # 126
        ).place(
            x=112, y=44
        )  # x = 112 ; y = 44.5

        self.container_frame__username_transfer: customtkinter.CTkFrame = (
            customtkinter.CTkFrame(
                self.if_00_transfer,
                width=280,
                height=40,
                fg_color="transparent",
                border_width=1,
                border_color="#FFFFFF",
                corner_radius=6,
            )
        )

        self.container_frame__username_label_transfer: customtkinter.CTkLabel = (
            customtkinter.CTkLabel(
                self.if_00_transfer,
                text="username",
                font=("Consolas", 10),
                height=12,
                width=44,  # 38
                text_color="#FFFFFF",
            )
        )

        customtkinter.CTkLabel(
            self.container_frame__username_transfer,
            image=customtkinter.CTkImage(
                light_image=assets.icons.material.account_circle,
                dark_image=assets.icons.material.account_circle,
                size=(20, 20),
            ),
            text="",
        ).place(x=8, rely=0.5, anchor="w")

        self.container_frame__username_transfer.place(x=35, y=150)

        self.__username: customtkinter.CTkEntry = customtkinter.CTkEntry(
            self.container_frame__username_transfer,
            placeholder_text="username",
            width=280 - 40,
            height=40 - 8,
            corner_radius=0,
            border_width=0,
            fg_color="transparent",
            font=("Consolas", 16),
        )
        self.__username.place(x=28, rely=0.5, anchor="w")

        self.__username.bind(
            "<FocusIn>",
            lambda event: (
                self.container_frame__username_label_transfer.place(x=55, y=144)
                if not self.__username.get()
                else None
            ),
        )
        self.__username.bind(
            "<FocusOut>",
            lambda event: (
                self.container_frame__username_label_transfer.place_forget()
                if not self.__username.get()
                else None
            ),
        )

        self.container_frame__username_info_transfer: customtkinter.CTkFrame = (
            customtkinter.CTkFrame(
                self.if_00_transfer,
                width=280,
                height=104,
                fg_color="transparent",
                border_width=1,
                border_color="#FFFFFF",
                corner_radius=6,
            )
        )

        self.container_frame__username_info_transfer.place(x=35, y=210)

        self.__username.bind("<Return>", lambda _event: self._validate_username())

        self.validate_username_btn: customtkinter.CTkButton = customtkinter.CTkButton(
            self.if_00_transfer,
            text="",
            width=0,  # 28
            height=0,  # 28
            fg_color="transparent",
            hover=False,
            image=customtkinter.CTkImage(
                light_image=assets.icons.material.person_search,
                dark_image=assets.icons.material.person_search,
                size=(20, 20),
            ),
            command=self._validate_username,
        )

        self.validate_username_btn.place(x=302, y=342)

        self.continue_to_if_01_transfer: customtkinter.CTkButton = (
            customtkinter.CTkButton(
                self.if_00_transfer,
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
                command=lambda: (
                    self.if_01_transfer.place(x=0, y=0),
                    self.if_00_transfer.place_forget(),
                ),
            )
        )

        self.if_01_transfer: customtkinter.CTkFrame = customtkinter.CTkFrame(
            self.frame__transfer,
            width=350,
            height=390,
            fg_color="#0a0a0a",
            background_corner_colors=(
                "#000000",
                "#000000",
                "#000000",
                "#000000",
            ),  # type: ignore[arg-type]
        )

        customtkinter.CTkLabel(
            self.if_01_transfer,
            text="Transfer To",
            font=("Consolas", 16, "bold"),
            text_color="#FFFFFF",
            height=0,  # 19
            width=0,  # 99
        ).place(
            x=125, y=24
        )  # x = 125.5 ; y = 24.5

        self.recipient_username_h1: customtkinter.CTkLabel = customtkinter.CTkLabel(
            self.if_01_transfer,
            text="",
            font=("Consolas", 18, "bold"),
            text_color="#FFFFFF",
            height=25,  # 22
            width=280,  # 280
        )

        self.recipient_username_h1.place(x=35, y=84)  # x = 35 ; y = 84

        self.container_frame__amount_transfer: customtkinter.CTkFrame = (
            customtkinter.CTkFrame(
                self.if_01_transfer,
                width=280,
                height=40,
                fg_color="transparent",
                border_width=1,
                border_color="#FFFFFF",
                corner_radius=6,
            )
        )

        self.container_frame__amount_label_transfer: customtkinter.CTkLabel = (
            customtkinter.CTkLabel(
                self.if_01_transfer,
                text="amount",
                font=("Consolas", 10),
                height=12,
                width=34,  # 28
                text_color="#FFFFFF",
            )
        )

        customtkinter.CTkLabel(
            self.container_frame__amount_transfer,
            image=customtkinter.CTkImage(
                light_image=assets.icons.material.paid,
                dark_image=assets.icons.material.paid,
                size=(20, 20),
            ),
            text="",
        ).place(x=8, rely=0.5, anchor="w")

        self.container_frame__amount_transfer.place(x=35, y=150)

        self.__amount: customtkinter.CTkEntry = customtkinter.CTkEntry(
            self.container_frame__amount_transfer,
            placeholder_text="amount",
            width=280 - 40,
            height=40 - 8,
            corner_radius=0,
            border_width=0,
            fg_color="transparent",
            font=("Consolas", 16),
        )
        self.__amount.place(x=28, rely=0.5, anchor="w")

        self.__amount.bind(
            "<FocusIn>",
            lambda event: (
                self.container_frame__amount_label_transfer.place(x=55, y=144)
                if not self.__amount.get()
                else None
            ),
        )
        self.__amount.bind(
            "<FocusOut>",
            lambda event: (
                self.container_frame__amount_label_transfer.place_forget()
                if not self.__amount.get()
                else None
            ),
        )

        self.container_frame__password_transfer: customtkinter.CTkFrame = (
            customtkinter.CTkFrame(
                self.if_01_transfer,
                width=280,
                height=40,
                fg_color="transparent",
                border_width=1,
                border_color="#FFFFFF",
                corner_radius=6,
            )
        )

        self.container_frame__password_label_transfer: customtkinter.CTkLabel = (
            customtkinter.CTkLabel(
                self.if_01_transfer,
                text="password",
                font=("Consolas", 10),
                height=12,
                width=44,  # 38
                text_color="#FFFFFF",
            )
        )

        customtkinter.CTkLabel(
            self.container_frame__password_transfer,
            image=customtkinter.CTkImage(
                light_image=assets.icons.material.password,
                dark_image=assets.icons.material.password,
                size=(20, 20),
            ),
            text="",
        ).place(x=8, rely=0.5, anchor="w")

        self.container_frame__password_transfer.place(x=35, y=210)

        self.__password: customtkinter.CTkEntry = customtkinter.CTkEntry(
            self.container_frame__password_transfer,
            placeholder_text="password",
            width=280 - 40,
            height=40 - 8,
            corner_radius=0,
            border_width=0,
            fg_color="transparent",
            font=("Consolas", 16),
        )
        self.__password.place(x=28, rely=0.5, anchor="w")

        self.__password.bind(
            "<FocusIn>",
            lambda event: (
                self.container_frame__password_label_transfer.place(x=55, y=204)
                if not self.__password.get()
                else None
            ),
        )
        self.__password.bind(
            "<FocusOut>",
            lambda event: (
                self.container_frame__password_label_transfer.place_forget()
                if not self.__password.get()
                else None
            ),
        )

        self.message_label = customtkinter.CTkLabel(
            self.if_01_transfer,
            text="",
            width=280,
            height=65,
            wraplength=270,
            font=("Consolas", 12),
            text_color="#22C55E",
        )
        self.message_label.place(x=35, y=250)

        self.__amount.bind("<Return>", lambda _event: self.handle_transfer())
        self.__password.bind("<Return>", lambda _event: self.handle_transfer())

        self.back_to_if_00_transfer: customtkinter.CTkButton = customtkinter.CTkButton(
            self.if_01_transfer,
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
                self.if_00_transfer.place(x=0, y=0),
                self.if_01_transfer.place_forget(),
            ),
        )
        self.back_to_if_00_transfer.place(x=20, y=20)

        transfer_btn: customtkinter.CTkButton = customtkinter.CTkButton(
            self.if_01_transfer,
            text="Transfer",
            width=280,
            height=40,
            border_width=0,
            text_color="#FFFFFF",
            bg_color="transparent",
            fg_color="#3B82F6",
            font=("Consolas", 16, "bold"),
            hover_color="#2563EB",
            corner_radius=6,
            command=self.handle_transfer,
        )
        transfer_btn.place(x=35, y=315)

    def handle_transfer(self) -> None:

        amount_string: str = self.__amount.get().strip()
        user_password: str = self.__password.get().strip()

        self.__amount.bind(
            "<KeyPress>",
            lambda event: self.container_frame__amount_transfer.configure(
                border_color="#FFFFFF"
            )
            or self.container_frame__amount_label_transfer.configure(
                text_color="#FFFFFF"
            )
            or self.container_frame__amount_label_transfer.configure(
                text="amount",
                width=34,  # 28
            )
            or self.message_label.configure(text="", text_color="#22C55E")
            or self.__amount.unbind("<KeyPress>"),
        )
        self.__password.bind(
            "<KeyPress>",
            lambda event: self.container_frame__password_transfer.configure(
                border_color="#FFFFFF"
            )
            or self.container_frame__password_label_transfer.configure(
                text_color="#FFFFFF"
            )
            or self.container_frame__password_label_transfer.configure(
                text="password",
                width=44,  # 38
            )
            or self.message_label.configure(text="", text_color="#22C55E")
            or self.__password.unbind("<KeyPress>"),
        )

        if (not amount_string) and (
            not user_password
        ):  # amount_string: false -- user_password: false

            self.container_frame__amount_transfer.configure(border_color="#FF0000")
            self.container_frame__password_transfer.configure(border_color="#FF0000")
            self.container_frame__amount_label_transfer.configure(
                text="invalid amount", width=73
            )

            self.container_frame__amount_label_transfer.configure(text_color="#FF0000")
            self.container_frame__password_label_transfer.configure(
                text_color="#FF0000"
            )
            self.container_frame__password_label_transfer.configure(
                text="invalid password", width=83
            )

            return

        if not user_password:

            self.container_frame__password_transfer.configure(border_color="#FF0000")
            self.container_frame__password_label_transfer.configure(
                text_color="#FF0000"
            )
            self.container_frame__password_label_transfer.configure(
                text="invalid password", width=83
            )

            return

        try:

            amount_float: float = round(float(amount_string), 2)

        except ValueError:

            self.container_frame__amount_transfer.configure(border_color="#FF0000")
            self.container_frame__amount_label_transfer.configure(text_color="#FF0000")
            self.container_frame__amount_label_transfer.configure(
                text="invalid amount", width=73
            )

            return

        if amount_float <= 0:

            self.container_frame__amount_transfer.configure(border_color="#FF0000")
            self.container_frame__amount_label_transfer.configure(text_color="#FF0000")
            self.container_frame__amount_label_transfer.configure(
                text="invalid amount", width=73
            )

            self.message_label.configure(
                text="Amount must be greater than $0", text_color="#FF0000"
            )

            return

        if amount_float > 99999.99:

            self.container_frame__amount_transfer.configure(border_color="#FF0000")
            self.container_frame__amount_label_transfer.configure(text_color="#FF0000")
            self.container_frame__amount_label_transfer.configure(
                text="invalid amount", width=73
            )

            self.message_label.configure(
                text="Maximum Transfer: $99,999.99", text_color="#FF0000"
            )

            return

        if not SERVER.authentication.user.password(self.username, user_password):

            self.container_frame__password_transfer.configure(border_color="#FF0000")
            self.container_frame__password_label_transfer.configure(
                text_color="#FF0000"
            )
            self.container_frame__password_label_transfer.configure(
                text="invalid password", width=83
            )

            self.message_label.configure(
                text="Incorrect password", text_color="#FF0000"
            )

            return

        if SERVER.lookup.user.balance(self.username) < amount_float:

            self.container_frame__amount_transfer.configure(border_color="#FF0000")
            self.container_frame__amount_label_transfer.configure(text_color="#FF0000")
            self.container_frame__amount_label_transfer.configure(
                text="invalid amount", width=73
            )

            self.message_label.configure(
                text="Insufficient available balance.", text_color="#FF0000"
            )

            return

        server_response: bool = SERVER.management.user.transfer(
            self.username, self.recipient_username, amount_float
        )

        if server_response:

            self.__amount.delete(0, "end")
            self.__password.delete(0, "end")
            self.balance_instance.refresh()
            self.favorites_instance.refresh()
            self.transactions_instance.refresh()

            self.message_label.configure(text="Transfer successful!")
            self.message_label.after(
                3000, lambda: self.message_label.configure(text="")
            )

        else:

            self.message_label.configure(
                text="Transfer failed. Please try again.",
                text_color="#FF0000",
            )
            self.message_label.after(
                3000, lambda: self.message_label.configure(text="")
            )

    def _validate_username(self) -> None:

        self.recipient_username = self.__username.get().strip()

        self.__username.bind(
            "<KeyPress>",
            lambda event: self.container_frame__username_transfer.configure(
                border_color="#FFFFFF"
            )
            or self.container_frame__username_label_transfer.configure(
                text_color="#FFFFFF",
                width=34,  # 28
                text="amount",
            )
            or self.validate_username_btn.place(x=302, y=342)
            or self.continue_to_if_01_transfer.place_forget()
            or self.__amount.unbind("<KeyPress>"),
        )

        if not self.recipient_username:

            self.container_frame__username_transfer.configure(border_color="#FF0000")
            self.container_frame__username_label_transfer.configure(
                text="invalid username",
                text_color="#FF0000",
                width=83,
            )

            return

        if not SERVER.lookup.user.exists(self.recipient_username):

            self.container_frame__username_transfer.configure(border_color="#FF0000")
            self.container_frame__username_label_transfer.configure(
                text="invalid username",
                text_color="#FF0000",
                width=83,
            )

            return

        if self.recipient_username == self.username:

            self.container_frame__username_transfer.configure(border_color="#FF0000")
            self.container_frame__username_label_transfer.configure(
                text="invalid username",
                text_color="#FF0000",
                width=83,
            )

            return

        self.recipient_username_h1.configure(
            text="@"
            + (
                self.recipient_username
                if len(self.recipient_username) <= 23
                else self.recipient_username[:20] + "..."
            )
        )
        self.validate_username_btn.place_forget()
        self.continue_to_if_01_transfer.place(x=302, y=342)
