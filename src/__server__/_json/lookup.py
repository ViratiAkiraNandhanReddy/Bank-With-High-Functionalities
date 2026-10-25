lazy from datetime import UTC, datetime

lazy from ..__base__ import (
    AdminLookupBase,
    ApplicationLookupBase,
    SecurityEventLookupBase,
    UserLookupBase,
)
lazy from .._uuids import _uuids
lazy from ._connection import DATA, find_user


class UserLookup(UserLookupBase):
    @classmethod
    def exists(cls, username_or_uuid: str) -> bool:

        return find_user(username_or_uuid) is not None

    @classmethod
    def balance(cls, username_or_uuid: str) -> float:

        user = find_user(username_or_uuid)
        return float(user.get("BALANCE", 0.0)) if user is not None else 0.0  # type: ignore

    @classmethod
    def resolve_uuid(cls, username: str) -> str | None:

        if _uuids.validate(username):
            return username
        user = next(
            (row for row in DATA.get("USERS", []) if row.get("USERNAME") == username),
            None,
        )
        value = user.get("UUID") if user is not None else None
        return str(value) if value is not None else None

    @classmethod
    def transactions(
        cls, username_or_uuid: str, limit: int = 5
    ) -> list[tuple[str, str, float, str]]:
        """Return counterparty, transaction type, amount, and timestamp tuples."""

        user_uuid = cls.resolve_uuid(username_or_uuid)
        if user_uuid is None:
            return []
        rows = [
            row
            for row in DATA.get("TRANSACTIONS", [])
            if row.get("USER_UUID") == user_uuid
        ]
        rows.sort(key=lambda row: str(row.get("TIMESTAMP", "")), reverse=True)
        return [
            (
                str(row.get("COUNTERPARTY_USERNAME", "")),
                str(row.get("TRANSACTION_TYPE", "")),
                float(row.get("AMOUNT", 0.0)),  # type: ignore
                str(row.get("TIMESTAMP", "")),
            )
            for row in rows[:limit]
        ]

    @classmethod
    def full_name(cls, username_or_uuid: str) -> str:

        user = find_user(username_or_uuid)
        return str(user.get("FULL_NAME", "User")) if user is not None else "User"

    @classmethod
    def last_login(cls, username_or_uuid: str) -> datetime | None:

        user = find_user(username_or_uuid)
        value = user.get("LAST_LOGIN") if user is not None else None
        if value is None:
            return None
        result = (
            value if isinstance(value, datetime) else datetime.fromisoformat(str(value))
        )
        return result.replace(tzinfo=UTC) if result.tzinfo is None else result

    @classmethod
    def frequent_transfer_recipients(
        cls, username_or_uuid: str
    ) -> list[tuple[str, int]]:

        user_uuid = cls.resolve_uuid(username_or_uuid)
        if user_uuid is None:
            return []
        counts: dict[str, int] = {}
        for row in DATA.get("TRANSACTIONS", []):
            if (
                row.get("USER_UUID") == user_uuid
                and row.get("TRANSACTION_TYPE") == "transfer_out"
            ):
                recipient = str(row.get("COUNTERPARTY_USERNAME", ""))
                counts[recipient] = counts.get(recipient, 0) + 1
        return sorted(counts.items(), key=lambda item: item[1], reverse=True)[:3]

    @classmethod
    def created_at(cls, username_or_uuid: str) -> str:

        user = find_user(username_or_uuid)
        value = user.get("CREATED_AT") if user is not None else None
        if value is None:
            return "0000-00-00 00:00:00 AM (+0000)"
        timestamp = (
            value if isinstance(value, datetime) else datetime.fromisoformat(str(value))
        )
        if timestamp.tzinfo is None:
            timestamp = timestamp.replace(tzinfo=UTC)
        return timestamp.astimezone().strftime("%Y-%m-%d %I:%M:%S %p (%z)")

    @classmethod
    def backup_code(cls, username_or_uuid: str) -> str:

        user = find_user(username_or_uuid)
        return (
            str(user.get("BACKUP_CODE"))
            if user is not None and user.get("BACKUP_CODE") is not None
            else "00000000-0000-0000-0000-000000000000"
        )

    @classmethod
    def email_address(cls, username_or_uuid: str) -> str:

        user = find_user(username_or_uuid)
        return (
            str(user.get("EMAIL"))
            if user is not None and user.get("EMAIL") is not None
            else "email@example.com"
        )


class AdminLookup(AdminLookupBase):
    @classmethod
    def exists(cls, username: str) -> bool:

        return any(row.get("USERNAME") == username for row in DATA.get("ADMINS", []))


class ApplicationLookup(ApplicationLookupBase):
    @classmethod
    def current_announcement(cls) -> str:

        row = next(
            (
                announcement
                for announcement in DATA.get("ANNOUNCEMENT", [])
                if announcement.get("ANNOUNCEMENT_ID") == 1
            ),
            None,
        )
        return (
            str(row.get("CONTENT", "No new announcements."))
            if row is not None
            else "No new announcements."
        )


class SecurityEventLookup(SecurityEventLookupBase):
    @classmethod
    def recent(cls, username_or_uuid: str, limit: int = 5) -> list[tuple[str, str]]:

        user_uuid = UserLookup.resolve_uuid(username_or_uuid)
        if user_uuid is None:
            return []
        events = [
            row
            for row in DATA.get("SECURITY_EVENTS", [])
            if row.get("USER_UUID") == user_uuid
        ]
        events.sort(key=lambda row: str(row.get("CREATED_AT", "")), reverse=True)
        return [
            (str(row.get("EVENT_TYPE", "")), str(row.get("CREATED_AT", "")))
            for row in events[:limit]
        ]
