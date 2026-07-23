from .._balance import balance
from .._transactions import transactions
from .... import customtkinter, assets, Callable, SERVER


class deposit:

    def __init__(
        self,
        parent_frame: customtkinter.CTkFrame,
        balance_instance: balance,
        transactions_instance: transactions,
    ) -> None:

        self.frame__deposit: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame,
            width=350,
            height=390,
            fg_color="#0a0a0a",
        )

        self.show_frame: Callable = lambda: self.frame__deposit.place(x=740, y=250)

        self.hide_frame: Callable = lambda: self.frame__deposit.place_forget()
