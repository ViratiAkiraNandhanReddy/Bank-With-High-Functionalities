lazy import mysql.connector
lazy from uuid import uuid4
lazy from CaesarCipher import Encryption

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
                VALUES (%s, %s, %s, %s, %s, %s)
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
        except mysql.connector.Error:
            connection.rollback()
            return False

    @classmethod
    def deposit(cls, username_or_uuid: str, amount: float) -> bool:

        user_uuid = UserLookup.resolve_uuid(username_or_uuid)
        if user_uuid is None:
            return False

        cursor.execute("SELECT 1 FROM USERS WHERE UUID = %s", (user_uuid,))
        if cursor.fetchone() is None:
            return False
        try:
            cursor.execute(
                "UPDATE USERS SET BALANCE = BALANCE + %s WHERE UUID = %s",
                (amount, user_uuid),
            )
            cursor.execute(
                """
                INSERT INTO TRANSACTIONS (
                    USER_UUID, COUNTERPARTY_USERNAME, AMOUNT, TRANSACTION_TYPE
                )
                VALUES (%s, %s, %s, %s)
                """,
                (user_uuid, username_or_uuid, amount, "deposit"),
            )
            connection.commit()
        except mysql.connector.Error:
            connection.rollback()
            raise
        return True

    @classmethod
    def withdraw(cls, username_or_uuid: str, amount: float) -> bool:

        user_uuid = UserLookup.resolve_uuid(username_or_uuid)
        if user_uuid is None:
            return False

        cursor.execute("SELECT 1 FROM USERS WHERE UUID = %s", (user_uuid,))
        if cursor.fetchone() is None:
            return False
        try:
            cursor.execute(
                "UPDATE USERS SET BALANCE = BALANCE - %s WHERE UUID = %s",
                (amount, user_uuid),
            )
            cursor.execute(
                """
                INSERT INTO TRANSACTIONS (
                    USER_UUID, COUNTERPARTY_USERNAME, AMOUNT, TRANSACTION_TYPE
                )
                VALUES (%s, %s, %s, %s)
                """,
                (user_uuid, username_or_uuid, amount, "withdraw"),
            )
            connection.commit()
        except mysql.connector.Error:
            connection.rollback()
            raise
        return True

    @classmethod
    def transfer(
        cls, username_or_uuid: str, recipient_username: str, amount: float
    ) -> bool:

        user_uuid = UserLookup.resolve_uuid(username_or_uuid)
        recipient_uuid = UserLookup.resolve_uuid(recipient_username)
        if user_uuid is None or recipient_uuid is None:
            return False

        try:
            cursor.execute("SELECT 1 FROM USERS WHERE UUID = %s", (user_uuid,))
            if cursor.fetchone() is None:
                return False
            cursor.execute("SELECT 1 FROM USERS WHERE UUID = %s", (recipient_uuid,))
            if cursor.fetchone() is None:
                return False
            cursor.execute(
                "UPDATE USERS SET BALANCE = BALANCE - %s WHERE UUID = %s",
                (amount, user_uuid),
            )
            cursor.execute(
                "UPDATE USERS SET BALANCE = BALANCE + %s WHERE UUID = %s",
                (amount, recipient_uuid),
            )
            cursor.execute(
                """
                INSERT INTO TRANSACTIONS (
                    USER_UUID, COUNTERPARTY_USERNAME, AMOUNT, TRANSACTION_TYPE
                )
                VALUES (%s, %s, %s, %s)
                """,
                (user_uuid, recipient_username, amount, "transfer_out"),
            )
            cursor.execute(
                """
                INSERT INTO TRANSACTIONS (
                    USER_UUID, COUNTERPARTY_USERNAME, AMOUNT, TRANSACTION_TYPE
                )
                VALUES (%s, %s, %s, %s)
                """,
                (recipient_uuid, username_or_uuid, amount, "transfer_in"),
            )
            connection.commit()
            return True
        except mysql.connector.Error:
            connection.rollback()
            raise

    @classmethod
    def change_password(cls, username_or_uuid: str, new_password: str) -> bool:

        cursor.execute(
            "SELECT 1 FROM USERS WHERE USERNAME = %s OR UUID = %s",
            (username_or_uuid, username_or_uuid),
        )
        if cursor.fetchone() is None:
            return False
        password = Encryption(new_password, shift=8, alterNumbers=True).encrypt()
        cursor.execute(
            """
            UPDATE USERS SET PASSWORD = %s
            WHERE USERNAME = %s OR UUID = %s
            """,
            (password, username_or_uuid, username_or_uuid),
        )
        connection.commit()
        return True

    @classmethod
    def change_username(cls, old_username_or_uuid: str, new_username: str) -> bool:

        cursor.execute(
            "SELECT 1 FROM USERS WHERE USERNAME = %s OR UUID = %s",
            (old_username_or_uuid, old_username_or_uuid),
        )
        if cursor.fetchone() is None:
            return False
        cursor.execute(
            """
            UPDATE USERS SET USERNAME = %s
            WHERE USERNAME = %s OR UUID = %s
            """,
            (new_username, old_username_or_uuid, old_username_or_uuid),
        )
        connection.commit()
        return True

    @classmethod
    def delete(cls, username_or_uuid: str) -> bool:

        cursor.execute(
            "DELETE FROM USERS WHERE USERNAME = %s OR UUID = %s",
            (username_or_uuid, username_or_uuid),
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
                VALUES (%s, %s, %s, %s)
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
        except mysql.connector.Error:
            connection.rollback()
            return False

    @classmethod
    def change_password(cls, username: str, new_password: str) -> bool:

        cursor.execute("SELECT 1 FROM ADMINS WHERE USERNAME = %s", (username,))
        if cursor.fetchone() is None:
            return False
        password = Encryption(new_password, shift=53, alterNumbers=True).encrypt()
        cursor.execute(
            "UPDATE ADMINS SET PASSWORD = %s WHERE USERNAME = %s",
            (password, username),
        )
        connection.commit()
        return True


class ApplicationManagement(ApplicationManagementBase):
    @classmethod
    def update_announcement(cls, announcement: str = "No new announcements.") -> bool:

        cursor.execute("SELECT 1 FROM ANNOUNCEMENT WHERE ANNOUNCEMENT_ID = 1")
        if cursor.fetchone() is None:
            return False
        cursor.execute(
            """
            UPDATE ANNOUNCEMENT
            SET CONTENT = %s, UPDATED_AT = CURRENT_TIMESTAMP
            WHERE ANNOUNCEMENT_ID = 1
            """,
            (announcement,),
        )
        connection.commit()
        return True


class SecurityEventManagement(SecurityEventManagementBase):
    @classmethod
    def record(cls, username_or_uuid: str, event_type: str) -> bool:

        user_uuid = UserLookup.resolve_uuid(username_or_uuid)
        if user_uuid is None:
            return False
        cursor.execute(
            "INSERT INTO SECURITY_EVENTS (USER_UUID, EVENT_TYPE) VALUES (%s, %s)",
            (user_uuid, event_type),
        )
        connection.commit()
        return cursor.rowcount > 0
