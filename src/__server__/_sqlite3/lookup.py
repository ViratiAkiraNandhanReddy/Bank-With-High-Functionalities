from .._uuids import _uuids
from ._connection import connection
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
