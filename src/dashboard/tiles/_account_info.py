from ... import customtkinter, assets, SERVER


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

        customtkinter.CTkLabel(
            self.frame__account_info,
            text="Keep your backup code private. It can be used to recover access to"
            + "\n"
            + "your account if you lose access to your primary sign-in method.",
            font=("Consolas", 11),
            height=0,  # 26
            width=456,
        ).place(x=22, y=252)
