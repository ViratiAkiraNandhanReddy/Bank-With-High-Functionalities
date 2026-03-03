from . import *


class dashboard:

    def __init__(self, username: str, parent: customtkinter.CTk) -> None:
        self.username = username

        self.window__dashboard = customtkinter.CTkToplevel(parent)

    class transactions:

        def __init__(self) -> None:
            pass

    class settings:

        def __init__(self) -> None:
            pass
