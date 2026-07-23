from .. import customtkinter, Callable


class issues_and_broadcasts:

    def __init__(self, parent_frame: customtkinter.CTkFrame, username: str) -> None:

        self.frame__issues_and_broadcasts: customtkinter.CTkFrame = (
            customtkinter.CTkFrame(
                parent_frame, width=870, height=590, fg_color="#0a0a0a"
            )
        )

        self.show_frame: Callable = lambda: self.frame__issues_and_broadcasts.place(
            x=220, y=50
        )
        self.hide_frame: Callable = (
            lambda: self.frame__issues_and_broadcasts.place_forget()
        )
