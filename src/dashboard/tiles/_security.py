from ... import customtkinter, SERVER
from datetime import datetime, timezone

EVENT_LABELS: dict[str, tuple[str, str]] = {
    "login": (
        "Logged in",
        "[INFO]",
    ),
    "failed_login": (
        "Failed login",
        "[MEDIUM]",
    ),
    "logout": (
        "Logged out",
        "[INFO]",
    ),
}


class security:

    def __init__(self, parent_frame: customtkinter.CTkFrame, username: str) -> None:

        self.username: str = username

        self.frame__security: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame, width=245, height=220, fg_color="#0a0a0a"
        )
        self.frame__security.place(x=265, y=420)

        self.load_security_cards()

    def load_security_cards(self) -> None:

        recent_security_events: list[tuple[str, str]] = (
            SERVER.lookup.security_event.recent(self.username)
        )

        for n, (event_type, timestamp) in enumerate(recent_security_events):

            get_event_labels = EVENT_LABELS.get(event_type, ("Unknown", "[INFO]"))

            card = customtkinter.CTkFrame(
                self.frame__security,
                width=235,
                height=38,
                fg_color="#111111",
            )
            card.place(x=5, y=(5 + n * (38 + 5)))

            customtkinter.CTkLabel(
                card,
                text=get_event_labels[0],
                width=153,
                height=24,
                font=("Consolas", 12, "bold"),
                text_color="#D4D4D4",
                anchor="w",
            ).place(x=6, y=0)

            customtkinter.CTkLabel(
                card,
                text=get_event_labels[1],
                width=70,
                height=24,
                font=("Consolas", 12, "bold"),
                text_color="#D4D4D4",
                anchor="e",
            ).place(x=159, y=0)

            customtkinter.CTkLabel(
                card,
                text=(
                    datetime.fromisoformat(timestamp)
                    .replace(tzinfo=timezone.utc)
                    .astimezone()
                    .strftime("%Y-%m-%d %I:%M:%S %p (%z)")
                ),  # %Y-%m-%d %I:%M:%S %p (%z)
                width=227,
                height=0,  # 12
                font=("Consolas", 10),
                text_color="#A3A3A3",
            ).place(x=4, y=24)

    def refresh(self) -> None:

        widget: customtkinter.CTkFrame

        for widget in self.frame__security.winfo_children():

            widget.destroy()

        self.load_security_cards()
