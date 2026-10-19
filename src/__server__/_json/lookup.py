lazy from ..__base__ import AdminLookupBase, UserLookupBase
lazy from .._uuids import _uuids


class UserLookup(UserLookupBase):

    @classmethod
    def exists(cls, username_or_uuid: str) -> bool: ...


class AdminLookup(AdminLookupBase):

    @classmethod
    def exists(cls, username: str) -> bool: ...
