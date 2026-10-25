lazy from ... import SERVER, Callable, customtkinter
lazy from ...ui import add_password_toggle


class settings_overlay:

    def __init__(self, parent_frame: customtkinter.CTkFrame, username: str) -> None:

        self.frame__settings: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame, width=1080, height=590, fg_color="#0a0a0a"
        )

        self.show_frame: Callable = lambda: self.frame__settings.place(x=10, y=50)
        self.hide_frame: Callable = lambda: self.frame__settings.place_forget()

        customtkinter.CTkLabel(
            self.frame__settings,
            text="Account settings",
            font=("Segoe UI", 24, "bold"),
        ).place(x=40, y=35)

        customtkinter.CTkLabel(
            self.frame__settings,
            text="Change password",
            font=("Segoe UI", 17, "bold"),
        ).place(x=40, y=95)

        current_password = customtkinter.CTkEntry(
            self.frame__settings,
            width=360,
            height=40,
            placeholder_text="current password",
            show="•",
        )
        current_password.place(x=40, y=135)
        add_password_toggle(self.frame__settings, current_password, x=340, y=143)

        new_password = customtkinter.CTkEntry(
            self.frame__settings,
            width=360,
            height=40,
            placeholder_text="new password",
            show="•",
        )
        new_password.place(x=40, y=190)
        add_password_toggle(self.frame__settings, new_password, x=340, y=198)

        confirm_password = customtkinter.CTkEntry(
            self.frame__settings,
            width=360,
            height=40,
            placeholder_text="confirm new password",
            show="•",
        )
        confirm_password.place(x=40, y=245)
        add_password_toggle(self.frame__settings, confirm_password, x=340, y=253)

        status_label = customtkinter.CTkLabel(
            self.frame__settings,
            text="",
            font=("Segoe UI", 13),
        )
        status_label.place(x=40, y=300)

        def update_password() -> None:
            current = current_password.get()
            new = new_password.get()
            confirm = confirm_password.get()
            if not SERVER.authentication.user.password(username, current):
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
            if SERVER.management.user.change_password(username, new):
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
            text="Update password",
            width=360,
            height=42,
            command=update_password,
        ).place(x=40, y=345)
