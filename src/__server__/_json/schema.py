from ..__base__ import UserSchemaBase, AdminSchemaBase, TransactionSchemaBase


class AdminSchema(AdminSchemaBase):

    @classmethod
    def create(cls) -> bool: ...


class UserSchema(UserSchemaBase):

    @classmethod
    def create(cls) -> bool: ...


class TransactionSchema(TransactionSchemaBase):

    @classmethod
    def create(cls) -> bool: ...
