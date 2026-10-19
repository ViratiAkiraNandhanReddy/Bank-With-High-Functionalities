lazy from PIL import Image

lazy from ..utils import root


class banners:

    reset_pwd_sidebar_bg: Image.Image = Image.open(
        root / "assets" / "banners" / "reset-pwd-sidebar-bg-banner.jpg"
    )

    signin_sidebar_bg: Image.Image = Image.open(
        root / "assets" / "banners" / "signin-sidebar-bg-banner.jpg"
    )
