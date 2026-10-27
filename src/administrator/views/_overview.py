lazy from ... import SERVER, Callable, customtkinter, ui


class overview:

    def __init__(self, parent_frame: customtkinter.CTkFrame, username: str) -> None:

        self.frame__overview: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame, width=870, height=590, fg_color="#0a0a0a"
        )

        self.show_frame: Callable = lambda: self.frame__overview.place(x=220, y=50)
        self.hide_frame: Callable = lambda: self.frame__overview.place_forget()

        self.refresh()

    def refresh(self) -> None:

        for widget in self.frame__overview.winfo_children():
            widget.destroy()

        ui.section_title(self.frame__overview, "Administrator overview", x=35, y=30)

        users = SERVER.lookup.admin.users()
        admins = SERVER.lookup.admin.administrators()
        total_balance = sum(user[2] for user in users)

        recent_events = SERVER.lookup.admin.recent_security_events(100)

        cards = (
            ("Users", str(len(users)), "#218CFF"),
            ("Administrators", str(len(admins)), "#A855F7"),
            ("Total balance", f"$ {total_balance:,.2f}", "#22C55E"),
            ("Security events", str(len(recent_events)), "#F59E0B"),
        )

        for index, (title, value, color) in enumerate(cards):
            ui.metric_card(
                self.frame__overview,
                title,
                value,
                35 + index * 200,
                95,
                width=180,
                color=color,
            )

        recent_users_card = ui.action_tile(
            self.frame__overview,
            "Recent users",
            "Newest accounts and current balances.",
            35,
            225,
            width=390,
            height=300,
            accent="info",
        )
        recent_events_card = ui.action_tile(
            self.frame__overview,
            "Recent security activity",
            "Latest authentication and account events.",
            445,
            225,
            width=390,
            height=300,
            accent="warning",
        )

        for row, user in enumerate(users[:6]):
            customtkinter.CTkLabel(
                recent_users_card,
                text=f"{user[0]}  |  {user[1]}  |  $ {user[2]:,.2f}",
                font=("Consolas", 12),
                text_color="#D4D4D4",
                anchor="w",
            ).place(x=35, y=92 + row * 32)

        for row, event in enumerate(recent_events[:6]):
            customtkinter.CTkLabel(
                recent_events_card,
                text=f"{event[0]}  |  {event[1]}",
                font=("Consolas", 11),
                text_color="#D4D4D4",
                anchor="w",
            ).place(x=35, y=92 + row * 32)
