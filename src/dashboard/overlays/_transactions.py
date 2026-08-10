from datetime import datetime, timezone
from ... import customtkinter, Callable, SERVER


class transactions_overlay:

    def __init__(self, parent_frame: customtkinter.CTkFrame, username: str) -> None:

        self.username = username

        self.frame__transactions: customtkinter.CTkScrollableFrame = (
            customtkinter.CTkScrollableFrame(
                parent_frame, width=1058, height=578, fg_color="#0a0a0a"
            )
        )

        self.show_frame: Callable = lambda: (
            self.refresh(),
            self.frame__transactions.place(x=10, y=50),
        )
        self.hide_frame: Callable = lambda: self.frame__transactions.place_forget()

        self.load_transactions_cards()

    def load_transactions_cards(self) -> None:

        total_transactions = SERVER.lookup.user.transactions(self.username, -1)

        for n, _transaction in enumerate(total_transactions):

            card = customtkinter.CTkFrame(
                self.frame__transactions, width=200, height=82, fg_color="#111111"
            )
            card.place(x=5, y=(5 + n * (82 + 5)))

            match _transaction[1]:

                case "deposit":

                    text = "Deposit"
                    sign = "+"
                    color = "#22C55E"

                case "withdraw":

                    text = "Withdraw"
                    sign = "-"
                    color = "#EF4444"

                case "transfer_in":

                    text = "Received"
                    sign = "+"
                    color = "#22C55E"

                case "transfer_out":

                    text = "Sent"
                    sign = "-"
                    color = "#EF4444"

                case _:

                    text = "Unknown"
                    sign = "~"
                    color = "#FFFFFF"

            customtkinter.CTkLabel(
                card,
                text=text,
                width=0,
                height=20,
                font=("Consolas", 12, "bold"),
                text_color="#FFFFFF",
            ).place(x=10, y=5)

            customtkinter.CTkLabel(
                card,
                text=f"{sign}${_transaction[2]:,.2f}",
                width=105,
                height=20,
                font=("Consolas", 12, "bold"),
                text_color=color,
                anchor="e",
            ).place(x=85, y=5)

            customtkinter.CTkLabel(
                card,
                text=(
                    _transaction[0]
                    if len(_transaction[0]) < 29
                    else _transaction[0][:26] + "..."
                ),
                width=200,
                height=20,
                font=("Consolas", 11),
                text_color="#D4D4D4",
            ).place(x=0, y=31)

            customtkinter.CTkLabel(
                card,
                text=(
                    datetime.fromisoformat(_transaction[3])
                    .replace(tzinfo=timezone.utc)
                    .astimezone()
                    .strftime("%Y-%m-%d %I:%M:%S %p (%z)")
                ),  # %Y-%m-%d %I:%M:%S %p (%z)
                width=200,
                height=20,
                font=("Consolas", 11),
                text_color="#A3A3A3",
            ).place(x=0, y=57)

    def refresh(self) -> None:

        pass
