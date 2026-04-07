from . import *


class activation:

    def __init__(self, _keys: list[str]) -> None:
        self._keys = _keys

        self.__raw_accent_color = get_accent_color()
        self.__hvr_accent_color = utils.get_hvr_accent_color(self.__raw_accent_color)

        self.window = customtkinter.CTk()

        _width, _height = 532, 276
        _x_pos = int((self.window.winfo_screenwidth() / 2) - (_width / 2))
        _y_pos = int((self.window.winfo_screenheight() / 2) - (_height / 2))

        self.window.title("Bank With High Functionalities")
        self.window.geometry(f"{_width}x{_height}+{_x_pos}+{_y_pos}")

        apply_style(self.window, "transparent")
        title_bar.hide(self.window, no_span=True)

        self.window.minsize(_width, _height)
        self.window.maxsize(_width, _height)

        self.window.bind(
            "<Button-1>",
            lambda event: move_tk_with_no_titlebar_winos_native_ctypes(
                event, self.window
            ),
        )

        customtkinter.CTkLabel(
            self.window,
            text="Enter a product key",
            font=("Segoe UI", 21),
            bg_color="black",
            height=0,
            width=0,
            pady=20,
            justify="left",
        ).place(x=20, y=0)

        customtkinter.CTkLabel(
            self.window,
            text="""Bank With High Functionalities activation keys are available exclusively through
our official GitHub repository, offering source, product keys, software updates,
release notices, setup guidance, and important information for all users.""",
            font=("Segoe UI", 13),
            bg_color="black",
            height=0,
            width=0,
            justify="left",
        ).place(x=20, y=74)

        customtkinter.CTkLabel(
            self.window,
            text="Product Key",
            font=("Segoe UI", 13),
            bg_color="black",
            height=0,
            width=0,
            pady=20,
            justify="left",
        ).place(x=20, y=129)

        self.container_frame__activation_entry = customtkinter.CTkFrame(
            self.window,
            width=470,
            height=34,
            fg_color="black",
            bg_color="black",
            border_width=1,
            border_color="#FFFFFF",
            corner_radius=6,
        )

        self.container_frame__activation_label = customtkinter.CTkLabel(
            self.window,
            text="",
            font=("Roboto", 10),
            height=12,
            width=0,
            text_color="#FFFFFF",
        )

        customtkinter.CTkLabel(
            self.container_frame__activation_entry,
            image=customtkinter.CTkImage(
                light_image=icon__shield_lock,
                dark_image=icon__shield_lock,
                size=(20, 20),
            ),
            text="",
        ).place(x=8, rely=0.5, anchor="w")

        self.container_frame__activation_entry.place(x=20, y=173)

        self.__activation_code = customtkinter.CTkEntry(
            self.container_frame__activation_entry,
            placeholder_text="XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX",
            width=470 - 40,
            height=34 - 8,
            corner_radius=0,
            border_width=0,
            fg_color="transparent",
            font=("Roboto", 14),
        )
        self.__activation_code.place(x=28, rely=0.5, anchor="w")

        self.visit_repository__button = customtkinter.CTkButton(
            self.window,
            text="Repository",
            width=120,
            height=30,
            bg_color="black",
            fg_color="#333333",
            text_color="#FFFFFF",
            hover_color="#3D3D3D",
            image=customtkinter.CTkImage(
                light_image=icon__platform_github,
                dark_image=icon__platform_github,
                size=(17, 17),
            ),
            command=lambda: utils.Open_Browser_For_Specified_URL(
                CONSTANTS["WEBSITES"]["GITHUB_REPOSITORY"]
            ),
        )
        self.visit_repository__button.place(x=196, y=234)

        self.next_and_activate__button = customtkinter.CTkButton(
            self.window,
            text="Next",
            width=90,
            height=30,
            bg_color="black",
            fg_color=self.__raw_accent_color,
            text_color="#FFFFFF",
            hover_color=self.__hvr_accent_color,
            command=self._verify_product_key_and_redirect_to_activate,
        )
        self.next_and_activate__button.place(x=328, y=234)

        self.cancel_and_close__button = customtkinter.CTkButton(
            self.window,
            text="Cancel",
            width=90,
            height=30,
            bg_color="black",
            fg_color="#333333",
            text_color="#FFFFFF",
            hover_color="#3D3D3D",
            command=lambda: [self.window.destroy(), exit()],
        )
        self.cancel_and_close__button.place(x=430, y=234)

        self.window.mainloop()

    def _verify_product_key_and_redirect_to_activate(self):
        pass
