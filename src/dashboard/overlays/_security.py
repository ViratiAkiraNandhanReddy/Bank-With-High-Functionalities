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

        self.frame__security: customtkinter.CTkScrollableFrame = customtkinter.CTkScrollableFrame(
            parent_frame, width=1058, height=578, fg_color="#0a0a0a",
        )

        self.show_frame: Callable = lambda: (
            self.refresh(),
            self.frame__security.place(x=10, y=50),
        )
        self.hide_frame: Callable = lambda: self.frame__security.place_forget()

    def refresh(self) -> None:

        pass
