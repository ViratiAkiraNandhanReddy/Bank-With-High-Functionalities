from .._uuids import _uuids
from ._connection import connection
from datetime import datetime, timezone
from ..__base__ import (
    UserLookupBase,
    AdminLookupBase,
    ApplicationLookupBase,
    SecurityEventLookupBase,
)

cursor = connection.cursor()


class UserLookup(UserLookupBase):

    @classmethod
    def exists(
        cls,
        username_or_uuid: str,
    ) -> bool:

        cursor.execute(
            """
            SELECT
                1
            FROM USERS
            WHERE USERNAME = ? OR UUID = ?
            """,
            (
                username_or_uuid,
                username_or_uuid,
            ),
        )

        return cursor.fetchone() is not None

    @classmethod
    def balance(
        cls,
        username_or_uuid,
    ) -> float:

        cursor.execute(
            """
            SELECT
                BALANCE
            FROM USERS
            WHERE USERNAME = ? OR UUID = ?
            """,
            (
                username_or_uuid,
                username_or_uuid,
            ),
        )

        row = cursor.fetchone()
        return row[0] if row is not None else 0.0

    @classmethod
    def resolve_uuid(
        cls,
        username: str,
    ) -> str | None:

        if _uuids.validate(username):

            return username

        cursor.execute(
            """
            SELECT
                UUID
            FROM USERS
            WHERE USERNAME = ?
            """,
            (username,),
        )

        row = cursor.fetchone()
        return row[0] if row is not None else None

    @classmethod
    def transactions(
        cls,
        username_or_uuid: str,
        limit: int = 5,
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
            (
                user_uuid,
                limit,
            ),
        )

        return cursor.fetchall()

    @classmethod
    def full_name(
        cls,
        username_or_uuid: str,
    ) -> str:

        cursor.execute(
            """
            SELECT
                FULL_NAME
            FROM USERS
            WHERE USERNAME = ? OR UUID = ?
            """,
            (
                username_or_uuid,
                username_or_uuid,
            ),
        )

        row = cursor.fetchone()
        return row[0] if row is not None else "User"

    @classmethod
    def last_login(
        cls,
        username_or_uuid: str,
    ) -> datetime | None:

        cursor.execute(
            """
            SELECT
                LAST_LOGIN
            FROM USERS
            WHERE USERNAME = ? OR UUID = ?
            """,
            (
                username_or_uuid,
                username_or_uuid,
            ),
        )

        row = cursor.fetchone()
        return (
            datetime.fromisoformat(row[0]).replace(tzinfo=timezone.utc)
            if row is not None and row[0] is not None
            else None
        )

    @classmethod
    def frequent_transfer_recipients(
        cls,
        username_or_uuid: str,
    ) -> list[tuple[str, int]]:

        cursor.execute(
            """
            SELECT
                COUNTERPARTY_USERNAME,
                COUNT(*) AS TRANSFER_COUNT
            FROM TRANSACTIONS
            WHERE USER_UUID = (
                SELECT UUID
                FROM USERS
                WHERE USERNAME = ? OR UUID = ?
            )
            AND TRANSACTION_TYPE = 'transfer_out'
            GROUP BY COUNTERPARTY_USERNAME
            ORDER BY TRANSFER_COUNT DESC
            LIMIT 3
            """,
            (
                username_or_uuid,
                username_or_uuid,
            ),
        )

        return cursor.fetchall()

    @classmethod
    def created_at(
        cls,
        username_or_uuid: str,
    ) -> str:

        user_uuid = cls.resolve_uuid(username_or_uuid)

        if not user_uuid:

            return "0000-00-00 00:00:00 AM (+0000)"

        cursor.execute(
            """
            SELECT
                CREATED_AT
            FROM USERS
            WHERE UUID = ?
            """,
            (user_uuid,),
        )

        return (
            datetime.fromisoformat(cursor.fetchone()[0])
            .replace(tzinfo=timezone.utc)
            .astimezone()
            .strftime("%Y-%m-%d %I:%M:%S %p (%z)")
        )

    @classmethod
    def backup_code(
        cls,
        username_or_uuid: str,
    ) -> str:

        user_uuid = cls.resolve_uuid(username_or_uuid)

        if not user_uuid:

            return "00000000-0000-0000-0000-000000000000"

        cursor.execute(
            """
        SELECT
            BACKUP_CODE
        FROM USERS
        WHERE UUID = ?
        """,
            (user_uuid,),
        )

        return cursor.fetchone()[0]

    @classmethod
    def email_address(
        cls,
        username_or_uuid: str,
    ) -> str:

        user_uuid = cls.resolve_uuid(username_or_uuid)

        if not user_uuid:

            return "email@example.com"

        cursor.execute(
            """
        SELECT
            EMAIL
        FROM USERS
        WHERE UUID = ?
        """,
            (user_uuid,),
        )

        return cursor.fetchone()[0]


class AdminLookup(AdminLookupBase):

    @classmethod
    def exists(
        cls,
        username: str,
    ) -> bool:

        cursor.execute(
            """
            SELECT
                1
            FROM ADMINS
            WHERE USERNAME = ?
            """,
            (username,),
        )

        return cursor.fetchone() is not None


class ApplicationLookup(ApplicationLookupBase):

    @classmethod
    def current_announcement(
        cls,
    ) -> str:

        cursor.execute(
            """
            SELECT
                CONTENT
            FROM ANNOUNCEMENT
            WHERE ANNOUNCEMENT_ID = 1
            """,
        )

        return cursor.fetchone()[0]


class SecurityEventLookup(SecurityEventLookupBase):

    @classmethod
    def recent(
        cls,
        username_or_uuid: str,
        limit: int = 5,
    ) -> list[tuple[str, str]]:

        user_uuid = UserLookup.resolve_uuid(username_or_uuid)

        cursor.execute(
            """
            SELECT
                EVENT_TYPE,
                CREATED_AT
            FROM SECURITY_EVENTS
            WHERE USER_UUID = ?
            ORDER BY CREATED_AT DESC
            LIMIT ?
            """,
            (
                user_uuid,
                limit,
            ),
        )

        return cursor.fetchall()
