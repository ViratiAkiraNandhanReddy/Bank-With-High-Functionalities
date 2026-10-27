lazy from ... import SERVER, Callable, customtkinter


class activity_and_history:

    def __init__(self, parent_frame: customtkinter.CTkFrame) -> None:

        self.frame__activity_and_history: customtkinter.CTkFrame = (
            customtkinter.CTkFrame(
                parent_frame, width=870, height=590, fg_color="#0a0a0a"
            )
        )

        self.show_frame: Callable = lambda: self.frame__activity_and_history.place(
            x=220, y=50
        )
        self.hide_frame: Callable = (
            lambda: self.frame__activity_and_history.place_forget()
        )

        customtkinter.CTkLabel(
            self.frame__activity_and_history,
            text="Activity & history",
            font=("Segoe UI", 24, "bold"),
        ).place(x=35, y=30)

        events_frame = customtkinter.CTkScrollableFrame(
            self.frame__activity_and_history,
            width=790,
            height=465,
            fg_color="#111111",
        )
        events_frame.place(x=35, y=90)

        for row, (username, event_type, timestamp) in enumerate(
            SERVER.lookup.admin.recent_security_events(100)
        ):
            customtkinter.CTkLabel(
                events_frame,
                text=f"{timestamp}  |  {username}  |  {event_type}",
                font=("Consolas", 12),
                anchor="w",
            ).grid(row=row, column=0, padx=15, pady=7, sticky="w")
