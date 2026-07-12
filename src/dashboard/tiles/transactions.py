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

            match _transaction[1]:

                case "deposit":

                    icon = assets.icons.material.add_circle
                    text = " Deposit"
                    sign = "+"
                    color = "#22C55E"

                case "withdraw":

                    icon = assets.icons.material.do_not_disturb_on
                    text = " Withdraw"
                    sign = "-"
                    color = "#EF4444"

                case "transfer_in":

                    icon = assets.icons.material.arrow_circle_down
                    text = " Received"
                    sign = "+"
                    color = "#22C55E"

                case "transfer_out":

                    icon = assets.icons.material.arrow_circle_up
                    text = " Sent"
                    sign = "-"
                    color = "#EF4444"

                case _:

                    icon = assets.icons.material.error
                    text = " Unknown"
                    sign = "~"
                    color = "#FFFFFF"

            customtkinter.CTkLabel(
                card,
                text=text,
                width=0,
                height=0,
                font=("Roboto", 12, "bold"),
                image=customtkinter.CTkImage(
                    light_image=icon, dark_image=icon, size=(20, 20)
                ),
                compound="left",
                text_color="#FFFFFF",
            ).place(x=5, y=5)

            customtkinter.CTkLabel(
                card,
                text=f"{sign}${_transaction[2]:,.2f}",
                width=110,
                height=20,
                font=("Roboto", 12, "bold"),
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

