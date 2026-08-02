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
