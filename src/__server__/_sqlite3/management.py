lazy from CaesarCipher import Encryption
lazy from uuid import uuid4

lazy from ..__base__ import (
    AdminManagementBase,
    ApplicationManagementBase,
    SecurityEventManagementBase,
    UserManagementBase,
)
lazy from ._connection import connection
lazy from .lookup import UserLookup

cursor = connection.cursor()


class UserManagement(UserManagementBase):

    @classmethod
    def create(
        cls,
        username: str,
        password: str,
        full_name: str,
        email: str = "",
    ) -> bool:

        try:
            cursor.execute(
                """
                INSERT INTO USERS (
                    UUID, USERNAME, PASSWORD, EMAIL, BACKUP_CODE, FULL_NAME
                )
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    str(uuid4()),
                    username,
                    Encryption(password, shift=8, alterNumbers=True).encrypt(),
                    email or None,
                    str(uuid4()),
                    full_name,
                ),
            )
            connection.commit()
            return True
        except Exception:
            connection.rollback()
            return False

    @classmethod
    def deposit(
        cls,
        username_or_uuid: str,
        amount: float,
    ) -> bool:

        user_uuid = UserLookup.resolve_uuid(username_or_uuid)
        if user_uuid is None or amount <= 0:
            return False

        cursor.execute(
            """
            UPDATE USERS
            SET BALANCE = BALANCE + ?
            WHERE UUID = ?
            """,
            (
                amount,
                user_uuid,
            ),
        )
        if cursor.rowcount == 0:
            connection.rollback()
            return False

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
            (
                user_uuid,
                username_or_uuid,
                amount,
                "deposit",
            ),
        )

        connection.commit()

        return cursor.rowcount > 0

    @classmethod
    def withdraw(
        cls,
        username_or_uuid: str,
        amount: float,
    ) -> bool:

        user_uuid = UserLookup.resolve_uuid(username_or_uuid)
        if user_uuid is None or amount <= 0:
            return False

        cursor.execute(
            """
            UPDATE USERS
            SET BALANCE = BALANCE - ?
            WHERE UUID = ? AND BALANCE >= ?
            """,
            (
                amount,
                user_uuid,
                amount,
            ),
        )
        if cursor.rowcount == 0:
            connection.rollback()
            return False

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
            (
                user_uuid,
                username_or_uuid,
                amount,
                "withdraw",
            ),
        )

        connection.commit()

        return cursor.rowcount > 0

    @classmethod
    def transfer(
        cls,
        username_or_uuid: str,
        recipient_username: str,
        amount: float,
    ) -> bool:

        try:

            user_uuid = UserLookup.resolve_uuid(username_or_uuid)

            recipient_uuid = UserLookup.resolve_uuid(recipient_username)
            if (
                user_uuid is None
                or recipient_uuid is None
                or user_uuid == recipient_uuid
                or amount <= 0
            ):
                return False

            cursor.execute(
                """
                UPDATE USERS
                SET BALANCE = BALANCE - ?
                WHERE UUID = ? AND BALANCE >= ?
                """,
                (
                    amount,
                    user_uuid,
                    amount,
                ),
            )
            if cursor.rowcount == 0:
                connection.rollback()
                return False

            cursor.execute(
                """
                UPDATE USERS
                SET BALANCE = BALANCE + ?
                WHERE UUID = ?
                """,
                (
                    amount,
                    recipient_uuid,
                ),
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
                (
                    user_uuid,
                    recipient_username,
                    amount,
                    "transfer_out",
                ),
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
                (
                    recipient_uuid,
                    username_or_uuid,
                    amount,
                    "transfer_in",
                ),
            )

            connection.commit()

            return True

        except Exception:

            connection.rollback()

            return False

    @classmethod
    def change_password(
        cls,
        username_or_uuid: str,
        new_password: str,
    ) -> bool:

        password: str = Encryption(
            new_password,
            shift=8,
            alterNumbers=True,
        ).encrypt()

        cursor.execute(
            """
            UPDATE USERS
            SET PASSWORD = ?
            WHERE USERNAME = ? OR UUID = ?
            """,
            (
                password,
                username_or_uuid,
                username_or_uuid,
            ),
        )

        connection.commit()

        return cursor.rowcount > 0

    @classmethod
    def change_username(
        cls,
        old_username_or_uuid: str,
        new_username: str,
    ) -> bool:

        cursor.execute(
            """
            UPDATE USERS
            SET USERNAME = ?
            WHERE USERNAME = ? OR UUID = ?
            """,
            (
                new_username,
                old_username_or_uuid,
                old_username_or_uuid,
            ),
        )

        connection.commit()

        return cursor.rowcount > 0

    @classmethod
    def delete(
        cls,
        username_or_uuid: str,
    ) -> bool:

        cursor.execute(
            """
            DELETE FROM USERS
            WHERE USERNAME = ? OR UUID = ?
            """,
            (
                username_or_uuid,
                username_or_uuid,
            ),
        )
        connection.commit()

        return cursor.rowcount > 0


class AdminManagement(AdminManagementBase):

    @classmethod
    def create(
        cls,
        username: str,
        password: str,
        email: str = "",
    ) -> bool:

        try:
            cursor.execute(
                """
                INSERT INTO ADMINS (USERNAME, PASSWORD, EMAIL, BACKUP_CODE)
                VALUES (?, ?, ?, ?)
                """,
                (
                    username,
                    Encryption(password, shift=53, alterNumbers=True).encrypt(),
                    email or None,
                    str(uuid4()),
                ),
            )
            connection.commit()
            return True
        except Exception:
            connection.rollback()
            return False

    @classmethod
    def change_password(
        cls,
        username: str,
        new_password: str,
    ) -> bool:

        password: str = Encryption(
            new_password,
            shift=53,
            alterNumbers=True,
        ).encrypt()

        cursor.execute(
            """
            UPDATE ADMINS
            SET PASSWORD = ?
            WHERE USERNAME = ?
            """,
            (
                password,
                username,
            ),
        )

        connection.commit()

        return cursor.rowcount > 0


class ApplicationManagement(ApplicationManagementBase):

    @classmethod
    def update_announcement(
        cls,
        announcement: str = "No new announcements.",
    ) -> bool:

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


class SecurityEventManagement(SecurityEventManagementBase):

    @classmethod
    def record(
        cls,
        username_or_uuid: str,
        event_type: str,
    ) -> bool:

        user_uuid = UserLookup.resolve_uuid(username_or_uuid)

        cursor.execute(
            """
            INSERT INTO SECURITY_EVENTS (
                USER_UUID,
                EVENT_TYPE
            )
            VALUES (?, ?)
            """,
            (
                user_uuid,
                event_type,
            ),
        )

        connection.commit()

        return cursor.rowcount > 0
