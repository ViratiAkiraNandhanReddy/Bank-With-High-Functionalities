from .lookup import UserLookup, AdminLookup
from .management import UserManagement, AdminManagement
from .schema import UserSchema, AdminSchema, TransactionSchema
from .authentication import UserAuthentication, AdminAuthentication


class Schema:

    user: type[UserSchema] = UserSchema
    admin: type[AdminSchema] = AdminSchema
    transaction: type[TransactionSchema] = TransactionSchema


class Lookup:

    user: type[UserLookup] = UserLookup
    admin: type[AdminLookup] = AdminLookup


class Authentication:

    user: type[UserAuthentication] = UserAuthentication
    admin: type[AdminAuthentication] = AdminAuthentication


class Management:

    user: type[UserManagement] = UserManagement
    admin: type[AdminManagement] = AdminManagement


class SERVER:

    authentication: type[Authentication] = Authentication
    lookup: type[Lookup] = Lookup
    management: type[Management] = Management
    schema: type[Schema] = Schema


__all__ = ["SERVER"]
