from .._balance import balance
from .._transactions import transactions
from .... import customtkinter, assets, Callable, SERVER


class transfer:

    def __init__(
        self,
        parent_frame: customtkinter.CTkFrame,
        username: str,
        balance_instance: balance,
        transactions_instance: transactions,
    ) -> None:

        self.balance_instance = balance_instance
        self.transactions_instance = transactions_instance
        self.username = username

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
                command=self.redirect_to_if_01_transfer,
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

    def _validate_username(self) -> None:

        pass

    def redirect_to_if_01_transfer(self) -> None:

        pass
