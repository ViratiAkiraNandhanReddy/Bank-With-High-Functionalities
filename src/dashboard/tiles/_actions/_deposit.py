from .._balance import balance
from .._transactions import transactions
from .... import customtkinter, assets, Callable, SERVER


class deposit:

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

        self.frame__deposit: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame,
            width=350,
            height=390,
            fg_color="#0a0a0a",
        )

        self.show_frame: Callable = lambda: self.frame__deposit.place(x=740, y=250)

        self.hide_frame: Callable = lambda: self.frame__deposit.place_forget()

        customtkinter.CTkLabel(
            self.frame__deposit,
            text="Deposit Funds",
            font=("Consolas", 16, "bold"),
            text_color="#FFFFFF",
            image=customtkinter.CTkImage(
                light_image=assets.icons.material.add_circle,
                dark_image=assets.icons.material.add_circle,
                size=(42, 42),
            ),
            compound="top",
            height=0,  # 61
            width=0,  # 117
        ).place(
            x=117, y=44
        )  # x = 116.5 ; y = 44.5

        self.container_frame__amount_deposit: customtkinter.CTkFrame = (
            customtkinter.CTkFrame(
                self.frame__deposit,
                width=280,
                height=40,
                fg_color="transparent",
                border_width=1,
                border_color="#FFFFFF",
                corner_radius=6,
            )
        )

        self.container_frame__amount_label_deposit: customtkinter.CTkLabel = (
            customtkinter.CTkLabel(
                self.frame__deposit,
                text="amount",
                font=("Consolas", 10),
                height=12,
                width=34,  # 28
                text_color="#FFFFFF",
            )
        )

        customtkinter.CTkLabel(
            self.container_frame__amount_deposit,
            image=customtkinter.CTkImage(
                light_image=assets.icons.material.account_circle,
                dark_image=assets.icons.material.account_circle,
                size=(20, 20),
            ),
            text="",
        ).place(x=8, rely=0.5, anchor="w")

        self.container_frame__amount_deposit.place(x=35, y=150)

        self.__amount: customtkinter.CTkEntry = customtkinter.CTkEntry(
            self.container_frame__amount_deposit,
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
                self.container_frame__amount_label_deposit.place(x=55, y=144)
                if not self.__amount.get()
                else None
            ),
        )
        self.__amount.bind(
            "<FocusOut>",
            lambda event: (
                self.container_frame__amount_label_deposit.place_forget()
                if not self.__amount.get()
                else None
            ),
        )

        self.container_frame__password_deposit: customtkinter.CTkFrame = (
            customtkinter.CTkFrame(
                self.frame__deposit,
                width=280,
                height=40,
                fg_color="transparent",
                border_width=1,
                border_color="#FFFFFF",
                corner_radius=6,
            )
        )

        self.container_frame__password_label_deposit: customtkinter.CTkLabel = (
            customtkinter.CTkLabel(
                self.frame__deposit,
                text="password",
                font=("Consolas", 10),
                height=12,
                width=44,  # 38
                text_color="#FFFFFF",
            )
        )

        customtkinter.CTkLabel(
            self.container_frame__password_deposit,
            image=customtkinter.CTkImage(
                light_image=assets.icons.material.password,
                dark_image=assets.icons.material.password,
                size=(20, 20),
            ),
            text="",
        ).place(x=8, rely=0.5, anchor="w")

        self.container_frame__password_deposit.place(x=35, y=210)

        self.__password: customtkinter.CTkEntry = customtkinter.CTkEntry(
            self.container_frame__password_deposit,
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
                self.container_frame__password_label_deposit.place(x=55, y=204)
                if not self.__password.get()
                else None
            ),
        )
        self.__password.bind(
            "<FocusOut>",
            lambda event: (
                self.container_frame__password_label_deposit.place_forget()
                if not self.__password.get()
                else None
            ),
        )

        self.message_label = customtkinter.CTkLabel(
            self.frame__deposit,
            text="",
            width=280,
            height=65,
            wraplength=270,
            font=("Consolas", 12),
            text_color="#22C55E",
        )
        self.message_label.place(x=35, y=250)

        self.__amount.bind("<Return>", lambda _event: self.handle_deposit())
        self.__password.bind("<Return>", lambda _event: self.handle_deposit())

        deposit_btn: customtkinter.CTkButton = customtkinter.CTkButton(
            self.frame__deposit,
            text="Deposit",
            width=280,
            height=40,
            border_width=0,
            text_color="#000000",
            bg_color="transparent",
            fg_color="#22C55E",
            font=("Consolas", 16, "bold"),
            hover_color="#16A34A",
            corner_radius=6,
            command=self.handle_deposit,
        )
        deposit_btn.place(x=35, y=315)

    def handle_deposit(self) -> None:

        amount_string: str = self.__amount.get().strip()
        user_password: str = self.__password.get().strip()

        self.__amount.bind(
            "<KeyPress>",
            lambda event: self.container_frame__amount_deposit.configure(
                border_color="#FFFFFF"
            )
            or self.container_frame__amount_label_deposit.configure(
                text_color="#FFFFFF"
            )
            or self.container_frame__amount_label_deposit.configure(
                text="amount",
                width=34,  # 28
            )
            or self.message_label.configure(text="", text_color="#22C55E")
            or self.__amount.unbind("<KeyPress>"),
        )
        self.__password.bind(
            "<KeyPress>",
            lambda event: self.container_frame__password_deposit.configure(
                border_color="#FFFFFF"
            )
            or self.container_frame__password_label_deposit.configure(
                text_color="#FFFFFF"
            )
            or self.container_frame__password_label_deposit.configure(
                text="password",
                width=44,  # 38
            )
            or self.message_label.configure(text="", text_color="#22C55E")
            or self.__password.unbind("<KeyPress>"),
        )
