import sqlite3
from CaesarCipher import Encryption

connection = sqlite3.connect('')

class SERVER:

    cursor = connection.cursor()

    class table_definition:
        
        def __init__(self):
            self.cursor = SERVER.cursor

        def define_user_table(self):
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS USERS (
                USERNAME VARCHAR(100) NOT NULL PRIMARY KEY,
                PASSWORD TEXT NOT NULL,
                EMAIL TEXT,
                CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )''')
            connection.commit()
        
        def define_transactions_table(self):
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS TRANSACTIONS (
                TRANSACTION_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                USERNAME VARCHAR(100) NOT NULL,
                AMOUNT REAL NOT NULL,
                TRANSACTION_TYPE VARCHAR(50) NOT NULL,
                TIMESTAMP TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (USERNAME) REFERENCES USERS(USERNAME)
            )''')
            connection.commit()

    class traversal:

        def __init__(self):
            self.cursor = SERVER.cursor
        
        def is_user_exists(self, username: str) -> bool:
            self.cursor.execute("SELECT 1 FROM USERS WHERE USERNAME = ?", (username,))
            return self.cursor.fetchone() is not None