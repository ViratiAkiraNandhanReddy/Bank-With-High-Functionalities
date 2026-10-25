lazy from ... import Callable, CONSTANTS, customtkinter, utils


class support_overlay:

    def __init__(self, parent_frame: customtkinter.CTkFrame, username: str) -> None:

        self.frame__support: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame, width=1080, height=590, fg_color="#0a0a0a"
        )

        self.show_frame: Callable = lambda: self.frame__support.place(x=10, y=50)
        self.hide_frame: Callable = lambda: self.frame__support.place_forget()

        customtkinter.CTkLabel(
            self.frame__support,
            text="Support",
            font=("Segoe UI", 24, "bold"),
        ).place(x=40, y=35)

        customtkinter.CTkLabel(
            self.frame__support,
            text=(
                "Need help with your account or a transaction?\n"
                "Use the project resources below to report an issue or get support."
            ),
            font=("Segoe UI", 15),
            justify="left",
            anchor="w",
        ).place(x=40, y=100)

        customtkinter.CTkButton(
            self.frame__support,
            text="Open documentation",
            width=260,
            height=42,
            command=lambda: utils.browser.open_url(CONSTANTS["website"]["home"]),
        ).place(x=40, y=210)

        customtkinter.CTkButton(
            self.frame__support,
            text="Report an issue",
            width=260,
            height=42,
            command=lambda: utils.browser.open_url(CONSTANTS["github"]["issues"]),
        ).place(x=40, y=265)

        customtkinter.CTkButton(
            self.frame__support,
            text="Open discussions",
            width=260,
            height=42,
            command=lambda: utils.browser.open_url(CONSTANTS["github"]["discussions"]),
        ).place(x=40, y=320)
