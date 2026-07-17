from ._connection import connection
from CaesarCipher import Encryption
from ..__base__ import UserAuthenticationBase, AdminAuthenticationBase

cursor = connection.cursor()


class UserAuthentication(UserAuthenticationBase):

    @classmethod
    def password(cls, username_or_uuid: str, password: str) -> bool:

        cursor.execute(
            """
            SELECT 
                PASSWORD
            FROM USERS
            WHERE USERNAME = ? OR UUID = ?
            """,
            (username_or_uuid, username_or_uuid),
        )

        return (
            cursor.fetchone()[0]
            == Encryption(password, shift=8, alterNumbers=True).encrypt()
        )

    @classmethod
    def backup_code(cls, username_or_uuid: str, backup_code: str) -> bool:

        cursor.execute(
            """
            SELECT
                BACKUP_CODE
            FROM USERS
            WHERE USERNAME = ? OR UUID = ?
            """,
            (username_or_uuid, username_or_uuid),
        )

        return cursor.fetchone()[0] == backup_code

    @classmethod
    def email_address(cls, username_or_uuid: str, email_address: str) -> bool:

        cursor.execute(
            """
            SELECT
                EMAIL
            FROM USERS
            WHERE USERNAME = ? OR UUID = ?
            """,
            (username_or_uuid, username_or_uuid),
        )

        return cursor.fetchone()[0] == email_address

    @classmethod
    def update_last_login(cls, username_or_uuid: str) -> None:

        cursor.execute(
            """
            UPDATE USERS
            SET LAST_LOGIN = CURRENT_TIMESTAMP
            WHERE USERNAME = ? OR UUID = ?
            """,
            (username_or_uuid, username_or_uuid),
        )

        connection.commit()


class AdminAuthentication(AdminAuthenticationBase):

    @classmethod
    def password(cls, username: str, password: str) -> bool:

        cursor.execute(
            """
            SELECT
                PASSWORD
            FROM ADMINS
            WHERE USERNAME = ?
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
            SELECT
                BACKUP_CODE
            FROM ADMINS
            WHERE USERNAME = ?
            """,
            (username,),
        )

        return cursor.fetchone()[0] == backup_code

    @classmethod
    def email_address(cls, username: str, email_address: str) -> bool:

        cursor.execute(
            """
            SELECT
                EMAIL
            FROM ADMINS
            WHERE USERNAME = ?
            """,
            (username,),
        )

        return cursor.fetchone()[0] == email_address
