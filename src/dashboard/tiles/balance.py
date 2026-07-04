from ... import customtkinter


class balance:

    def __init__(self, parent_frame: customtkinter.CTkFrame) -> None:

        self.frame__balance: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame, width=500, height=50, fg_color="#0a0a0a"
        )
        self.frame__balance.place(x=10, y=50)
