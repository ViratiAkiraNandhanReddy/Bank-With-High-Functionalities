from ... import customtkinter


class account_info:

    def __init__(self, parent_frame: customtkinter.CTkFrame, username: str) -> None:

        self.frame__account_info: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame, width=500, height=300, fg_color="#0a0a0a"
        )
        self.frame__account_info.place(x=10, y=110)
