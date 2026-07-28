from ... import customtkinter


class notice:

    def __init__(self, parent_frame: customtkinter.CTkFrame, username: str) -> None:

        self.frame__notice: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame, width=570, height=140, fg_color="#0a0a0a"
        )
        self.frame__notice.place(x=520, y=50)
