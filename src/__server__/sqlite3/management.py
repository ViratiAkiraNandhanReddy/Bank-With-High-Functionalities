from ... import _uuids
from ._connection import connection
from CaesarCipher import Encryption
from ..__base__ import UserManagementBase, AdminManagementBase

cursor = connection.cursor()


class UserManagement(UserManagementBase):

    @classmethod
    def change_password(cls, username_or_uuid: str, new_password: str) -> bool:

        password: str = Encryption(new_password, shift=8, alterNumbers=True).encrypt()

        cursor.execute(
            """
                UPDATE users SET password = ? WHERE username = ?
                """,
            (password, username_or_uuid),
        )

        connection.commit()

        return cursor.rowcount > 0

    @classmethod
    def change_username(cls, old_username_or_uuid: str, new_username: str) -> bool:

        cursor.execute(
            """
                UPDATE users SET username = ? WHERE username = ?
                """,
            (new_username, old_username_or_uuid),
        )

        connection.commit()

        return cursor.rowcount > 0

    @classmethod
    def delete(cls, username_or_uuid: str, password: str) -> bool: ...


class AdminManagement(AdminManagementBase):

    @classmethod
    def change_password(cls, username: str, new_password: str) -> bool:

        password: str = Encryption(new_password, shift=53, alterNumbers=True).encrypt()

        cursor.execute(
            """
                UPDATE admins SET password = ? WHERE username = ?
                """,
            (password, username),
        )

        connection.commit()

        return cursor.rowcount > 0
