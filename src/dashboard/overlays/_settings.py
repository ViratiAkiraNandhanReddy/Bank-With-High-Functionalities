lazy from ... import SERVER, Callable, customtkinter, ui
lazy from ...ui import add_password_toggle


class settings_overlay:

    def __init__(self, parent_frame: customtkinter.CTkFrame, username: str) -> None:

        self.frame__settings: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame, width=1080, height=590, fg_color="#0a0a0a"
        )

        self.show_frame: Callable = lambda: self.frame__settings.place(x=10, y=50)
        self.hide_frame: Callable = lambda: self.frame__settings.place_forget()

        ui.section_title(self.frame__settings, "Account settings", x=35, y=28)
        customtkinter.CTkLabel(
            self.frame__settings,
            text="Manage your profile, security, and account health.",
            font=("Segoe UI", 13),
            text_color=ui.COLORS["muted"],
            anchor="w",
        ).place(x=38, y=67)

        profile_card = customtkinter.CTkFrame(
            self.frame__settings,
            width=390,
            height=190,
            fg_color=ui.COLORS["card"],
            border_width=1,
            border_color="#252525",
            corner_radius=8,
        )
        profile_card.place(x=25, y=105)

        customtkinter.CTkLabel(
            profile_card,
            text="PROFILE",
            font=("Segoe UI", 11, "bold"),
            text_color=ui.COLORS["info"],
            anchor="w",
        ).place(x=20, y=16)
        customtkinter.CTkLabel(
            profile_card,
            text=SERVER.lookup.user.full_name(username),
            font=("Segoe UI", 21, "bold"),
            text_color=ui.COLORS["text"],
            anchor="w",
        ).place(x=20, y=43)
        customtkinter.CTkLabel(
            profile_card,
            text=f"@{username}",
            font=("Consolas", 13),
            text_color=ui.COLORS["muted"],
            anchor="w",
        ).place(x=20, y=78)
        customtkinter.CTkLabel(
            profile_card,
            text=SERVER.lookup.user.email_address(username) or "No email address added",
            font=("Segoe UI", 12),
            text_color=ui.COLORS["muted"],
            anchor="w",
        ).place(x=20, y=112)
        customtkinter.CTkLabel(
            profile_card,
            text="Active account",
            font=("Segoe UI", 12, "bold"),
            text_color=ui.COLORS["success"],
            anchor="w",
        ).place(x=20, y=150)

        account_card = customtkinter.CTkFrame(
            self.frame__settings,
            width=390,
            height=190,
            fg_color=ui.COLORS["card"],
            border_width=1,
            border_color="#252525",
            corner_radius=8,
        )
        account_card.place(x=435, y=105)

        customtkinter.CTkLabel(
            account_card,
            text="ACCOUNT SNAPSHOT",
            font=("Segoe UI", 11, "bold"),
            text_color=ui.COLORS["success"],
            anchor="w",
        ).place(x=20, y=16)
        ui.metric_card(
            account_card,
            "Balance",
            f"$ {SERVER.lookup.user.balance(username):,.2f}",
            20,
            43,
            width=160,
            color="success",
        )
        ui.metric_card(
            account_card,
            "Member since",
            str(SERVER.lookup.user.created_at(username))[:10],
            200,
            43,
            width=165,
            color="info",
        )

        security_card = ui.action_tile(
            self.frame__settings,
            "Security center",
            "Update your password regularly and never share it with anyone.",
            25,
            305,
            accent="warning",
            width=390,
            height=285,
        )

        activity_card = ui.action_tile(
            self.frame__settings,
            "Account activity",
            "A quick view of your recent account usage.",
            435,
            305,
            accent="info",
            width=390,
            height=230,
        )
        last_login = SERVER.lookup.user.last_login(username)
        customtkinter.CTkLabel(
            activity_card,
            text="Last sign-in",
            font=("Segoe UI", 12),
            text_color=ui.COLORS["muted"],
            anchor="w",
        ).place(x=35, y=105)
        customtkinter.CTkLabel(
            activity_card,
            text=(
                last_login.astimezone().strftime("%d %b %Y, %I:%M %p")
                if last_login is not None
                else "No previous sign-in"
            ),
            font=("Consolas", 12, "bold"),
            text_color=ui.COLORS["text"],
            anchor="w",
        ).place(x=145, y=105)
        customtkinter.CTkLabel(
            activity_card,
            text="Transactions",
            font=("Segoe UI", 12),
            text_color=ui.COLORS["muted"],
            anchor="w",
        ).place(x=35, y=135)
        customtkinter.CTkLabel(
            activity_card,
            text=str(len(SERVER.lookup.user.transactions(username, -1))),
            font=("Consolas", 12, "bold"),
            text_color=ui.COLORS["text"],
            anchor="w",
        ).place(x=145, y=135)
        customtkinter.CTkLabel(
            activity_card,
            text="Security events",
            font=("Segoe UI", 12),
            text_color=ui.COLORS["muted"],
            anchor="w",
        ).place(x=35, y=165)
        customtkinter.CTkLabel(
            activity_card,
            text=str(len(SERVER.lookup.security_event.recent(username, 10))),
            font=("Consolas", 12, "bold"),
            text_color=ui.COLORS["text"],
            anchor="w",
        ).place(x=145, y=165)

        current_password = customtkinter.CTkEntry(
            security_card,
            width=320,
            height=40,
            placeholder_text="current password",
            show="•",
        )
        current_password.place(x=35, y=93)
        add_password_toggle(security_card, current_password, x=300, y=101)

        new_password = customtkinter.CTkEntry(
            security_card,
            width=320,
            height=40,
            placeholder_text="new password",
            show="•",
        )
        new_password.place(x=35, y=138)
        add_password_toggle(security_card, new_password, x=300, y=146)

        confirm_password = customtkinter.CTkEntry(
            security_card,
            width=320,
            height=40,
            placeholder_text="confirm new password",
            show="•",
        )
        confirm_password.place(x=35, y=183)
        add_password_toggle(security_card, confirm_password, x=300, y=191)

        status_label = customtkinter.CTkLabel(
            security_card,
            text="",
            font=("Segoe UI", 13),
        )
        status_label.place(x=35, y=228)

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
            security_card,
            text="Update password",
            width=320,
            height=42,
            command=update_password,
        ).place(x=35, y=252)
