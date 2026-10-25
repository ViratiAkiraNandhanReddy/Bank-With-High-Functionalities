lazy from .. import SERVER, Callable, customtkinter


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
            username_entry = customtkinter.CTkEntry(
                self.frame__signup,
                width=420,
                height=40,
                placeholder_text="username",
            )
            username_entry.place(x=60, y=140)

            customtkinter.CTkLabel(
                self.frame__signup,
                text="Full name",
                font=("Segoe UI", 13),
            ).place(x=60, y=195)
            full_name_entry = customtkinter.CTkEntry(
                self.frame__signup,
                width=420,
                height=40,
                placeholder_text="full name",
            )
            full_name_entry.place(x=60, y=220)

            customtkinter.CTkLabel(
                self.frame__signup,
                text="Email (optional)",
                font=("Segoe UI", 13),
            ).place(x=60, y=275)
            email_entry = customtkinter.CTkEntry(
                self.frame__signup,
                width=420,
                height=40,
                placeholder_text="email",
            )
            email_entry.place(x=60, y=300)

            password_entry = customtkinter.CTkEntry(
                self.frame__signup,
                width=420,
                height=40,
                placeholder_text="password",
                show="•",
            )
            password_entry.place(x=560, y=140)

            confirm_password_entry = customtkinter.CTkEntry(
                self.frame__signup,
                width=420,
                height=40,
                placeholder_text="confirm password",
                show="•",
            )
            confirm_password_entry.place(x=560, y=220)

            status_label = customtkinter.CTkLabel(
                self.frame__signup,
                text="",
                font=("Segoe UI", 13),
            )
            status_label.place(x=560, y=300)

            def create_account() -> None:
                username = username_entry.get().strip()
                full_name = full_name_entry.get().strip()
                email = email_entry.get().strip()
                password = password_entry.get()
                confirm_password = confirm_password_entry.get()

                if not username or not full_name:
                    status_label.configure(
                        text="Username and full name are required.",
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
                if SERVER.management.user.create(username, password, full_name, email):
                    status_label.configure(
                        text="Account created. You can now sign in.",
                        text_color="#22C55E",
                    )
                    username_entry.delete(0, "end")
                    full_name_entry.delete(0, "end")
                    email_entry.delete(0, "end")
                    password_entry.delete(0, "end")
                    confirm_password_entry.delete(0, "end")
                else:
                    status_label.configure(
                        text="Username or email already exists.",
                        text_color="#FF0000",
                    )

            customtkinter.CTkButton(
                self.frame__signup,
                text="Create account",
                width=420,
                height=44,
                command=create_account,
            ).place(x=560, y=350)
