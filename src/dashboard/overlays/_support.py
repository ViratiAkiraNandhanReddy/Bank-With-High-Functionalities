lazy from ... import Callable, CONSTANTS, customtkinter, ui, utils


class support_overlay:

    def __init__(self, parent_frame: customtkinter.CTkFrame, username: str) -> None:

        self.frame__support: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame, width=1080, height=590, fg_color="#0a0a0a"
        )

        self.show_frame: Callable = lambda: self.frame__support.place(x=10, y=50)
        self.hide_frame: Callable = lambda: self.frame__support.place_forget()

        ui.section_title(self.frame__support, "Support", x=40, y=35)

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

        ui.action_tile(
            self.frame__support,
            title="Documentation",
            description="Learn the main flows and find guidance for common account tasks.",
            x=40,
            y=190,
            command=lambda: utils.browser.open_url(CONSTANTS["website"]["home"]),
            accent="info",
            width=300,
            height=140,
        )

        ui.action_tile(
            self.frame__support,
            title="Report an issue",
            description="Tell us what went wrong so the problem can be investigated.",
            x=360,
            y=190,
            command=lambda: utils.browser.open_url(CONSTANTS["github"]["issues"]),
            accent="danger",
            width=300,
            height=140,
        )

        ui.action_tile(
            self.frame__support,
            title="Community discussions",
            description="Ask questions, share feedback, and connect with the project community.",
            x=40,
            y=350,
            command=lambda: utils.browser.open_url(CONSTANTS["github"]["discussions"]),
            accent="success",
            width=300,
            height=140,
        )
