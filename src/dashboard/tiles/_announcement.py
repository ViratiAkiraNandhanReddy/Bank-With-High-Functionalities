lazy from ... import SERVER, customtkinter, ui


class announcement:

    def __init__(self, parent_frame: customtkinter.CTkFrame) -> None:

        self.frame__announcement: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame,
            width=570,
            height=140,
            fg_color=ui.COLORS["card"],
            border_width=1,
            border_color="#252525",
            corner_radius=8,
        )
        self.frame__announcement.place(x=520, y=50)

        customtkinter.CTkLabel(
            self.frame__announcement,
            text="Latest announcement",
            font=("Segoe UI", 12, "bold"),
            text_color="#218CFF",
        ).place(x=12, y=7)

        customtkinter.CTkFrame(
            self.frame__announcement,
            width=4,
            height=92,
            fg_color="#218CFF",
            corner_radius=2,
        ).place(x=12, y=34)

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
            width=530,
            height=100,
            wraplength=530,
            justify=justify,
            anchor=anchor,
            font=("Consolas", 13),
        )
        self.label__announcement.place(x=24, y=31)
