lazy from ... import SERVER, Callable, customtkinter, ui
lazy from ...ui import add_password_toggle


class settings:

    def __init__(self, parent_frame: customtkinter.CTkFrame, username: str) -> None:

        self.frame__settings: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame, width=870, height=590, fg_color="#0a0a0a"
        )

        self.show_frame: Callable = lambda: self.frame__settings.place(x=220, y=50)
        self.hide_frame: Callable = lambda: self.frame__settings.place_forget()

        customtkinter.CTkLabel(
            self.frame__settings,
            text="Administrator settings",
            font=("Segoe UI", 24, "bold"),
        ).place(x=35, y=30)

        customtkinter.CTkLabel(
            self.frame__settings,
            text=f"Signed in as: {username}",
            font=("Segoe UI", 14),
            text_color="#A3A3A3",
        ).place(x=35, y=80)

        ui.action_tile(
            self.frame__settings,
            "Update administrator password",
            "Use a strong password and keep your administrator account protected.",
            20,
            105,
            accent="warning",
            width=410,
            height=390,
        )

        ui.action_tile(
            self.frame__settings,
            "Administrator security",
            "Use a unique password, avoid sharing access, and sign out when finished.",
            455,
            105,
            accent="info",
            width=390,
            height=220,
        )

        current_password = customtkinter.CTkEntry(
            self.frame__settings,
            width=360,
            height=40,
            placeholder_text="current password",
            show="•",
        )
        current_password.place(x=35, y=180)
        add_password_toggle(self.frame__settings, current_password, x=335, y=188)

        new_password = customtkinter.CTkEntry(
            self.frame__settings,
            width=360,
            height=40,
            placeholder_text="new password",
            show="•",
        )
        new_password.place(x=35, y=235)
        add_password_toggle(self.frame__settings, new_password, x=335, y=243)

        confirm_password = customtkinter.CTkEntry(
            self.frame__settings,
            width=360,
            height=40,
            placeholder_text="confirm new password",
            show="•",
        )
        confirm_password.place(x=35, y=290)
        add_password_toggle(self.frame__settings, confirm_password, x=335, y=298)

        status_label = customtkinter.CTkLabel(
            self.frame__settings,
            text="",
            font=("Segoe UI", 13),
        )
        status_label.place(x=35, y=350)

        def update_password() -> None:
            current = current_password.get()
            new = new_password.get()
            confirm = confirm_password.get()
            if not SERVER.authentication.admin.password(username, current):
                status_label.configure(
                    text="Current password is incorrect.",
                    text_color="#FF0000",
                )
                return
            if len(new) < 8:
                status_label.configure(
                    text="Password must be at least 8 characters long.",
                    text_color="#FF0000",
                )
                return
            if new != confirm:
                status_label.configure(
                    text="Passwords do not match.",
                    text_color="#FF0000",
                )
                return
            if SERVER.management.admin.change_password(username, new):
                current_password.delete(0, "end")
                new_password.delete(0, "end")
                confirm_password.delete(0, "end")
                status_label.configure(
                    text="Password updated.",
                    text_color="#22C55E",
                )
            else:
                status_label.configure(
                    text="Password update failed.",
                    text_color="#FF0000",
                )

        customtkinter.CTkButton(
            self.frame__settings,
            text="Change password",
            width=360,
            height=42,
            command=update_password,
        ).place(x=35, y=395)
