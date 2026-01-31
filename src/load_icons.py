import os
from PIL import Image

DIR_PATH: str = str(os.environ.get("LOCALAPPDATA")) + r"\Bank-With-High-Functionalities"

# --- common --- #

icon__close = Image.open(rf"{DIR_PATH}\assets\icons\material icons\close.png")

# --- login.py --- #

icon__password = Image.open(rf"{DIR_PATH}\assets\icons\material icons\password.png")
icon__security = Image.open(rf"{DIR_PATH}\assets\icons\material icons\security.png")
icon__account_circle = Image.open(
    rf"{DIR_PATH}\assets\icons\material icons\account_circle.png"
)

# --- administrator.py --- #

icon__developer_mode_tv = Image.open(
    rf"{DIR_PATH}\assets\icons\material icons\developer_mode_tv.png"
)
