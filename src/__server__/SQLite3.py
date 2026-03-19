import sqlite3
from CaesarCipher import Encryption
from . import os

connection = sqlite3.connect(
    rf"{ os.environ.get('LOCALAPPDATA') }\Bank-With-High-Functionalities\database\sqlite3\database.sqlite3"
)


class SERVER:

    cursor = connection.cursor()

    class table_definition:

        def __init__(self):

            self.cursor = SERVER.cursor

        def define_user_table(self):

            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS USERS (
                USERNAME VARCHAR(100) NOT NULL PRIMARY KEY,
                PASSWORD TEXT NOT NULL,
                EMAIL TEXT,
                SECURITY_CODE TEXT NOT NULL,
                CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
                """)

            connection.commit()

        def define_transactions_table(self):

            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS TRANSACTIONS (
                TRANSACTION_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                USERNAME VARCHAR(100) NOT NULL,
                AMOUNT REAL NOT NULL,
                TRANSACTION_TYPE VARCHAR(50) NOT NULL,
                TIMESTAMP TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (USERNAME) REFERENCES USERS(USERNAME))
                """)

            connection.commit()

    class traversal:

        def __init__(self):

            self.cursor = SERVER.cursor

        def is_user_exists(self, username: str) -> bool:

            self.cursor.execute(
                """
                SELECT 1 FROM USERS WHERE USERNAME = ?
                """,
                (username,),
            )

            return self.cursor.fetchone() is not None

    class authentication:

        def __init__(self) -> None:

            self.cursor = SERVER.cursor

        def authenticate_password(self, username: str, password: str) -> bool:

            self.cursor.execute(
                """
                SELECT password FROM users WHERE username = ?
                """,
                (username,),
            )

            return (
                self.cursor.fetchone()[0]
                == Encryption(password, shift=8, alterNumbers=True).encrypt()
            )

        def authenticate_security_code(self, username: str, security_code: str) -> bool:

            self.cursor.execute(
                """
                SELECT security_code FROM users WHERE username = ?
                """,
                (username,),
            )

            return self.cursor.fetchone()[0] == security_code

    class accountactions:

        def __init__(self) -> None:

            self.cursor = SERVER.cursor

        def change_password(self, username: str, new_password: str) -> bool:

            password: str = Encryption(
                new_password, shift=8, alterNumbers=True
            ).encrypt()

            self.cursor.execute(
                """
                UPDATE users SET password = ? WHERE username = ?
                """,
                (password, username),
            )

            connection.commit()

            return self.cursor.rowcount > 0

        def change_username(self, old_username: str, new_username: str) -> bool:

            self.cursor.execute(
                """
                UPDATE users SET username = ? WHERE username = ?
                """,
                (new_username, old_username),
            )

            connection.commit()

            return self.cursor.rowcount > 0

        def delete_account(self, username: str) -> bool:

            self.cursor.execute(
                """
                DELETE FROM users WHERE username = ?
                """,
                (username,),
            )
            connection.commit()

            return self.cursor.rowcount > 0
