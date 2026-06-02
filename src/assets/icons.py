from PIL import Image
from ..utils import root


class icons:

    class material:

        account_circle: Image.Image = Image.open(
            root / "assets" / "icons" / "material-icons" / "account_circle.png"
        )

        arrow_back: Image.Image = Image.open(
            root / "assets" / "icons" / "material-icons" / "arrow_back.png"
        )

        arrow_forward: Image.Image = Image.open(
            root / "assets" / "icons" / "material-icons" / "arrow_forward.png"
        )

        assured_workload: Image.Image = Image.open(
            root / "assets" / "icons" / "material-icons" / "assured_workload.png"
        )

        chevron_backward: Image.Image = Image.open(
            root / "assets" / "icons" / "material-icons" / "chevron_backward.png"
        )

        chevron_forward: Image.Image = Image.open(
            root / "assets" / "icons" / "material-icons" / "chevron_forward.png"
        )

        close: Image.Image = Image.open(
            root / "assets" / "icons" / "material-icons" / "close.png"
        )

        developer_mode_tv: Image.Image = Image.open(
            root / "assets" / "icons" / "material-icons" / "developer_mode_tv.png"
        )

        exit_to_app: Image.Image = Image.open(
            root / "assets" / "icons" / "material-icons" / "exit_to_app.png"
        )

        lock_person: Image.Image = Image.open(
            root / "assets" / "icons" / "material-icons" / "lock_person.png"
        )

        mail: Image.Image = Image.open(
            root / "assets" / "icons" / "material-icons" / "mail.png"
        )

        manage_accounts: Image.Image = Image.open(
            root / "assets" / "icons" / "material-icons" / "manage_accounts.png"
        )

        more_horiz: Image.Image = Image.open(
            root / "assets" / "icons" / "material-icons" / "more_horiz.png"
        )

        overview: Image.Image = Image.open(
            root / "assets" / "icons" / "material-icons" / "overview.png"
        )

        password: Image.Image = Image.open(
            root / "assets" / "icons" / "material-icons" / "password.png"
        )

        remove: Image.Image = Image.open(
            root / "assets" / "icons" / "material-icons" / "remove.png"
        )

        security: Image.Image = Image.open(
            root / "assets" / "icons" / "material-icons" / "security.png"
        )

        shield_lock: Image.Image = Image.open(
            root / "assets" / "icons" / "material-icons" / "shield_lock.png"
        )

        wifi_off: Image.Image = Image.open(
            root / "assets" / "icons" / "material-icons" / "wifi_off.png"
        )

    class platform:

        github: Image.Image = Image.open(
            root / "assets" / "icons" / "platform-logos" / "github.png"
        )
