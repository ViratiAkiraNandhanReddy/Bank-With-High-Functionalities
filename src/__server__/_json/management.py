lazy from datetime import datetime
lazy from uuid import uuid4

lazy from CaesarCipher import Encryption

lazy from ..__base__ import (
    AdminManagementBase,
    ApplicationManagementBase,
    SecurityEventManagementBase,
    UserManagementBase,
)
lazy from ._connection import DATA, find_user, save
lazy from .lookup import UserLookup


def _timestamp() -> str:

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def _next_id(table_name: str, id_column: str) -> int:

    return (
        max(
            (int(row.get(id_column, 0)) for row in DATA.get(table_name, [])),  # type: ignore
            default=0,
        )
        + 1
    )


class UserManagement(UserManagementBase):

    @classmethod
    def create(
        cls,
        username: str,
        password: str,
        full_name: str,
        email: str = "",
    ) -> bool:

        if any(row.get("USERNAME") == username for row in DATA.get("USERS", [])):
            return False
        if email and any(row.get("EMAIL") == email for row in DATA.get("USERS", [])):
            return False

        DATA.setdefault("USERS", []).append(
            {
                "UUID": str(uuid4()),
                "USERNAME": username,
                "PASSWORD": Encryption(password, shift=8, alterNumbers=True).encrypt(),
                "EMAIL": email or None,
                "BACKUP_CODE": str(uuid4()),
                "LAST_LOGIN": None,
                "FULL_NAME": full_name,
                "BALANCE": 0.0,
                "CREATED_AT": _timestamp(),
            }
        )
        save()
        return True

    @classmethod
    def deposit(cls, username_or_uuid: str, amount: float) -> bool:

        user = find_user(username_or_uuid)
        if user is None:
            return False
        user["BALANCE"] = float(user.get("BALANCE", 0.0)) + amount  # type: ignore
        DATA.setdefault("TRANSACTIONS", []).append(
            {
                "TRANSACTION_ID": _next_id("TRANSACTIONS", "TRANSACTION_ID"),
                "USER_UUID": user["UUID"],
                "COUNTERPARTY_USERNAME": username_or_uuid,
                "AMOUNT": amount,
                "TRANSACTION_TYPE": "deposit",
                "TIMESTAMP": _timestamp(),
            }
        )
        save()
        return True

    @classmethod
    def withdraw(cls, username_or_uuid: str, amount: float) -> bool:

        user = find_user(username_or_uuid)
        if user is None:
            return False
        user["BALANCE"] = float(user.get("BALANCE", 0.0)) - amount  # type: ignore
        DATA.setdefault("TRANSACTIONS", []).append(
            {
                "TRANSACTION_ID": _next_id("TRANSACTIONS", "TRANSACTION_ID"),
                "USER_UUID": user["UUID"],
                "COUNTERPARTY_USERNAME": username_or_uuid,
                "AMOUNT": amount,
                "TRANSACTION_TYPE": "withdraw",
                "TIMESTAMP": _timestamp(),
            }
        )
        save()
        return True

    @classmethod
    def transfer(
        cls, username_or_uuid: str, recipient_username: str, amount: float
    ) -> bool:

        user = find_user(username_or_uuid)
        recipient = find_user(recipient_username)
        if user is None or recipient is None:
            return False

        transaction_id = _next_id("TRANSACTIONS", "TRANSACTION_ID")
        user["BALANCE"] = float(user.get("BALANCE", 0.0)) - amount  # type: ignore
        recipient["BALANCE"] = float(recipient.get("BALANCE", 0.0)) + amount  # type: ignore
        timestamp = _timestamp()
        DATA.setdefault("TRANSACTIONS", []).extend(
            [
                {
                    "TRANSACTION_ID": transaction_id,
                    "USER_UUID": user["UUID"],
                    "COUNTERPARTY_USERNAME": recipient_username,
                    "AMOUNT": amount,
                    "TRANSACTION_TYPE": "transfer_out",
                    "TIMESTAMP": timestamp,
                },
                {
                    "TRANSACTION_ID": transaction_id + 1,
                    "USER_UUID": recipient["UUID"],
                    "COUNTERPARTY_USERNAME": username_or_uuid,
                    "AMOUNT": amount,
                    "TRANSACTION_TYPE": "transfer_in",
                    "TIMESTAMP": timestamp,
                },
            ]
        )
        save()
        return True

    @classmethod
    def change_password(cls, username_or_uuid: str, new_password: str) -> bool:

        user = find_user(username_or_uuid)
        if user is None:
            return False
        user["PASSWORD"] = Encryption(
            new_password, shift=8, alterNumbers=True
        ).encrypt()
        save()
        return True

    @classmethod
    def change_username(cls, old_username_or_uuid: str, new_username: str) -> bool:

        user = find_user(old_username_or_uuid)
        if user is None:
            return False
        user["USERNAME"] = new_username
        save()
        return True

    @classmethod
    def delete(cls, username_or_uuid: str) -> bool:

        user = find_user(username_or_uuid)
        if user is None:
            return False
        user_uuid = user.get("UUID")
        DATA["USERS"].remove(user)
        DATA["TRANSACTIONS"] = [
            row
            for row in DATA.get("TRANSACTIONS", [])
            if row.get("USER_UUID") != user_uuid
        ]
        DATA["SECURITY_EVENTS"] = [
            row
            for row in DATA.get("SECURITY_EVENTS", [])
            if row.get("USER_UUID") != user_uuid
        ]
        save()
        return True


class AdminManagement(AdminManagementBase):

    @classmethod
    def create(
        cls,
        username: str,
        password: str,
        email: str = "",
    ) -> bool:

        if any(row.get("USERNAME") == username for row in DATA.get("ADMINS", [])):
            return False

        DATA.setdefault("ADMINS", []).append(
            {
                "USERNAME": username,
                "PASSWORD": Encryption(password, shift=53, alterNumbers=True).encrypt(),
                "EMAIL": email or None,
                "BACKUP_CODE": str(uuid4()),
                "CREATED_AT": _timestamp(),
            }
        )
        save()
        return True

    @classmethod
    def change_password(cls, username: str, new_password: str) -> bool:

        admin = next(
            (row for row in DATA.get("ADMINS", []) if row.get("USERNAME") == username),
            None,
        )
        if admin is None:
            return False
        admin["PASSWORD"] = Encryption(
            new_password, shift=53, alterNumbers=True
        ).encrypt()
        save()
        return True


class ApplicationManagement(ApplicationManagementBase):
    @classmethod
    def update_announcement(cls, announcement: str = "No new announcements.") -> bool:

        row = next(
            (
                item
                for item in DATA.get("ANNOUNCEMENT", [])
                if item.get("ANNOUNCEMENT_ID") == 1
            ),
            None,
        )
        if row is None:
            return False
        row["CONTENT"] = announcement
        row["UPDATED_AT"] = _timestamp()
        save()
        return True


class SecurityEventManagement(SecurityEventManagementBase):
    @classmethod
    def record(cls, username_or_uuid: str, event_type: str) -> bool:

        user_uuid = UserLookup.resolve_uuid(username_or_uuid)
        if user_uuid is None:
            return False
        DATA.setdefault("SECURITY_EVENTS", []).append(
            {
                "EVENT_ID": _next_id("SECURITY_EVENTS", "EVENT_ID"),
                "USER_UUID": user_uuid,
                "EVENT_TYPE": event_type,
                "CREATED_AT": _timestamp(),
            }
        )
        save()
        return True
