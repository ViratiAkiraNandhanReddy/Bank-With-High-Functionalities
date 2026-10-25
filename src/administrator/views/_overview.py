lazy from ... import SERVER, Callable, customtkinter


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

        customtkinter.CTkLabel(
            self.frame__overview,
            text="Administrator overview",
            font=("Segoe UI", 24, "bold"),
        ).place(x=35, y=30)

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
            card = customtkinter.CTkFrame(
                self.frame__overview,
                width=180,
                height=115,
                fg_color="#111111",
            )
            card.place(x=35 + index * 200, y=95)
            customtkinter.CTkLabel(
                card,
                text=title,
                font=("Segoe UI", 14),
                text_color="#A3A3A3",
            ).place(x=18, y=18)
            customtkinter.CTkLabel(
                card,
                text=value,
                font=("Consolas", 24, "bold"),
                text_color=color,
            ).place(x=18, y=52)

        customtkinter.CTkLabel(
            self.frame__overview,
            text="Recent users",
            font=("Segoe UI", 18, "bold"),
        ).place(x=35, y=245)

        customtkinter.CTkLabel(
            self.frame__overview,
            text="Recent security activity",
            font=("Segoe UI", 18, "bold"),
        ).place(x=470, y=245)

        for row, user in enumerate(users[:6]):
            customtkinter.CTkLabel(
                self.frame__overview,
                text=f"{user[0]}  |  {user[1]}  |  $ {user[2]:,.2f}",
                font=("Consolas", 12),
                text_color="#D4D4D4",
                anchor="w",
            ).place(x=40, y=285 + row * 38)

        for row, event in enumerate(recent_events[:6]):
            customtkinter.CTkLabel(
                self.frame__overview,
                text=f"{event[0]}  |  {event[1]}",
                font=("Consolas", 11),
                text_color="#D4D4D4",
                anchor="w",
            ).place(x=475, y=285 + row * 38)
