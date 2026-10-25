lazy from datetime import datetime

lazy from ..__base__ import (
    AdminSchemaBase,
    AnnouncementSchemaBase,
    SecurityEventSchemaBase,
    TransactionSchemaBase,
    UserSchemaBase,
)
lazy from ._connection import DATA, ensure_table, save


class AdminSchema(AdminSchemaBase):
    @classmethod
    def create(cls) -> bool:

        ensure_table("ADMINS")
        return True


class UserSchema(UserSchemaBase):
    @classmethod
    def create(cls) -> bool:

        ensure_table("USERS")
        return True


class TransactionSchema(TransactionSchemaBase):
    @classmethod
    def create(cls) -> bool:

        ensure_table("TRANSACTIONS")
        return True


class AnnouncementSchema(AnnouncementSchemaBase):
    @classmethod
    def create(cls) -> bool:

        ensure_table("ANNOUNCEMENT")
        if not DATA["ANNOUNCEMENT"]:
            DATA["ANNOUNCEMENT"].append(
                {
                    "ANNOUNCEMENT_ID": 1,
                    "CONTENT": "No new announcements.",
                    "UPDATED_AT": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }
            )
            save()
        return True


class SecurityEventSchema(SecurityEventSchemaBase):
    @classmethod
    def create(cls) -> bool:

        ensure_table("SECURITY_EVENTS")
        return True
