from .. import customtkinter, assets


class transaction_carousel:

    def __init__(self, parent_frame: customtkinter.CTkFrame) -> None:

        self.frame__transaction_carousel: customtkinter.CTkFrame = (
            customtkinter.CTkFrame(
                parent_frame, width=190, height=110, fg_color="#1a1a1a"
            )
        )
        self.frame__transaction_carousel.place(x=5, y=515)
