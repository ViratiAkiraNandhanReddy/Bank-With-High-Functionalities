from .authentication import UserAuthentication, AdminAuthentication
from .lookup import UserLookup, AdminLookup, ApplicationLookup, SecurityEventLookup
from .management import (
    UserManagement,
    AdminManagement,
    ApplicationManagement,
    SecurityEventManagement,
)
from .schema import (
    UserSchema,
    AdminSchema,
    TransactionSchema,
    AnnouncementSchema,
    SecurityEventSchema,
)


class Schema:

    user: type[UserSchema] = UserSchema
    admin: type[AdminSchema] = AdminSchema
    transaction: type[TransactionSchema] = TransactionSchema
    announcement: type[AnnouncementSchema] = AnnouncementSchema
    security_event: type[SecurityEventSchema] = SecurityEventSchema


class Lookup:

    user: type[UserLookup] = UserLookup
    admin: type[AdminLookup] = AdminLookup
    application: type[ApplicationLookup] = ApplicationLookup
    security_event: type[SecurityEventLookup] = SecurityEventLookup


class Authentication:

    user: type[UserAuthentication] = UserAuthentication
    admin: type[AdminAuthentication] = AdminAuthentication


class Management:

    user: type[UserManagement] = UserManagement
    admin: type[AdminManagement] = AdminManagement
    application: type[ApplicationManagement] = ApplicationManagement
    security_event: type[SecurityEventManagement] = SecurityEventManagement


class SERVER:

    authentication: type[Authentication] = Authentication
    lookup: type[Lookup] = Lookup
    management: type[Management] = Management
    schema: type[Schema] = Schema


__all__ = ["SERVER"]
