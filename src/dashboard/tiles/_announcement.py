from ... import customtkinter, SERVER


class announcement:

    def __init__(self, parent_frame: customtkinter.CTkFrame) -> None:

        self.frame__announcement: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame, width=570, height=140, fg_color="#0a0a0a"
        )
        self.frame__announcement.place(x=520, y=50)

        self.announcement_content: str = (
            SERVER.lookup.application.current_announcement()
        )

        if self.announcement_content == "No new announcements.":

            justify: str = "center"
            anchor: str = "center"

        else:

            justify: str = "left"
            anchor: str = "nw"

        self.label__announcement: customtkinter.CTkLabel = customtkinter.CTkLabel(
            self.frame__announcement,
            text=self.announcement_content,
            width=550,
            height=126,
            wraplength=550,
            justify=justify,
            anchor=anchor,
            font=("Consolas", 13),
        )
        self.label__announcement.place(x=10, y=7)
