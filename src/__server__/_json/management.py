from ... import _uuids
from CaesarCipher import Encryption
from ..__base__ import UserManagementBase, AdminManagementBase


class UserManagement(UserManagementBase):

    @classmethod
    def change_password(cls, username_or_uuid: str, new_password: str) -> bool: ...

    @classmethod
    def change_username(cls, old_username_or_uuid: str, new_username: str) -> bool: ...

    @classmethod
    def delete(cls, username_or_uuid: str, password: str) -> bool: ...


class AdminManagement(AdminManagementBase):

    @classmethod
    def change_password(cls, username: str, new_password: str) -> bool: ...
