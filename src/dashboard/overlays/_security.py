from ... import customtkinter, Callable


class security_overlay:

    def __init__(self, parent_frame: customtkinter.CTkFrame, username: str) -> None:

        self.frame__security: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame, width=1080, height=590, fg_color="#0a0a0a"
        )

        self.show_frame: Callable = lambda: (
            self.refresh(),
            self.frame__security.place(x=10, y=50),
        )
        self.hide_frame: Callable = lambda: self.frame__security.place_forget()

    def refresh(self) -> None:

        pass
