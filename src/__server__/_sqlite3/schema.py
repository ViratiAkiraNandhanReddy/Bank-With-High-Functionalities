from ._connection import connection
from ..__base__ import UserSchemaBase, AdminSchemaBase, TransactionSchemaBase

cursor = connection.cursor()


class AdminSchema(AdminSchemaBase):

    @classmethod
    def create(cls) -> bool:

        try:

            cursor.execute("""

                CREATE TABLE IF NOT EXISTS ADMINS (

                    USERNAME VARCHAR(100) NOT NULL PRIMARY KEY,

                    PASSWORD TEXT NOT NULL,
                    EMAIL TEXT UNIQUE,
                    BACKUP_CODE CHAR(36) NOT NULL,

                    CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP

                );

                """)

            connection.commit()

            return True

        except Exception:

            return False


class UserSchema(UserSchemaBase):

    @classmethod
    def create(cls) -> bool:

        try:

            cursor.execute("""

                CREATE TABLE IF NOT EXISTS USERS (

                    UUID CHAR(36) PRIMARY KEY,
                    USERNAME VARCHAR(100) NOT NULL UNIQUE,

                    PASSWORD TEXT NOT NULL,
                    EMAIL TEXT UNIQUE,
                    BACKUP_CODE CHAR(36) NOT NULL,
                    LAST_LOGIN TIMESTAMP,

                    FULL_NAME VARCHAR(100) NOT NULL,
                    BALANCE REAL NOT NULL DEFAULT 0.0,

                    CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP

                );

                """)

            connection.commit()  # DDL statements do not affect rowcount

            return True

        except Exception:

            return False


class TransactionSchema(TransactionSchemaBase):

    @classmethod
    def create(cls) -> bool:

        try:

            cursor.execute("""

                CREATE TABLE IF NOT EXISTS TRANSACTIONS (

                    TRANSACTION_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    USER_UUID CHAR(36) NOT NULL,

                    COUNTERPARTY_USERNAME VARCHAR(100) NOT NULL,
                    AMOUNT REAL NOT NULL,
                    TRANSACTION_TYPE VARCHAR(20) NOT NULL,

                    TIMESTAMP TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

                    FOREIGN KEY (USER_UUID) REFERENCES USERS(UUID) ON DELETE CASCADE

                );

                """)

            connection.commit()  # DDL statements do not affect rowcount

            return True

        except Exception:

            return False
