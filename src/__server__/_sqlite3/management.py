from .lookup import UserLookup
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
    def deposit(cls, username_or_uuid: str, amount: float) -> bool:

        user_uuid = UserLookup.resolve_uuid(username_or_uuid)

        cursor.execute(
            """
            UPDATE USERS
            SET BALANCE = BALANCE + ?
            WHERE UUID = ?
            """,
            (amount, user_uuid),
        )

        cursor.execute(
            """
            INSERT INTO TRANSACTIONS (
                USER_UUID,
                COUNTERPARTY_USERNAME,
                AMOUNT,
                TRANSACTION_TYPE
            )
            VALUES (?, ?, ?, ?)
            """,
            (user_uuid, username_or_uuid, amount, "deposit"),
        )

        connection.commit()

        return cursor.rowcount > 0

    @classmethod
    def withdraw(cls, username_or_uuid: str, amount: float) -> bool:

        user_uuid = UserLookup.resolve_uuid(username_or_uuid)

        cursor.execute(
            """
            UPDATE USERS
            SET BALANCE = BALANCE - ?
            WHERE UUID = ?
            """,
            (amount, user_uuid),
        )

        cursor.execute(
            """
            INSERT INTO TRANSACTIONS (
                USER_UUID,
                COUNTERPARTY_USERNAME,
                AMOUNT,
                TRANSACTION_TYPE
            )
            VALUES (?, ?, ?, ?)
            """,
            (user_uuid, username_or_uuid, amount, "withdraw"),
        )

        connection.commit()

        return cursor.rowcount > 0

    @classmethod
    def transfer(
        cls, username_or_uuid: str, recipient_username: str, amount: float
    ) -> bool:

        try:

            user_uuid = UserLookup.resolve_uuid(username_or_uuid)

            recipient_uuid = UserLookup.resolve_uuid(recipient_username)

            cursor.execute(
                """
                UPDATE USERS
                SET BALANCE = BALANCE - ?
                WHERE UUID = ?
                """,
                (amount, user_uuid),
            )

            cursor.execute(
                """
                UPDATE USERS
                SET BALANCE = BALANCE + ?
                WHERE UUID = ?
                """,
                (amount, recipient_uuid),
            )

            cursor.execute(
                """
                INSERT INTO TRANSACTIONS (
                    USER_UUID,
                    COUNTERPARTY_USERNAME,
                    AMOUNT,
                    TRANSACTION_TYPE
                )
                VALUES (?, ?, ?, ?)
                """,
                (user_uuid, recipient_username, amount, "transfer_out"),
            )

            cursor.execute(
                """
                INSERT INTO TRANSACTIONS (
                    USER_UUID,
                    COUNTERPARTY_USERNAME,
                    AMOUNT,
                    TRANSACTION_TYPE
                )
                VALUES (?, ?, ?, ?)
                """,
                (recipient_uuid, username_or_uuid, amount, "transfer_in"),
            )

            connection.commit()

            return True

        except Exception:

            connection.rollback()

            return False

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
    def update_announcement(cls, announcement: str = "No new announcements.") -> bool:

        cursor.execute(
            """
            UPDATE ANNOUNCEMENT
            SET
                CONTENT = ?,
                UPDATED_AT = CURRENT_TIMESTAMP
            WHERE ANNOUNCEMENT_ID = 1
            """,
            (announcement,),
        )

        connection.commit()

        return cursor.rowcount > 0
