from .. import *


class sign_up_interface:

    class sign_up:

        def __init__(self, parent_window: customtkinter.CTk):

            self.frame__signup: customtkinter.CTkFrame = customtkinter.CTkFrame(
                parent_window, width=1060, height=610, corner_radius=0
            )

            self.show_frame: Callable = lambda: self.frame__signup.place(x=20, y=20)
            self.hide_frame: Callable = lambda: self.frame__signup.place_forget()
