import os
from PIL import Image

DIR_PATH: str = str(os.environ.get("LOCALAPPDATA")) + r"\Bank-With-High-Functionalities"

image__banner_sign_in = Image.open(
    rf"{DIR_PATH}\assets\banners\signin-sidebar-bg-banner.jpg"
)

image__banner_reset_password = Image.open(
    rf"{DIR_PATH}\assets\banners\reset-pwd-sidebar-bg-banner.jpg"
)
