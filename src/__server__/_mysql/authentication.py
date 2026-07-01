from .._uuids import _uuids
from ._connection import connection
from CaesarCipher import Encryption
from ..__base__ import UserAuthenticationBase, AdminAuthenticationBase

cursor = connection.cursor()


class UserAuthentication(UserAuthenticationBase):

    @classmethod
    def password(cls, username_or_uuid: str, password: str) -> bool: ...

    @classmethod
    def backup_code(cls, username_or_uuid: str, backup_code: str) -> bool: ...

    @classmethod
    def email_address(cls, username_or_uuid: str, email_address: str) -> bool: ...


class AdminAuthentication(AdminAuthenticationBase):

    @classmethod
    def password(cls, username: str, password: str) -> bool: ...

    @classmethod
    def backup_code(cls, username: str, backup_code: str) -> bool: ...

    @classmethod
    def email_address(cls, username: str, email_address: str) -> bool: ...
