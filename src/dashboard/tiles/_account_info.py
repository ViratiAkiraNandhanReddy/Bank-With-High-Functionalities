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
