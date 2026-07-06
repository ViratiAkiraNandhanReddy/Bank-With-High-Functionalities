from ... import customtkinter, SERVER


class balance:

    def __init__(self, parent_frame: customtkinter.CTkFrame, username: str) -> None:

        self.frame__balance: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame, width=500, height=50, fg_color="#0a0a0a"
        )
        self.frame__balance.place(x=10, y=50)

        self.label__balance: customtkinter.CTkLabel = customtkinter.CTkLabel(
            self.frame__balance,
            text=f"$ {SERVER.lookup.user.balance(username):,.2f}",
            width=480,
            height=50,
            text_color="#FFFFFF",
            font=("Roboto", 18),
        )
        self.label__balance.place(x=10, y=0)

        self.refresh = lambda: self.label__balance.configure(
            text=f"$ {SERVER.lookup.user.balance(username):,.2f}"
        )
