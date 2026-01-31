from . import *
from PIL import Image

icon__developer_mode_tv = Image.open(
    rf"{DIR_PATH}\assets\icons\material icons\developer_mode_tv.png"
)


class administrator:
    def __init__(self, parent: customtkinter.CTk):

        self.window__developer = customtkinter.CTkToplevel(parent)
        self.window__developer.geometry("1000x500")
        self.window__developer.title("Developer")
        self.window__developer.resizable(False, False)
        self.frame__developer = customtkinter.CTkFrame(
            self.window__developer, width=980, height=480
        )
        self.frame__developer.place(x=10, y=10)

        def hover(_):
            rame = customtkinter.CTkFrame(self.frame__developer, width=100, height=100)
            rame.place(x=300, y=100)

        dev = customtkinter.CTkButton(
            self.frame__developer,
            text="",
            image=customtkinter.CTkImage(
                light_image=icon__developer_mode_tv,
                dark_image=icon__developer_mode_tv,
                size=(10, 10),
            ),
            fg_color="transparent",
            hover=False,
            width=0,
            height=0,
        )
        dev.place(x=89, y=100)
        dev.bind("<Motion>", hover)
        customtkinter.CTkButton(
            self.frame__developer,
            text="Exit",
            command=self.window__developer.destroy,
        ).place(x=200, y=300)
