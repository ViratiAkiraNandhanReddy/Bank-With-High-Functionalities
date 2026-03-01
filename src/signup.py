from . import *


class signup_interface:

    class signup:

        def __init__(self, parent_window: customtkinter.CTk):

            self.frame__signup = customtkinter.CTkFrame(parent_window, corner_radius=0)
            self.frame__signup.configure(width=910, height=560)

            self.show_frame = lambda: self.frame__signup.place(x=20, y=20)
            self.hide_frame = lambda: self.frame__signup.place_forget()
