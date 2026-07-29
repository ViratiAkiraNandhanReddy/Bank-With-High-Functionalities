from ... import customtkinter, SERVER


class notice:

    def __init__(self, parent_frame: customtkinter.CTkFrame, username: str) -> None:

        self.frame__notice: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame, width=570, height=140, fg_color="#0a0a0a"
        )
        self.frame__notice.place(x=520, y=50)

        self.notice_content: str = SERVER.lookup.application.current_notice()

        self.label__notice: customtkinter.CTkLabel = customtkinter.CTkLabel(
            self.frame__notice,
            text=self.notice_content,
            width=550,
            wraplength=540,
            justify="left",
            anchor="nw",
        )
        self.label__notice.place(x=10, y=10)

