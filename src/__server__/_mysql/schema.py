from ._connection import connection
from ..__base__ import UserSchemaBase, AdminSchemaBase, TransactionSchemaBase

cursor = connection.cursor()


class AdminSchema(AdminSchemaBase):

    @classmethod
    def create(cls) -> bool: ...


class UserSchema(UserSchemaBase):

    @classmethod
    def create(cls) -> bool: ...


class TransactionSchema(TransactionSchemaBase):

    @classmethod
    def create(cls) -> bool: ...
