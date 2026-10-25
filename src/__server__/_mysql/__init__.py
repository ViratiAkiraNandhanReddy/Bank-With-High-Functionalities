lazy from .authentication import AdminAuthentication, UserAuthentication
lazy from .lookup import (
    AdminLookup,
    ApplicationLookup,
    SecurityEventLookup,
    UserLookup,
)
lazy from .management import (
    AdminManagement,
    ApplicationManagement,
    SecurityEventManagement,
    UserManagement,
)
lazy from .schema import (
    AdminSchema,
    AnnouncementSchema,
    SecurityEventSchema,
    TransactionSchema,
    UserSchema,
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


Schema.admin.create()
Schema.user.create()
Schema.transaction.create()
Schema.announcement.create()
Schema.security_event.create()

__all__ = ["SERVER"]
