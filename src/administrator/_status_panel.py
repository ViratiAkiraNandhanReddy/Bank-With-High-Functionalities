from .. import customtkinter


class status_panel:

    def __init__(self, parent_frame: customtkinter.CTkFrame) -> None:

        self.frame__status_panel: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame, width=830, height=30, fg_color="#0a0a0a"
        )
        self.frame__status_panel.place(x=220, y=10)
