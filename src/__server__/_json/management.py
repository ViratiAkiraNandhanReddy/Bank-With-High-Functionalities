from .._uuids import _uuids
from CaesarCipher import Encryption
from ..__base__ import UserManagementBase, AdminManagementBase


class UserManagement(UserManagementBase):

    @classmethod
    def deposit(cls, username_or_uuid: str, amount: float) -> bool: ...

    @classmethod
    def withdraw(cls, username_or_uuid: str, amount: float) -> bool: ...

    @classmethod
    def change_password(cls, username_or_uuid: str, new_password: str) -> bool: ...

    @classmethod
    def change_username(cls, old_username_or_uuid: str, new_username: str) -> bool: ...

    @classmethod
    def delete(cls, username_or_uuid: str) -> bool: ...


class AdminManagement(AdminManagementBase):

    @classmethod
    def change_password(cls, username: str, new_password: str) -> bool: ...
