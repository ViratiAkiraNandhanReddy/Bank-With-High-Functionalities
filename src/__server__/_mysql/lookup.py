lazy from datetime import UTC, datetime

lazy from ..__base__ import (
    AdminLookupBase,
    ApplicationLookupBase,
    SecurityEventLookupBase,
    UserLookupBase,
)
lazy from .._uuids import _uuids
lazy from ._connection import connection

cursor = connection.cursor()


def _timestamp_string(value: object) -> str:

    return value.isoformat(sep=" ") if isinstance(value, datetime) else str(value)


class UserLookup(UserLookupBase):
    @classmethod
    def exists(cls, username_or_uuid: str) -> bool:

        cursor.execute(
            "SELECT 1 FROM USERS WHERE USERNAME = %s OR UUID = %s",
            (username_or_uuid, username_or_uuid),
        )
        return cursor.fetchone() is not None

    @classmethod
    def balance(cls, username_or_uuid: str) -> float:

        cursor.execute(
            "SELECT BALANCE FROM USERS WHERE USERNAME = %s OR UUID = %s",
            (username_or_uuid, username_or_uuid),
        )
        row = cursor.fetchone()
        return float(row[0]) if row is not None else 0.0  # type: ignore

    @classmethod
    def resolve_uuid(cls, username: str) -> str | None:

        if _uuids.validate(username):
            return username

        cursor.execute("SELECT UUID FROM USERS WHERE USERNAME = %s", (username,))
        row = cursor.fetchone()
        return row[0] if row is not None else None  # type: ignore

    @classmethod
    def transactions(
        cls, username_or_uuid: str, limit: int = 5
    ) -> list[tuple[str, str, float, str]]:
        """Return counterparty, type, amount, and timestamp tuples."""

        user_uuid = (
            username_or_uuid
            if _uuids.validate(username_or_uuid)
            else cls.resolve_uuid(username_or_uuid)
        )
        if not user_uuid:
            return []

        cursor.execute(
            """
            SELECT COUNTERPARTY_USERNAME, TRANSACTION_TYPE, AMOUNT, TIMESTAMP
            FROM TRANSACTIONS
            WHERE USER_UUID = %s
            ORDER BY TIMESTAMP DESC
            LIMIT %s
            """,
            (user_uuid, limit),
        )
        return [
            (counterparty, kind, float(amount), _timestamp_string(timestamp))  # type: ignore
            for counterparty, kind, amount, timestamp in cursor.fetchall()
        ]  # type: ignore

    @classmethod
    def full_name(cls, username_or_uuid: str) -> str:

        cursor.execute(
            "SELECT FULL_NAME FROM USERS WHERE USERNAME = %s OR UUID = %s",
            (username_or_uuid, username_or_uuid),
        )
        row = cursor.fetchone()
        return row[0] if row is not None else "User"  # type: ignore

    @classmethod
    def last_login(cls, username_or_uuid: str) -> datetime | None:

        cursor.execute(
            "SELECT LAST_LOGIN FROM USERS WHERE USERNAME = %s OR UUID = %s",
            (username_or_uuid, username_or_uuid),
        )
        row = cursor.fetchone()
        if row is None or row[0] is None:  # type: ignore
            return None
        value = row[0]  # type: ignore
        if isinstance(value, str):
            value = datetime.fromisoformat(value)
        return value.replace(tzinfo=UTC) if value.tzinfo is None else value  # type: ignore

    @classmethod
    def frequent_transfer_recipients(
        cls, username_or_uuid: str
    ) -> list[tuple[str, int]]:

        cursor.execute(
            """
            SELECT COUNTERPARTY_USERNAME, COUNT(*) AS TRANSFER_COUNT
            FROM TRANSACTIONS
            WHERE USER_UUID = (
                SELECT UUID FROM USERS
                WHERE USERNAME = %s OR UUID = %s
            )
            AND TRANSACTION_TYPE = 'transfer_out'
            GROUP BY COUNTERPARTY_USERNAME
            ORDER BY TRANSFER_COUNT DESC
            LIMIT 3
            """,
            (username_or_uuid, username_or_uuid),
        )
        return cursor.fetchall()  # type: ignore

    @classmethod
    def created_at(cls, username_or_uuid: str) -> str:

        user_uuid = cls.resolve_uuid(username_or_uuid)
        if not user_uuid:
            return "0000-00-00 00:00:00 AM (+0000)"

        cursor.execute("SELECT CREATED_AT FROM USERS WHERE UUID = %s", (user_uuid,))
        row = cursor.fetchone()
        if row is None or row[0] is None:  # type: ignore
            return "0000-00-00 00:00:00 AM (+0000)"
        value = row[0]  # type: ignore
        if isinstance(value, str):
            value = datetime.fromisoformat(value)
        return (
            value.replace(tzinfo=UTC).astimezone().strftime("%Y-%m-%d %I:%M:%S %p (%z)")  # type: ignore
        )

    @classmethod
    def backup_code(cls, username_or_uuid: str) -> str:

        user_uuid = cls.resolve_uuid(username_or_uuid)
        if not user_uuid:
            return "00000000-0000-0000-0000-000000000000"

        cursor.execute("SELECT BACKUP_CODE FROM USERS WHERE UUID = %s", (user_uuid,))
        row = cursor.fetchone()
        return row[0] if row is not None else "00000000-0000-0000-0000-000000000000"  # type: ignore

    @classmethod
    def email_address(cls, username_or_uuid: str) -> str:

        user_uuid = cls.resolve_uuid(username_or_uuid)
        if not user_uuid:
            return "email@example.com"

        cursor.execute("SELECT EMAIL FROM USERS WHERE UUID = %s", (user_uuid,))
        row = cursor.fetchone()
        return row[0] if row is not None else "email@example.com"  # type: ignore


class AdminLookup(AdminLookupBase):
    @classmethod
    def exists(cls, username: str) -> bool:

        cursor.execute("SELECT 1 FROM ADMINS WHERE USERNAME = %s", (username,))
        return cursor.fetchone() is not None


class ApplicationLookup(ApplicationLookupBase):
    @classmethod
    def current_announcement(cls) -> str:

        cursor.execute("SELECT CONTENT FROM ANNOUNCEMENT WHERE ANNOUNCEMENT_ID = 1")
        row = cursor.fetchone()
        return row[0] if row is not None else "No new announcements."  # type: ignore


class SecurityEventLookup(SecurityEventLookupBase):
    @classmethod
    def recent(cls, username_or_uuid: str, limit: int = 5) -> list[tuple[str, str]]:

        user_uuid = UserLookup.resolve_uuid(username_or_uuid)
        if not user_uuid:
            return []

        cursor.execute(
            """
            SELECT EVENT_TYPE, CREATED_AT
            FROM SECURITY_EVENTS
            WHERE USER_UUID = %s
            ORDER BY CREATED_AT DESC
            LIMIT %s
            """,
            (user_uuid, limit),
        )
        return [
            (event_type, _timestamp_string(created_at))
            for event_type, created_at in cursor.fetchall()
        ]  # type: ignore
