from .._uuids import _uuids
from ._connection import connection
from datetime import datetime, timezone
from ..__base__ import UserLookupBase, AdminLookupBase

cursor = connection.cursor()


class UserLookup(UserLookupBase):

    @classmethod
    def exists(cls, username_or_uuid: str) -> bool:

        if _uuids.validate(username_or_uuid):

            cursor.execute(
                """
                SELECT 1 FROM USERS WHERE UUID = ?
                """,
                (username_or_uuid,),
            )

            return cursor.fetchone() is not None

        cursor.execute(
            """
            SELECT 1 FROM USERS WHERE USERNAME = ?
            """,
            (username_or_uuid,),
        )

        return cursor.fetchone() is not None

    @classmethod
    def balance(cls, username_or_uuid) -> float:

        if _uuids.validate(username_or_uuid):

            cursor.execute(
                """
                SELECT balance FROM USERS WHERE UUID = ?
                """,
                (username_or_uuid,),
            )

            row = cursor.fetchone()
            return row[0] if row is not None else 0.0

        cursor.execute(
            """
            SELECT balance FROM USERS WHERE USERNAME = ?
            """,
            (username_or_uuid,),
        )

        row = cursor.fetchone()
        return row[0] if row is not None else 0.0

    @classmethod
    def resolve_uuid(cls, username: str) -> str | None:

        if _uuids.validate(username):

            return username

        cursor.execute(
            """
            SELECT UUID FROM USERS WHERE USERNAME = ?
            """,
            (username,),
        )

        row = cursor.fetchone()
        return row[0] if row is not None else None

    @classmethod
    def transactions(
        cls, username_or_uuid: str, limit: int = 5
    ) -> list[tuple[str, str, float, str]]:
        """[(COUNTERPARTY_USERNAME, TRANSACTION_TYPE, AMOUNT, TIMESTAMP)]"""

        user_uuid = (
            username_or_uuid
            if _uuids.validate(username_or_uuid)
            else cls.resolve_uuid(username_or_uuid)
        )

        if not user_uuid:

            return []

        cursor.execute(
            """
            SELECT
                COUNTERPARTY_USERNAME,
                TRANSACTION_TYPE,
                AMOUNT,
                TIMESTAMP
            FROM TRANSACTIONS
            WHERE USER_UUID = ?
            ORDER BY TIMESTAMP DESC
            LIMIT ?;
            """,
            (user_uuid, limit),
        )

        return cursor.fetchall()

    @classmethod
    def full_name(cls, username_or_uuid: str) -> str:

        if _uuids.validate(username_or_uuid):

            cursor.execute(
                """
                SELECT FULL_NAME FROM USERS WHERE UUID = ?
                """,
                (username_or_uuid,),
            )

            row = cursor.fetchone()
            return row[0] if row is not None else "User"

        cursor.execute(
            """
            SELECT FULL_NAME FROM USERS WHERE USERNAME = ?
            """,
            (username_or_uuid,),
        )

        row = cursor.fetchone()
        return row[0] if row is not None else "User"

    @classmethod
    def last_login(cls, username_or_uuid: str) -> datetime | None:

        if _uuids.validate(username_or_uuid):

            cursor.execute(
                """
                SELECT LAST_LOGIN FROM USERS WHERE UUID = ?
                """,
                (username_or_uuid,),
            )

            row = cursor.fetchone()
            return (
                datetime.fromisoformat(row[0]).replace(tzinfo=timezone.utc)
                if row is not None and row[0] is not None
                else None
            )

        cursor.execute(
            """
            SELECT LAST_LOGIN FROM USERS WHERE USERNAME = ?
            """,
            (username_or_uuid,),
        )

        row = cursor.fetchone()
        return (
            datetime.fromisoformat(row[0]).replace(tzinfo=timezone.utc)
            if row is not None and row[0] is not None
            else None
        )


class AdminLookup(AdminLookupBase):

    @classmethod
    def exists(cls, username: str) -> bool:

        cursor.execute(
            """
                SELECT 1 FROM ADMINS WHERE USERNAME = ?
                """,
            (username,),
        )

        return cursor.fetchone() is not None
