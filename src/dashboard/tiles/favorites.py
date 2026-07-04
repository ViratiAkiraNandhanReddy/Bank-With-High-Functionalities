from ... import customtkinter


class favorites:

    def __init__(self, parent_frame: customtkinter.CTkFrame, username: str) -> None:

        self.frame__favorites: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame, width=245, height=220, fg_color="#0a0a0a"
        )
        self.frame__favorites.place(x=10, y=420)
