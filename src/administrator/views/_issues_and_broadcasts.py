lazy from ... import SERVER, Callable, customtkinter, ui


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

        ui.section_title(
            self.frame__issues_and_broadcasts,
            "Issues & broadcasts",
            x=35,
            y=30,
        )

        customtkinter.CTkLabel(
            self.frame__issues_and_broadcasts,
            text="Publish a dashboard announcement",
            font=("Segoe UI", 16, "bold"),
        ).place(x=35, y=95)

        announcement_entry = customtkinter.CTkTextbox(
            self.frame__issues_and_broadcasts,
            width=760,
            height=145,
            font=("Segoe UI", 14),
        )
        announcement_entry.insert(
            "1.0", SERVER.lookup.application.current_announcement()
        )
        announcement_entry.place(x=35, y=130)

        customtkinter.CTkLabel(
            self.frame__issues_and_broadcasts,
            text="This message is shown to users on their dashboard.",
            font=("Segoe UI", 12),
            text_color="#A3A3A3",
        ).place(x=35, y=285)

        status_label = customtkinter.CTkLabel(
            self.frame__issues_and_broadcasts,
            text="",
            font=("Segoe UI", 13),
        )
        status_label.place(x=35, y=340)

        def update_announcement() -> None:
            content = announcement_entry.get("1.0", "end").strip()
            if not content:
                status_label.configure(
                    text="Announcement cannot be empty.",
                    text_color="#FF0000",
                )
                return
            if SERVER.management.application.update_announcement(content):
                status_label.configure(
                    text="Announcement updated.",
                    text_color="#22C55E",
                )
            else:
                status_label.configure(
                    text="Announcement update failed.",
                    text_color="#FF0000",
                )

        customtkinter.CTkButton(
            self.frame__issues_and_broadcasts,
            text="Publish announcement",
            width=240,
            height=42,
            command=update_announcement,
        ).place(x=35, y=375)
