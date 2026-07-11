from ... import customtkinter, SERVER, assets


class transactions:

    def __init__(self, parent_frame: customtkinter.CTkFrame, username: str) -> None:

        self.username = username

        self.frame__transactions: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame, width=210, height=440, fg_color="#0a0a0a"
        )
        self.frame__transactions.place(x=520, y=200)

        self.load_transactions_cards()

    def load_transactions_cards(self) -> None:

        recent_transactions = SERVER.lookup.user.transactions(self.username)

        for n, _transaction in enumerate(recent_transactions):

            card = customtkinter.CTkFrame(
                self.frame__transactions, width=200, height=82, fg_color="#111111"
            )
            card.place(x=5, y=(5 + n * (82 + 5)))
