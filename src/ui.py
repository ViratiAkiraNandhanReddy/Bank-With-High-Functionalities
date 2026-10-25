lazy import customtkinter
lazy from typing import Callable

COLORS: dict[str, str] = {
    "surface": "#0A0A0A",
    "card": "#111111",
    "card_hover": "#1A1A1A",
    "border": "#FFFFFF",
    "muted": "#A3A3A3",
    "text": "#FFFFFF",
    "info": "#218CFF",
    "success": "#22C55E",
    "warning": "#F59E0B",
    "danger": "#EF4444",
}


def section_title(
    parent: customtkinter.CTkBaseClass,
    text: str,
    x: int = 35,
    y: int = 30,
    size: int = 24,
) -> customtkinter.CTkLabel:

    label = customtkinter.CTkLabel(
        parent,
        text=text,
        font=("Segoe UI", size, "bold"),
        text_color=COLORS["text"],
        anchor="w",
    )
    label.place(x=x, y=y)
    return label


def status_label(
    parent: customtkinter.CTkBaseClass,
    x: int = 35,
    y: int = 0,
) -> customtkinter.CTkLabel:

    label = customtkinter.CTkLabel(
        parent,
        text="",
        font=("Segoe UI", 13),
        text_color=COLORS["muted"],
        anchor="w",
    )
    label.place(x=x, y=y)
    return label


def set_status(
    label: customtkinter.CTkLabel,
    message: str,
    kind: str = "info",
) -> None:

    label.configure(
        text=message,
        text_color=COLORS.get(kind, COLORS["muted"]),
    )


def entry_field(
    parent: customtkinter.CTkBaseClass,
    placeholder: str,
    x: int,
    y: int,
    width: int = 360,
    show: str | None = None,
) -> tuple[customtkinter.CTkFrame, customtkinter.CTkEntry]:

    container = customtkinter.CTkFrame(
        parent,
        width=width,
        height=42,
        fg_color="transparent",
        border_width=1,
        border_color=COLORS["border"],
        corner_radius=6,
    )
    container.place(x=x, y=y)

    entry = customtkinter.CTkEntry(
        container,
        width=width - 18,
        height=34,
        placeholder_text=placeholder,
        corner_radius=0,
        border_width=0,
        fg_color="transparent",
        font=("Consolas", 14),
        show=show,
    )
    entry.place(x=9, rely=0.5, anchor="w")

    def restore_border(_event: object) -> None:
        container.configure(border_color=COLORS["border"])

    entry.bind("<KeyPress>", restore_border)
    return container, entry


def metric_card(
    parent: customtkinter.CTkBaseClass,
    title: str,
    value: str,
    x: int,
    y: int,
    width: int = 180,
    color: str = "info",
    command: Callable | None = None,
) -> customtkinter.CTkFrame:

    card = customtkinter.CTkFrame(
        parent,
        width=width,
        height=112,
        fg_color=COLORS["card"],
        corner_radius=8,
    )
    card.place(x=x, y=y)

    customtkinter.CTkLabel(
        card,
        text=title,
        font=("Segoe UI", 12),
        text_color=COLORS["muted"],
        anchor="w",
    ).place(x=14, y=14)
    customtkinter.CTkLabel(
        card,
        text=value,
        font=("Consolas", 21, "bold"),
        text_color=COLORS.get(color, COLORS["info"]),
        anchor="w",
    ).place(x=14, y=47)

    if command is not None:
        button = customtkinter.CTkButton(
            card,
            text="Open",
            width=width - 28,
            height=24,
            fg_color="transparent",
            hover_color=COLORS["card_hover"],
            text_color=COLORS["muted"],
            font=("Segoe UI", 11),
            command=command,
        )
        button.place(x=14, y=80)

    return card


def action_tile(
    parent: customtkinter.CTkBaseClass,
    title: str,
    description: str,
    x: int,
    y: int,
    command: Callable | None = None,
    accent: str = "info",
    width: int = 250,
    height: int = 132,
) -> customtkinter.CTkFrame:

    accent_color = COLORS.get(accent, accent)
    tile = customtkinter.CTkFrame(
        parent,
        width=width,
        height=height,
        fg_color=COLORS["card"],
        border_width=1,
        border_color="#252525",
        corner_radius=8,
    )
    tile.place(x=x, y=y)

    customtkinter.CTkFrame(
        tile,
        width=5,
        height=height - 34,
        fg_color=accent_color,
        corner_radius=2,
    ).place(x=14, y=17)

    customtkinter.CTkLabel(
        tile,
        text=title,
        font=("Segoe UI", 16, "bold"),
        text_color=COLORS["text"],
        anchor="w",
    ).place(x=35, y=16)

    customtkinter.CTkLabel(
        tile,
        text=description,
        width=width - 55,
        font=("Segoe UI", 12),
        text_color=COLORS["muted"],
        justify="left",
        anchor="w",
        wraplength=width - 55,
    ).place(x=35, y=50)

    if command is not None:
        customtkinter.CTkButton(
            tile,
            text="Open",
            width=76,
            height=25,
            fg_color="transparent",
            hover_color=COLORS["card_hover"],
            text_color=accent_color,
            font=("Segoe UI", 11, "bold"),
            command=command,
        ).place(x=width - 92, y=height - 36)

    return tile


def empty_state(
    parent: customtkinter.CTkBaseClass,
    text: str,
) -> customtkinter.CTkLabel:

    label = customtkinter.CTkLabel(
        parent,
        text=text,
        font=("Segoe UI", 12),
        text_color=COLORS["muted"],
        justify="center",
    )
    label.place(relx=0.5, rely=0.5, anchor="center")
    return label


def add_password_toggle(
    parent: customtkinter.CTkBaseClass,
    entry: customtkinter.CTkEntry,
    x: int,
    y: int,
) -> customtkinter.CTkButton:

    state = {"visible": False}

    def toggle() -> None:
        state["visible"] = not state["visible"]
        entry.configure(show="" if state["visible"] else "•")
        button.configure(text="Hide" if state["visible"] else "Show")

    button = customtkinter.CTkButton(
        parent,
        text="Show",
        width=52,
        height=24,
        fg_color="transparent",
        hover_color=COLORS["card_hover"],
        text_color=COLORS["muted"],
        font=("Segoe UI", 10),
        command=toggle,
    )
    button.place(x=x, y=y)
    return button
