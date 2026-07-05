from ._connection import connection
from ..__base__ import UserSchemaBase, AdminSchemaBase, TransactionSchemaBase

cursor = connection.cursor()


class AdminSchema(AdminSchemaBase):

    @classmethod
    def create(cls) -> bool:

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ADMINS (
            USERNAME VARCHAR(100) NOT NULL PRIMARY KEY,
            PASSWORD TEXT NOT NULL,
            EMAIL TEXT,
            BACKUP_CODE TEXT NOT NULL,
            CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
            """)

        connection.commit()

        return cursor.rowcount > 0


class UserSchema(UserSchemaBase):

    @classmethod
    def create(cls) -> bool:

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS USERS (
            USERNAME VARCHAR(100) NOT NULL PRIMARY KEY,
            UUID CHAR(36) NOT NULL,
            PASSWORD TEXT NOT NULL,
            EMAIL TEXT,
            BACKUP_CODE TEXT NOT NULL,
            CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            BALANCE REAL DEFAULT 0.0)
            """)

        connection.commit()

        return cursor.rowcount > 0


class TransactionSchema(TransactionSchemaBase):

    @classmethod
    def create(cls) -> bool:

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS TRANSACTIONS (
            TRANSACTION_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            USERNAME VARCHAR(100) NOT NULL,
            AMOUNT REAL NOT NULL,
            TRANSACTION_TYPE VARCHAR(50) NOT NULL,
            TIMESTAMP TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (USERNAME) REFERENCES USERS(USERNAME))
            """)

        connection.commit()

        return cursor.rowcount > 0
