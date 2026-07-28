from .lookup import UserLookup, AdminLookup, ApplicationLookup
from .management import UserManagement, AdminManagement, ApplicationManagement
from .schema import UserSchema, AdminSchema, TransactionSchema, NoticeSchema
from .authentication import UserAuthentication, AdminAuthentication


class Schema:

    user: type[UserSchema] = UserSchema
    admin: type[AdminSchema] = AdminSchema
    transaction: type[TransactionSchema] = TransactionSchema
    notice: type[NoticeSchema] = NoticeSchema


class Lookup:

    user: type[UserLookup] = UserLookup
    admin: type[AdminLookup] = AdminLookup
    application: type[ApplicationLookup] = ApplicationLookup


class Authentication:

    user: type[UserAuthentication] = UserAuthentication
    admin: type[AdminAuthentication] = AdminAuthentication


class Management:

    user: type[UserManagement] = UserManagement
    admin: type[AdminManagement] = AdminManagement
    application: type[ApplicationManagement] = ApplicationManagement


class SERVER:

    authentication: type[Authentication] = Authentication
    lookup: type[Lookup] = Lookup
    management: type[Management] = Management
    schema: type[Schema] = Schema


__all__ = ["SERVER"]
