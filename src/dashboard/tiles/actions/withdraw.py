from ..balance import balance
from ..transactions import transactions
from .... import customtkinter, assets, Callable, SERVER


class withdraw:

    def __init__(
        self,
        parent_frame: customtkinter.CTkFrame,
        balance_instance: balance,
        transactions_instance: transactions,
    ) -> None:

        self.frame__withdraw: customtkinter.CTkFrame = customtkinter.CTkFrame(
            parent_frame,
            width=350,
            height=390,
            fg_color="#0a0a0a",
            background_corner_colors=(
                "#000000",
                "#000000",
                "#000000",
                "#000000",
            ),  # type: ignore[arg-type]
        )

        self.show_frame: Callable = lambda: self.frame__withdraw.place(x=0, y=0)

        self.hide_frame: Callable = lambda: self.frame__withdraw.place_forget()
