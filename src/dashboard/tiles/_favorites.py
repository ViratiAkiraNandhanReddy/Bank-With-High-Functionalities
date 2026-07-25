from ... import customtkinter, assets, SERVER


class favorites:

    def __init__(self, parent_frame: customtkinter.CTkFrame, username: str) -> None:

        self.username = username

        self.frame__favorites: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame, width=245, height=220, fg_color="#0a0a0a"
        )
        self.frame__favorites.place(x=10, y=420)

        self.load_favorites_cards()

    def load_favorites_cards(self) -> None:

        frequent_transfer_recipients: list[tuple[str, int]] = (
            SERVER.lookup.user.frequent_transfer_recipients(self.username)
        )

        for n, (recipient, count) in enumerate(frequent_transfer_recipients):

            card = customtkinter.CTkFrame(
                self.frame__favorites, width=231, height=64, fg_color="#111111"
            )
            card.place(x=7, y=(7 + n * (64 + 7)))

            customtkinter.CTkLabel(
                card,
                text=(recipient if len(recipient) < 25 else recipient[:21] + "..."),
                width=231,
                height=26,
                font=("Consolas", 16, "bold"),
                text_color="#D4D4D4",
            ).place(x=0, y=6)

            customtkinter.CTkLabel(
                card,
                text=f"{count} transfers",
                width=231,
                height=26,
                font=("Consolas", 12),
                text_color="#FFFFFF",
            ).place(x=0, y=32)

    def refresh(self) -> None:

        widget: customtkinter.CTkFrame

        for widget in self.frame__favorites.winfo_children():

            widget.destroy()

        self.load_favorites_cards()
