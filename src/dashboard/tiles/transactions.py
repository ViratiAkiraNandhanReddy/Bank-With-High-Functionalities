from ... import customtkinter


class transactions:

    def __init__(self, parent_frame: customtkinter.CTkFrame, username: str) -> None:

        self.frame__transactions: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame, width=210, height=440, fg_color="#0a0a0a"
        )
        self.frame__transactions.place(x=520, y=200)
