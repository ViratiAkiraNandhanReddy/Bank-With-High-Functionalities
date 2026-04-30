from .. import customtkinter


class navigation:

    def __init__(self, parent_frame) -> None:

        self.frame__navigation: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame, width=200, height=630, fg_color="#0a0a0a"
        )
        self.frame__navigation.place(x=10, y=10)
