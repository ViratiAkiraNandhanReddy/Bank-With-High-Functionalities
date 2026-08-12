from datetime import datetime, timezone
from ... import customtkinter, Callable, SERVER

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


class security_overlay:

    def __init__(self, parent_frame: customtkinter.CTkFrame, username: str) -> None:

        self.username = username

        self.frame__security: customtkinter.CTkScrollableFrame = (
            customtkinter.CTkScrollableFrame(
                parent_frame,
                width=1058,
                height=578,
                fg_color="#0a0a0a",
            )
        )

        self.show_frame: Callable = lambda: (
            self.refresh(),
            self.frame__security.place(x=10, y=50),
        )
        self.hide_frame: Callable = lambda: self.frame__security.place_forget()

    def load_security_cards(self) -> None:

        total_security_events: list[tuple[str, str]] = (
            SERVER.lookup.security_event.recent(self.username, -1)
        )

        columns = 4

        for column in range(columns):

            self.frame__security.grid_columnconfigure(
                column,
                weight=1,
            )

        for n, (event_type, timestamp) in enumerate(total_security_events):

            get_event_labels = EVENT_LABELS.get(event_type, ("Unknown", "[INFO]"))

            card = customtkinter.CTkFrame(
                self.frame__security,
                width=252,
                height=38,
                fg_color="#111111",
            )

            column = n % columns
            row = n // columns

            card.grid(
                row=row,
                column=column,
                padx=5,
                pady=5,
                sticky="nsew",
            )

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
                width=89,
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
                width=244,
                height=0,  # 12
                font=("Consolas", 10),
                text_color="#A3A3A3",
            ).place(x=4, y=24)

    def refresh(self) -> None:

        for widget in self.frame__security.winfo_children():

            widget.destroy()

        self.load_security_cards()
