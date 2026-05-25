import os
from PIL import Image

DIR_PATH: str = str(os.environ.get("LOCALAPPDATA")) + r"\Bank-With-High-Functionalities"

# --- common --- #

icon__close = Image.open(rf"{DIR_PATH}\assets\icons\material-icons\close.png")

icon__more_horiz = Image.open(rf"{DIR_PATH}\assets\icons\material-icons\more_horiz.png")

icon__exit_to_app = Image.open(
    rf"{DIR_PATH}\assets\icons\material-icons\exit_to_app.png"
)

icon__lock_person = Image.open(
    rf"{DIR_PATH}\assets\icons\material-icons\lock_person.png"
)

icon__arrow_back = Image.open(rf"{DIR_PATH}\assets\icons\material-icons\arrow_back.png")

icon__arrow_forward = Image.open(
    rf"{DIR_PATH}\assets\icons\material-icons\arrow_forward.png"
)

icon__chevron_forward = Image.open(
    rf"{DIR_PATH}\assets\icons\material-icons\chevron_forward.png"
)

icon__wifi_off = Image.open(rf"{DIR_PATH}\assets\icons\material-icons\wifi_off.png")

# --- platform --- #

icon__platform_github = Image.open(
    rf"{DIR_PATH}\assets\icons\platform-logos\github.png"
)

# --- sign-in --- #

icon__password = Image.open(rf"{DIR_PATH}\assets\icons\material-icons\password.png")

icon__security = Image.open(rf"{DIR_PATH}\assets\icons\material-icons\security.png")

icon__account_circle = Image.open(
    rf"{DIR_PATH}\assets\icons\material-icons\account_circle.png"
)

icon__assured_workload = Image.open(
    rf"{DIR_PATH}\assets\icons\material-icons\assured_workload.png"
)

icon__manage_accounts = Image.open(
    rf"{DIR_PATH}\assets\icons\material-icons\manage_accounts.png"
)

icon__shield_lock = Image.open(
    rf"{DIR_PATH}\assets\icons\material-icons\shield_lock.png"
)

# --- administrator --- #

icon__developer_mode_tv = Image.open(
    rf"{DIR_PATH}\assets\icons\material-icons\developer_mode_tv.png"
)


image__banner_sign_in = Image.open(
    rf"{DIR_PATH}\assets\banners\signin-sidebar-bg-banner.jpg"
)

image__banner_reset_password = Image.open(
    rf"{DIR_PATH}\assets\banners\reset-pwd-sidebar-bg-banner.jpg"
)
