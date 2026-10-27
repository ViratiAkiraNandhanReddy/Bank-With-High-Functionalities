lazy from ... import SERVER, Callable, customtkinter, ui
lazy from ...ui import add_password_toggle


class users_and_access:

    def __init__(self, parent_frame: customtkinter.CTkFrame, username: str) -> None:

        self.frame__users_and_access: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame, width=870, height=590, fg_color="#0a0a0a"
        )

        self.show_frame: Callable = lambda: self.frame__users_and_access.place(
            x=220, y=50
        )
        self.hide_frame: Callable = lambda: self.frame__users_and_access.place_forget()

        if username != "administrator":
            customtkinter.CTkLabel(
                self.frame__users_and_access,
                text="Only the administrator account can create administrator accounts.",
                font=("Segoe UI", 16, "bold"),
            ).place(x=40, y=40)
            return

        ui.action_tile(
            self.frame__users_and_access,
            "Create administrator",
            "Only the root administrator can add new administrator accounts.",
            25,
            20,
            accent="success",
            width=390,
            height=500,
        )

        customtkinter.CTkLabel(
            self.frame__users_and_access,
            text="Username",
            font=("Segoe UI", 13),
        ).place(x=40, y=105)
        username_entry = customtkinter.CTkEntry(
            self.frame__users_and_access,
            width=360,
            height=38,
            placeholder_text="username",
        )
        username_entry.place(x=40, y=130)

        customtkinter.CTkLabel(
            self.frame__users_and_access,
            text="Password",
            font=("Segoe UI", 13),
        ).place(x=40, y=185)
        password_entry = customtkinter.CTkEntry(
            self.frame__users_and_access,
            width=360,
            height=38,
            placeholder_text="password",
            show="•",
        )
        password_entry.place(x=40, y=210)
        add_password_toggle(self.frame__users_and_access, password_entry, x=340, y=217)

        customtkinter.CTkLabel(
            self.frame__users_and_access,
            text="Confirm password",
            font=("Segoe UI", 13),
        ).place(x=40, y=265)
        confirm_password_entry = customtkinter.CTkEntry(
            self.frame__users_and_access,
            width=360,
            height=38,
            placeholder_text="confirm password",
            show="•",
        )
        confirm_password_entry.place(x=40, y=290)
        add_password_toggle(
            self.frame__users_and_access,
            confirm_password_entry,
            x=340,
            y=297,
        )

        customtkinter.CTkLabel(
            self.frame__users_and_access,
            text="Email (optional)",
            font=("Segoe UI", 13),
        ).place(x=40, y=345)
        email_entry = customtkinter.CTkEntry(
            self.frame__users_and_access,
            width=360,
            height=38,
            placeholder_text="email",
        )
        email_entry.place(x=40, y=370)

        status_label = customtkinter.CTkLabel(
            self.frame__users_and_access,
            text="",
            font=("Segoe UI", 13),
            anchor="w",
        )
        status_label.place(x=40, y=425)

        def create_admin() -> None:
            new_username = username_entry.get().strip()
            password = password_entry.get()
            confirm_password = confirm_password_entry.get()
            email = email_entry.get().strip()

            if not new_username:
                status_label.configure(
                    text="Enter a username.",
                    text_color="#FF0000",
                )
                return

            if len(password) < 8:
                status_label.configure(
                    text="Password must be at least 8 characters long.",
                    text_color="#FF0000",
                )
                return

            if password != confirm_password:
                status_label.configure(
                    text="Passwords do not match.",
                    text_color="#FF0000",
                )
                return

            if SERVER.management.admin.create(new_username, password, email):
                username_entry.delete(0, "end")
                password_entry.delete(0, "end")
                confirm_password_entry.delete(0, "end")
                email_entry.delete(0, "end")
                status_label.configure(
                    text=f"Administrator '{new_username}' created.",
                    text_color="#00C853",
                )
            else:
                status_label.configure(
                    text="Username already exists or account creation failed.",
                    text_color="#FF0000",
                )

        customtkinter.CTkButton(
            self.frame__users_and_access,
            text="Create administrator",
            width=360,
            height=42,
            command=create_admin,
        ).place(x=40, y=470)

        ui.action_tile(
            self.frame__users_and_access,
            "Registered administrators",
            "Review the administrator accounts currently allowed to access the console.",
            435,
            20,
            accent="info",
            width=400,
            height=500,
        )

        administrators_frame = customtkinter.CTkScrollableFrame(
            self.frame__users_and_access,
            width=365,
            height=370,
            fg_color="transparent",
        )
        administrators_frame.place(x=450, y=120)

        for row, (admin_username, email, created_at) in enumerate(
            SERVER.lookup.admin.administrators()
        ):
            customtkinter.CTkLabel(
                administrators_frame,
                text=f"{admin_username}\n{email or 'No email'}\n{created_at}",
                font=("Consolas", 11),
                justify="left",
                anchor="w",
            ).grid(row=row, column=0, padx=12, pady=10, sticky="w")
