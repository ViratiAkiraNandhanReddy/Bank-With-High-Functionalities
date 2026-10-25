lazy from datetime import UTC, datetime

lazy from CaesarCipher import Encryption

lazy from ..__base__ import AdminAuthenticationBase, UserAuthenticationBase
lazy from ._connection import DATA, find_user, save


class UserAuthentication(UserAuthenticationBase):
    @classmethod
    def password(cls, username_or_uuid: str, password: str) -> bool:

        user = find_user(username_or_uuid)
        return (
            user is not None
            and user.get("PASSWORD")
            == Encryption(password, shift=8, alterNumbers=True).encrypt()
        )

    @classmethod
    def backup_code(cls, username_or_uuid: str, backup_code: str) -> bool:

        user = find_user(username_or_uuid)
        return user is not None and user.get("BACKUP_CODE") == backup_code

    @classmethod
    def email_address(cls, username_or_uuid: str, email_address: str) -> bool:

        user = find_user(username_or_uuid)
        return user is not None and user.get("EMAIL") == email_address

    @classmethod
    def update_last_login(cls, username_or_uuid: str) -> None:

        user = find_user(username_or_uuid)
        if user is not None:
            user["LAST_LOGIN"] = datetime.now(UTC).isoformat()
            save()


class AdminAuthentication(AdminAuthenticationBase):
    @classmethod
    def password(cls, username: str, password: str) -> bool:

        admin = next(
            (row for row in DATA.get("ADMINS", []) if row.get("USERNAME") == username),
            None,
        )
        return (
            admin is not None
            and admin.get("PASSWORD")
            == Encryption(password, shift=53, alterNumbers=True).encrypt()
        )

    @classmethod
    def backup_code(cls, username: str, backup_code: str) -> bool:

        admin = next(
            (row for row in DATA.get("ADMINS", []) if row.get("USERNAME") == username),
            None,
        )
        return admin is not None and admin.get("BACKUP_CODE") == backup_code

    @classmethod
    def email_address(cls, username: str, email_address: str) -> bool:

        admin = next(
            (row for row in DATA.get("ADMINS", []) if row.get("USERNAME") == username),
            None,
        )
        return admin is not None and admin.get("EMAIL") == email_address
