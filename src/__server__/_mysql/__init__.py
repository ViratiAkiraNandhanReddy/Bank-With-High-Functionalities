lazy from .authentication import AdminAuthentication, UserAuthentication
lazy from .lookup import AdminLookup, UserLookup
lazy from .management import AdminManagement, UserManagement
lazy from .schema import AdminSchema, TransactionSchema, UserSchema


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
