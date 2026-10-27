lazy from .. import SERVER, customtkinter


class status_panel:

    def __init__(self, parent_frame: customtkinter.CTkFrame) -> None:

        self.frame__status_panel: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame, width=830, height=30, fg_color="#0a0a0a"
        )
        self.frame__status_panel.place(x=220, y=10)

        users = SERVER.lookup.admin.users()
        administrators = SERVER.lookup.admin.administrators()

        customtkinter.CTkLabel(
            self.frame__status_panel,
            text="SYSTEM ONLINE",
            font=("Consolas", 12, "bold"),
            text_color="#22C55E",
        ).place(x=12, rely=0.5, anchor="w")

        customtkinter.CTkLabel(
            self.frame__status_panel,
            text=f"Users: {len(users)}  |  Administrators: {len(administrators)}",
            font=("Consolas", 12),
            text_color="#A3A3A3",
        ).place(relx=1, x=-12, rely=0.5, anchor="e")
