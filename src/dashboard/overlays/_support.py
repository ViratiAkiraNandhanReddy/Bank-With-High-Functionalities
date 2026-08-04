from ... import customtkinter, Callable


class support_overlay:

    def __init__(self, parent_frame: customtkinter.CTkFrame, username: str) -> None:

        self.frame__support: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame, width=1080, height=590, fg_color="#0a0a0a"
        )

        self.show_frame: Callable = lambda: self.frame__support.place(x=10, y=50)
        self.hide_frame: Callable = lambda: self.frame__support.place_forget()
