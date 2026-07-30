from ._connection import connection
from CaesarCipher import Encryption
from ..__base__ import (
    UserManagementBase,
    AdminManagementBase,
    ApplicationManagementBase,
)

cursor = connection.cursor()


class UserManagement(UserManagementBase):

    @classmethod
    def change_password(cls, username_or_uuid: str, new_password: str) -> bool:

        password: str = Encryption(new_password, shift=8, alterNumbers=True).encrypt()

        cursor.execute(
            """
            UPDATE USERS
            SET PASSWORD = ?
            WHERE USERNAME = ? OR UUID = ?
            """,
            (password, username_or_uuid, username_or_uuid),
        )

        connection.commit()

        return cursor.rowcount > 0

    @classmethod
    def change_username(cls, old_username_or_uuid: str, new_username: str) -> bool:

        cursor.execute(
            """
            UPDATE USERS
            SET USERNAME = ?
            WHERE USERNAME = ? OR UUID = ?
            """,
            (new_username, old_username_or_uuid, old_username_or_uuid),
        )

        connection.commit()

        return cursor.rowcount > 0

    @classmethod
    def delete(cls, username_or_uuid: str) -> bool:

        cursor.execute(
            """
            DELETE FROM USERS
            WHERE USERNAME = ? OR UUID = ?
            """,
            (username_or_uuid, username_or_uuid),
        )
        connection.commit()

        return cursor.rowcount > 0


class AdminManagement(AdminManagementBase):

    @classmethod
    def change_password(cls, username: str, new_password: str) -> bool:

        password: str = Encryption(new_password, shift=53, alterNumbers=True).encrypt()

        cursor.execute(
            """
            UPDATE ADMINS
            SET PASSWORD = ?
            WHERE USERNAME = ?
            """,
            (password, username),
        )

        connection.commit()

        return cursor.rowcount > 0


class ApplicationManagement(ApplicationManagementBase):

    @classmethod
    def update_notice(cls, notice: str) -> bool:

        cursor.execute(
            """
            UPDATE NOTICES
            SET
                CONTENT = ?,
                UPDATED_AT = CURRENT_TIMESTAMP
            WHERE NOTICE_ID = 1
            """,
            (notice,),
        )

        connection.commit()

        return cursor.rowcount > 0

    @classmethod
    def remove_notice(cls) -> bool:

        cursor.execute("""
            UPDATE NOTICES
            SET
                CONTENT = 'no new notices',
                UPDATED_AT = CURRENT_TIMESTAMP
            WHERE NOTICE_ID = 1
            """)

        connection.commit()

        return cursor.rowcount > 0
