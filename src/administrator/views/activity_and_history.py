from .. import customtkinter, Callable


class activity_and_history:

    def __init__(self, parent_frame: customtkinter.CTkFrame) -> None:

        self.frame__activity_and_history: customtkinter.CTkFrame = (
            customtkinter.CTkFrame(
                parent_frame, width=870, height=590, fg_color="#0a0a0a"
            )
        )

        self.show_frame: Callable = lambda: self.frame__activity_and_history.place(
            x=220, y=50
        )
        self.hide_frame: Callable = (
            lambda: self.frame__activity_and_history.place_forget()
        )
