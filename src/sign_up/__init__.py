lazy from .. import SERVER, Callable, customtkinter, ui


class sign_up_interface:

    class sign_up:

        def __init__(self, parent_window: customtkinter.CTk):

            self.frame__signup: customtkinter.CTkFrame = customtkinter.CTkFrame(
                parent_window, width=1060, height=610, corner_radius=0
            )

            self.show_frame: Callable = lambda: self.frame__signup.place(x=20, y=20)
            self.hide_frame: Callable = lambda: self.frame__signup.place_forget()

            customtkinter.CTkLabel(
                self.frame__signup,
                text="Create your account",
                font=("Segoe UI", 24, "bold"),
            ).place(x=60, y=45)

            customtkinter.CTkLabel(
                self.frame__signup,
                text="Username",
                font=("Segoe UI", 13),
            ).place(x=60, y=115)
            _, username_entry = ui.entry_field(
                self.frame__signup, "username", 60, 140, width=420
            )

            customtkinter.CTkLabel(
                self.frame__signup,
                text="Full name",
                font=("Segoe UI", 13),
            ).place(x=60, y=195)
            _, full_name_entry = ui.entry_field(
                self.frame__signup, "full name", 60, 220, width=420
            )

            customtkinter.CTkLabel(
                self.frame__signup,
                text="Email (optional)",
                font=("Segoe UI", 13),
            ).place(x=60, y=275)
            _, email_entry = ui.entry_field(
                self.frame__signup, "email", 60, 300, width=420
            )

            _, password_entry = ui.entry_field(
                self.frame__signup,
                "password",
                560,
                140,
                width=420,
                show="•",
            )
            ui.add_password_toggle(self.frame__signup, password_entry, 920, 149)

            _, confirm_password_entry = ui.entry_field(
                self.frame__signup,
                "confirm password",
                560,
                220,
                width=420,
                show="•",
            )
            ui.add_password_toggle(self.frame__signup, confirm_password_entry, 920, 229)

            status_label = ui.status_label(self.frame__signup, 560, 300)

            def create_account() -> None:
                username = username_entry.get().strip()
                full_name = full_name_entry.get().strip()
                email = email_entry.get().strip()
                password = password_entry.get()
                confirm_password = confirm_password_entry.get()

                if not username or not full_name:
                    ui.set_status(
                        status_label, "Username and full name are required.", "danger"
                    )
                    return
                if len(password) < 8:
                    ui.set_status(
                        status_label,
                        "Password must be at least 8 characters long.",
                        "danger",
                    )
                    return
                if password != confirm_password:
                    ui.set_status(status_label, "Passwords do not match.", "danger")
                    return
                if SERVER.management.user.create(username, password, full_name, email):
                    ui.set_status(
                        status_label, "Account created. You can now sign in.", "success"
                    )
                    username_entry.delete(0, "end")
                    full_name_entry.delete(0, "end")
                    email_entry.delete(0, "end")
                    password_entry.delete(0, "end")
                    confirm_password_entry.delete(0, "end")
                else:
                    ui.set_status(
                        status_label, "Username or email already exists.", "danger"
                    )

            customtkinter.CTkButton(
                self.frame__signup,
                text="Create account",
                width=420,
                height=44,
                command=create_account,
            ).place(x=560, y=350)
