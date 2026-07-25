from ... import customtkinter


class security:

    def __init__(self, parent_frame: customtkinter.CTkFrame, username: str) -> None:

        self.frame__security: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame, width=245, height=220, fg_color="#0a0a0a"
        )
        self.frame__security.place(x=265, y=420)
