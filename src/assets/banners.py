from PIL import Image
from ..utils import root


class banners:

    reset_pwd_sidebar_bg: Image.Image = Image.open(
        root / "assets" / "banners" / "Jreset-pwd-sidebar-bg-banner.jpg"
    )

    signin_sidebar_bg: Image.Image = Image.open(
        root / "assets" / "banners" / "signin-sidebar-bg-banner.jpg"
    )
