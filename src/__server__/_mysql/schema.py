lazy from ..__base__ import AdminSchemaBase, TransactionSchemaBase, UserSchemaBase
lazy from ._connection import connection

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
