lazy from ..__base__ import (
    AdminSchemaBase,
    AnnouncementSchemaBase,
    SecurityEventSchemaBase,
    TransactionSchemaBase,
    UserSchemaBase,
)
lazy from CaesarCipher import Encryption
lazy from uuid import uuid4
lazy from ._connection import connection

cursor = connection.cursor()


def _create_table(statement: str) -> bool:
    cursor.execute(statement)
    connection.commit()
    return True


class AdminSchema(AdminSchemaBase):
    @classmethod
    def create(cls) -> bool:

        created = _create_table("""
            CREATE TABLE IF NOT EXISTS ADMINS (
                USERNAME VARCHAR(100) NOT NULL PRIMARY KEY,
                PASSWORD TEXT NOT NULL,
                EMAIL VARCHAR(320) UNIQUE,
                BACKUP_CODE CHAR(36) NOT NULL,
                CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            ) ENGINE=InnoDB
        """)
        cursor.execute(
            """
            INSERT IGNORE INTO ADMINS (USERNAME, PASSWORD, BACKUP_CODE)
            VALUES (%s, %s, %s)
            """,
            (
                "administrator",
                Encryption("administrator", shift=53, alterNumbers=True).encrypt(),
                str(uuid4()),
            ),
        )
        connection.commit()
        return created


class UserSchema(UserSchemaBase):
    @classmethod
    def create(cls) -> bool:

        return _create_table("""
            CREATE TABLE IF NOT EXISTS USERS (
                UUID CHAR(36) PRIMARY KEY,
                USERNAME VARCHAR(100) NOT NULL UNIQUE,
                PASSWORD TEXT NOT NULL,
                EMAIL VARCHAR(320) UNIQUE,
                BACKUP_CODE CHAR(36) NOT NULL,
                LAST_LOGIN TIMESTAMP NULL,
                FULL_NAME VARCHAR(100) NOT NULL,
                BALANCE DOUBLE NOT NULL DEFAULT 0.0,
                CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            ) ENGINE=InnoDB
        """)


class TransactionSchema(TransactionSchemaBase):
    @classmethod
    def create(cls) -> bool:

        return _create_table("""
            CREATE TABLE IF NOT EXISTS TRANSACTIONS (
                TRANSACTION_ID BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                USER_UUID CHAR(36) NOT NULL,
                COUNTERPARTY_USERNAME VARCHAR(100) NOT NULL,
                AMOUNT DOUBLE NOT NULL,
                TRANSACTION_TYPE VARCHAR(20) NOT NULL,
                TIMESTAMP TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (USER_UUID) REFERENCES USERS(UUID) ON DELETE CASCADE
            ) ENGINE=InnoDB
        """)


class AnnouncementSchema(AnnouncementSchemaBase):
    @classmethod
    def create(cls) -> bool:

        _create_table("""
            CREATE TABLE IF NOT EXISTS ANNOUNCEMENT (
                ANNOUNCEMENT_ID TINYINT NOT NULL PRIMARY KEY,
                CONTENT TEXT NOT NULL,
                UPDATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    ON UPDATE CURRENT_TIMESTAMP,
                CONSTRAINT single_announcement CHECK (ANNOUNCEMENT_ID = 1)
            ) ENGINE=InnoDB
        """)
        cursor.execute("""
            INSERT INTO ANNOUNCEMENT (ANNOUNCEMENT_ID, CONTENT)
            VALUES (1, 'No new announcements.')
            ON DUPLICATE KEY UPDATE ANNOUNCEMENT_ID = VALUES(ANNOUNCEMENT_ID)
            """)
        connection.commit()
        return True


class SecurityEventSchema(SecurityEventSchemaBase):
    @classmethod
    def create(cls) -> bool:

        return _create_table("""
            CREATE TABLE IF NOT EXISTS SECURITY_EVENTS (
                EVENT_ID BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                USER_UUID CHAR(36) NOT NULL,
                EVENT_TYPE VARCHAR(255) NOT NULL,
                CREATED_AT TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (USER_UUID) REFERENCES USERS(UUID) ON DELETE CASCADE
            ) ENGINE=InnoDB
        """)
