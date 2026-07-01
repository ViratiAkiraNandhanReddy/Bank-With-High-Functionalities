from .._uuids import _uuids
from ._connection import connection
from CaesarCipher import Encryption
from ..__base__ import UserAuthenticationBase, AdminAuthenticationBase

cursor = connection.cursor()


class UserAuthentication(UserAuthenticationBase):

    @classmethod
    def password(cls, username_or_uuid: str, password: str) -> bool:

        if _uuids.validate_uuid5(username_or_uuid):

            cursor.execute(
                """
                SELECT password FROM users WHERE uuid = ?
                """,
                (username_or_uuid,),
            )

            return (
                cursor.fetchone()[0]
                == Encryption(password, shift=8, alterNumbers=True).encrypt()
            )

        cursor.execute(
            """
            SELECT password FROM users WHERE username = ?
            """,
            (username_or_uuid,),
        )

        return (
            cursor.fetchone()[0]
            == Encryption(password, shift=8, alterNumbers=True).encrypt()
        )

    @classmethod
    def backup_code(cls, username_or_uuid: str, backup_code: str) -> bool:

        cursor.execute(
            """
                SELECT backup_code FROM users WHERE username = ?
                """,
            (username_or_uuid,),
        )

        return cursor.fetchone()[0] == backup_code

    @classmethod
    def email_address(cls, username_or_uuid: str, email_address: str) -> bool:

        cursor.execute(
            """
            SELECT email FROM users WHERE username = ?
            """,
            (username_or_uuid,),
        )

        return cursor.fetchone()[0] == email_address


class AdminAuthentication(AdminAuthenticationBase):

    @classmethod
    def password(cls, username: str, password: str) -> bool:

        cursor.execute(
            """
            SELECT password FROM ADMINS WHERE username = ?
            """,
            (username,),
        )

        return (
            cursor.fetchone()[0]
            == Encryption(password, shift=53, alterNumbers=True).encrypt()
        )

    @classmethod
    def backup_code(cls, username: str, backup_code: str) -> bool:

        cursor.execute(
            """
                SELECT backup_code FROM ADMINS WHERE username = ?
                """,
            (username,),
        )

        return cursor.fetchone()[0] == backup_code

    @classmethod
    def email_address(cls, username: str, email_address: str) -> bool:

        cursor.execute(
            """
            SELECT email FROM ADMINS WHERE username = ?
            """,
            (username,),
        )

        return cursor.fetchone()[0] == email_address
