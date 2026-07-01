from ... import _uuids
from ..__base__ import UserLookupBase, AdminLookupBase


class UserLookup(UserLookupBase):

    @classmethod
    def exists(cls, username_or_uuid: str) -> bool: ...


class AdminLookup(AdminLookupBase):

    @classmethod
    def exists(cls, username: str) -> bool: ...
