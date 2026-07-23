from .deposit import deposit
from ..balance import balance
from .withdraw import withdraw
from .transfer import transfer
from .... import customtkinter
from ..favorites import favorites
from ..transactions import transactions


class actions:

    def __init__(self, parent_frame: customtkinter.CTkFrame, username: str) -> None:

        self.balance = balance(parent_frame, username)
        self.favorites = favorites(parent_frame, username)
        self.transactions = transactions(parent_frame, username)

        self.frame__actions: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame, width=350, height=40, fg_color="#0a0a0a"
        )
        self.frame__actions.place(x=740, y=200)

        self.frame__action_view: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame, width=350, height=390, fg_color="#0a0a0a"
        )
        self.frame__action_view.place(x=740, y=250)

        self.deposit: deposit = deposit(
            self.frame__action_view, self.balance, self.transactions
        )

        self.withdraw: withdraw = withdraw(
            self.frame__action_view, self.balance, self.transactions
        )

        self.transfer: transfer = transfer(
            self.frame__action_view, self.balance, self.transactions
        )

        self.action_selector_variable = customtkinter.StringVar(value="Deposit")

        self.action_selector = customtkinter.CTkSegmentedButton(
            self.frame__actions,
            height=30,
            width=340,
            fg_color="#0a0a0a",
            text_color="#FFFFFF",
            values=["Deposit", "Withdraw", "Transfer"],
            variable=self.action_selector_variable,
            dynamic_resizing=False,
            unselected_color="#131313",
            unselected_hover_color="#1D1D1D",
            selected_color="#1D1D1D",
            selected_hover_color="#1D1D1D",
        )
        self.action_selector.place(x=5, y=5)
