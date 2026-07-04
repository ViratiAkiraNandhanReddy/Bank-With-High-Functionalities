from ... import customtkinter


class messages:

    def __init__(self, parent_frame: customtkinter.CTkFrame, username: str) -> None:

        self.frame__messages: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame, width=570, height=140, fg_color="#0a0a0a"
        )
        self.frame__messages.place(x=520, y=50)
