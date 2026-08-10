from ... import customtkinter, Callable


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

    def refresh(self) -> None:

        pass
