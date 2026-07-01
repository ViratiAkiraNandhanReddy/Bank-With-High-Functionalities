from .._uuids import _uuids
from ._connection import connection
from ..__base__ import UserLookupBase, AdminLookupBase

cursor = connection.cursor()


class UserLookup(UserLookupBase):

    @classmethod
    def exists(cls, username_or_uuid: str) -> bool: ...


class AdminLookup(AdminLookupBase):

    @classmethod
    def exists(cls, username: str) -> bool: ...
