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

        self.window.bind(  # Allowing the user to move the window by dragging anywhere on it, since there is no title bar.
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
            height=0,
            width=268,
            text_color="#FF0000",
            bg_color="black",
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

        self.curr_key = customtkinter.StringVar()
        self.curr_key.trace_add(
            "write", lambda *args: self.curr_key.set(self.curr_key.get().upper()[:49])
        )

        self.__activation_code = customtkinter.CTkEntry(
            self.container_frame__activation_entry,
            placeholder_text="XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX",
            width=470 - 40,
            height=34 - 8,
            corner_radius=0,
            border_width=0,
            fg_color="transparent",
            font=("Consolas", 14),  # Consolas / Roboto
        )
        self.__activation_code.place(x=28, rely=0.5, anchor="w")

        self.__activation_code.bind(
            "<FocusIn>",
            lambda event: self.__activation_code.configure(textvariable=self.curr_key),
        )

        self.__activation_code.bind(
            "<FocusOut>",
            lambda event: self.__activation_code.configure(textvariable=None)
            or self.__activation_code.unbind("<FocusIn>"),
        )

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
                CONSTANTS["github"]["repository"]
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

    def _verify_product_key_and_redirect_to_activate(self) -> None:

        entered_key = self.__activation_code.get().strip()

        self.__activation_code.bind(
            "<KeyPress>",
            lambda event: self.container_frame__activation_entry.configure(
                border_color="#FFFFFF"
            )
            or self.container_frame__activation_label.place_forget()
            or self.__activation_code.unbind("<KeyPress>"),
        )

        if entered_key not in self._keys:
            self.container_frame__activation_entry.configure(border_color="#FF0000")
            self.container_frame__activation_label.configure(
                text="Invalid product key. Please check the repository for valid keys"
            )
            self.container_frame__activation_label.place(x=200, y=167)

            return

        for widget in self.window.winfo_children():

            if isinstance(widget, customtkinter.CTkLabel) or isinstance(
                widget, customtkinter.CTkFrame
            ):
                widget.destroy()
        else:
            self.visit_repository__button.destroy()

        customtkinter.CTkLabel(
            self.window,
            text="Ready to activate",
            font=("Segoe UI", 21),
            bg_color="black",
            height=0,
            width=0,
            pady=20,
            justify="left",
        ).place(x=20, y=0)

        customtkinter.CTkLabel(
            self.window,
            text="""By activating Bank With High Functionalities, you will unlock the full potential of
our software, gaining access to all features and functionalities. We appreciate
your support and trust in our product. If you have any questions or need
assistance, please don't hesitate to contact via github discussions.""",
            font=("Segoe UI", 13),
            bg_color="black",
            height=0,
            width=0,
            justify="left",
            text_color="#FFFB00",
        ).place(x=20, y=74)

        customtkinter.CTkLabel(
            self.window,
            text="""Everything is ready! Click the 'Activate' button below to complete the activation
process and start using Bank With High Functionalities.""",
            font=("Segoe UI", 13),
            bg_color="black",
            height=0,
            width=0,
            justify="left",
            text_color="#00FF00",
        ).place(x=20, y=170)

        self.next_and_activate__button.configure(
            text="Activate",
            command=self._activate_and_proceed,
        )

    def _activate_and_proceed(self) -> None:

        for widget in self.window.winfo_children():

            if isinstance(widget, customtkinter.CTkLabel):
                widget.destroy()
        else:
            self.next_and_activate__button.destroy()

        try:

            CONFIGURATION_JSON["is_activated"] = True
            saved = utils.save_configuration_json(CONFIGURATION_JSON)

            if saved:

                customtkinter.CTkLabel(
                    self.window,
                    text="Activation successful!",
                    font=("Segoe UI", 21),
                    bg_color="black",
                    height=0,
                    width=0,
                    pady=20,
                    justify="left",
                    text_color="#00FF00",
                ).place(x=20, y=0)

                customtkinter.CTkLabel(
                    self.window,
                    text="""Thank you for activating Bank With High Functionalities!

Your support plays an important role in helping us enhance features, improve performance,
and deliver a smoother and more reliable experience. This project is continuously evolving,
with a focus on usability, efficiency, and meaningful functionality for users like you.

If you have any questions, feedback, or need assistance at any point, feel free to reach out
through GitHub Discussions. Your input helps shape future updates and improvements,
and we are always open to suggestions that make the project better.
""",
                    font=("Segoe UI", 12),
                    bg_color="black",
                    height=0,
                    width=0,
                    justify="left",
                ).place(x=20, y=74)

            else:

                customtkinter.CTkLabel(
                    self.window,
                    text="Activation failed!",
                    font=("Segoe UI", 21),
                    bg_color="black",
                    height=0,
                    width=0,
                    pady=20,
                    justify="left",
                    text_color="#FF0000",
                ).place(x=20, y=0)

                customtkinter.CTkLabel(
                    self.window,
                    text="""We encountered an issue while attempting to save your activation status. This may be due to a
temporary system interruption or an unexpected internal error.

What you can try:

• Restart the application and attempt activation again.

Need help?
Please contact support through our GitHub Issues page, where you can report the issue and
receive guidance from the community. We apologize for any inconvenience caused and
appreciate your patience.
""",
                    font=("Segoe UI", 11),
                    bg_color="black",
                    height=0,
                    width=0,
                    justify="left",
                ).place(x=20, y=74)

                customtkinter.CTkButton(
                    self.window,
                    text="Report Issue",
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
                        CONSTANTS["github"]["issues"]
                    ),
                ).place(x=298, y=234)

        except Exception as e:
            raise NotImplementedError

        self.cancel_and_close__button.configure(
            text="Close",
            fg_color=self.__raw_accent_color,
            hover_color=self.__hvr_accent_color,
        )
