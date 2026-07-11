from ... import customtkinter, SERVER, assets


class balance:

    def __init__(self, parent_frame: customtkinter.CTkFrame, username: str) -> None:

        self.username = username

        self.frame__balance: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame, width=440, height=50, fg_color="#0a0a0a"
        )
        self.frame__balance.place(x=10, y=50)

        self.frame__balance_trend: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame, width=50, height=50, fg_color="#0a0a0a"
        )
        self.frame__balance_trend.place(x=460, y=50)

        self.balance_trend_icon: customtkinter.CTkLabel = customtkinter.CTkLabel(
            self.frame__balance_trend,
            text="",
            width=36,
            height=36,
        )
        self.balance_trend_icon.place(x=7, y=7)

        self.set_balance_trend_icon()

        self.label__balance: customtkinter.CTkLabel = customtkinter.CTkLabel(
            self.frame__balance,
            text=f"$ {SERVER.lookup.user.balance(self.username):,.2f}",
            width=420,
            height=50,
            text_color="#FFFFFF",
            font=("Roboto", 18),
        )
        self.label__balance.place(x=10, y=0)

    def refresh(self) -> None:

        self.label__balance.configure(
            text=f"$ {SERVER.lookup.user.balance(self.username):,.2f}"
        )

        self.set_balance_trend_icon()

    def set_balance_trend_icon(self) -> None:

        transactions = SERVER.lookup.user.transactions(self.username, limit=1)

        last_transaction = transactions[0] if transactions else None

        if not last_transaction:

            icon = assets.icons.material.remove

        elif last_transaction[0] in ("deposit", "transfer_in"):

            icon = assets.icons.material.trending_up

        else:

            icon = assets.icons.material.trending_down

        self.balance_trend_icon.configure(
            image=customtkinter.CTkImage(
                light_image=icon,
                dark_image=icon,
                size=(30, 30),
            )
        )
