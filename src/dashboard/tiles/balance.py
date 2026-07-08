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

        last_transaction = SERVER.lookup.user.last_transaction(self.username)

        if last_transaction is None:

            self.balance_trend_icon.configure(
                image=customtkinter.CTkImage(
                    light_image=assets.icons.material.remove,
                    dark_image=assets.icons.material.remove,
                    size=(30, 30),
                )
            )

        elif last_transaction[0] in ("deposit", "transfer_in"):

            self.balance_trend_icon.configure(
                image=customtkinter.CTkImage(
                    light_image=assets.icons.material.trending_up,
                    dark_image=assets.icons.material.trending_up,
                    size=(30, 30),
                )
            )

        else:

            self.balance_trend_icon.configure(
                image=customtkinter.CTkImage(
                    light_image=assets.icons.material.trending_down,
                    dark_image=assets.icons.material.trending_down,
                    size=(30, 30),
                )
            )
