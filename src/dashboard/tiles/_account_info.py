lazy from ... import SERVER, assets, customtkinter


class account_info:

    def __init__(self, parent_frame: customtkinter.CTkFrame, username: str) -> None:

        self.frame__account_info: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame, width=500, height=300, fg_color="#0a0a0a"
        )
        self.frame__account_info.place(x=10, y=110)

        customtkinter.CTkLabel(
            self.frame__account_info,
            width=0,
            height=0,
            text="",
            image=customtkinter.CTkImage(
                light_image=assets.icons.material.id_card,
                dark_image=assets.icons.material.id_card,
                size=(100, 100),
            ),
        ).place(x=11, y=3)

        customtkinter.CTkLabel(
            self.frame__account_info,
            text=f"UUID: {SERVER.lookup.user.resolve_uuid(username)}",
            font=("Consolas", 15, "bold"),
        ).place(x=122, y=20)

        customtkinter.CTkLabel(
            self.frame__account_info,
            text=f"Created At: {SERVER.lookup.user.created_at(username)}",
            font=("Consolas", 15, "bold"),
        ).place(x=122, y=55)

        customtkinter.CTkLabel(
            self.frame__account_info,
            text=f"Full Name: {SERVER.lookup.user.full_name(username)}",
            font=("Consolas", 13, "bold"),
            height=0,  # 15
        ).place(x=22, y=126)

        customtkinter.CTkLabel(
            self.frame__account_info,
            text=f"Username: {username}",
            font=("Consolas", 13, "bold"),
            height=0,  # 15
        ).place(x=22, y=156)

        customtkinter.CTkLabel(
            self.frame__account_info,
            text=f"Email: {SERVER.lookup.user.email_address(username)}",
            font=("Consolas", 13, "bold"),
            height=0,  # 15
        ).place(x=22, y=186)

        customtkinter.CTkLabel(
            self.frame__account_info,
            text=f"Backup Code: {SERVER.lookup.user.backup_code(username)}",
            font=("Consolas", 13, "bold"),
            height=0,  # 15
        ).place(x=22, y=216)

        self.frame__account_metrics = customtkinter.CTkFrame(
            self.frame__account_info,
            width=456,
            height=58,
            fg_color="transparent",
        )
        self.frame__account_metrics.place(x=22, y=248)

        metrics = (
            (
                "Transactions",
                len(SERVER.lookup.user.transactions(username, -1)),
                "#218CFF",
            ),
            (
                "Favorites",
                len(SERVER.lookup.user.frequent_transfer_recipients(username)),
                "#A855F7",
            ),
            (
                "Security events",
                len(SERVER.lookup.security_event.recent(username, -1)),
                "#22C55E",
            ),
        )

        for index, (title, value, color) in enumerate(metrics):
            card = customtkinter.CTkFrame(
                self.frame__account_metrics,
                width=142,
                height=58,
                fg_color="#111111",
            )
            card.place(x=index * 156, y=0)
            customtkinter.CTkLabel(
                card,
                text=title,
                font=("Segoe UI", 10),
                text_color="#A3A3A3",
            ).place(x=10, y=8)
            customtkinter.CTkLabel(
                card,
                text=str(value),
                font=("Consolas", 18, "bold"),
                text_color=color,
            ).place(x=10, y=27)
