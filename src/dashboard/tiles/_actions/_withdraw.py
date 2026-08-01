from .._balance import balance
from .._transactions import transactions
from .... import customtkinter, assets, Callable, SERVER


class withdraw:

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

        self.frame__withdraw: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame,
            width=350,
            height=390,
            fg_color="#0a0a0a",
        )

        self.show_frame: Callable = lambda: self.frame__withdraw.place(x=740, y=250)

        self.hide_frame: Callable = lambda: self.frame__withdraw.place_forget()

        customtkinter.CTkLabel(
            self.frame__withdraw,
            text="Withdraw Funds",
            font=("Consolas", 16, "bold"),
            text_color="#FFFFFF",
            image=customtkinter.CTkImage(
                light_image=assets.icons.material.do_not_disturb_on,
                dark_image=assets.icons.material.do_not_disturb_on,
                size=(42, 42),
            ),
            compound="top",
            height=0,  # 61
            width=0,  # 126
        ).place(
            x=112, y=44
        )  # x = 112 ; y = 44.5
