"""Seed the default SQLite database with fictional preview data."""

from __future__ import annotations

import argparse
import json
import sqlite3
from pathlib import Path

from CaesarCipher import Encryption

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "database" / "config.json"
DATABASE_PATH = ROOT / "database" / "sqlite3" / "database.sqlite3"
SEED_PATH = ROOT / "database" / "sqlite3" / "demo_data.sql"
LARGE_SEED_NAME = "preview-v2-large"
DEMO_PASSWORD = "DemoPass123!"


def load_database_type() -> str:
    with CONFIG_PATH.open(encoding="utf-8") as config_file:
        configuration = json.load(config_file)
    return configuration.get("DATABASE TYPE", "")


def is_seed_applied(connection: sqlite3.Connection, seed_name: str) -> bool:
    return (
        connection.execute(
            "SELECT 1 FROM DEMO_SEED WHERE SEED_NAME = ?",
            (seed_name,),
        ).fetchone()
        is not None
    )


def mark_seed_applied(connection: sqlite3.Connection, seed_name: str) -> None:
    connection.execute(
        "INSERT OR REPLACE INTO DEMO_SEED (SEED_NAME) VALUES (?)",
        (seed_name,),
    )


def seed_large_dataset(connection: sqlite3.Connection) -> None:
    password = Encryption(DEMO_PASSWORD, shift=8, alterNumbers=True).encrypt()
    users = []

    for index in range(1, 25):
        username = f"preview{index:02d}"
        initial_deposit = 1000.00 + index * 125.00
        transfer_out = 50.00 + index * 3.00
        transfer_in = 35.00 + (index - 1) * 2.00
        withdrawal = 25.00 + index
        follow_up_deposit = 75.00 + index * 4.00
        balance = (
            initial_deposit
            - transfer_out
            + transfer_in
            - withdrawal
            + follow_up_deposit
        )
        users.append(
            (
                f"00000000-0000-0000-0000-00000000{index + 300:06d}",
                username,
                password,
                f"{username}@example.com",
                f"00000000-0000-0000-0000-00000000{index + 400:06d}",
                f"2026-10-{(index % 27) + 1:02d} {8 + index % 8:02d}:15:00",
                f"Preview User {index:02d}",
                balance,
                f"2026-09-{(index % 27) + 1:02d} 09:00:00",
            )
        )

    connection.executemany(
        """
        INSERT OR IGNORE INTO USERS (
            UUID, USERNAME, PASSWORD, EMAIL, BACKUP_CODE, LAST_LOGIN,
            FULL_NAME, BALANCE, CREATED_AT
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        users,
    )

    transactions = []
    security_events = []
    for index, user in enumerate(users, start=1):
        user_uuid, username = user[0], user[1]
        previous_username = f"preview{index - 1:02d}" if index > 1 else "preview24"
        next_username = f"preview{index + 1:02d}" if index < 24 else "preview01"
        timestamp_day = (index % 27) + 1

        transactions.extend(
            [
                (
                    user_uuid,
                    username,
                    1000.00 + index * 125.00,
                    "deposit",
                    f"2026-10-{timestamp_day:02d} 09:20:00",
                ),
                (
                    user_uuid,
                    next_username,
                    50.00 + index * 3.00,
                    "transfer_out",
                    f"2026-10-{timestamp_day:02d} 11:10:00",
                ),
                (
                    user_uuid,
                    previous_username,
                    35.00 + (index - 1) * 2.00,
                    "transfer_in",
                    f"2026-10-{timestamp_day:02d} 13:40:00",
                ),
                (
                    user_uuid,
                    username,
                    25.00 + index,
                    "withdraw",
                    f"2026-10-{timestamp_day:02d} 15:05:00",
                ),
                (
                    user_uuid,
                    username,
                    75.00 + index * 4.00,
                    "deposit",
                    f"2026-10-{timestamp_day:02d} 17:30:00",
                ),
            ]
        )
        security_events.extend(
            [
                (user_uuid, "login", f"2026-10-{timestamp_day:02d} 08:15:00"),
                (user_uuid, "transfer", f"2026-10-{timestamp_day:02d} 11:10:00"),
                (user_uuid, "logout", f"2026-10-{timestamp_day:02d} 18:00:00"),
            ]
        )

    connection.executemany(
        """
        INSERT INTO TRANSACTIONS (
            USER_UUID, COUNTERPARTY_USERNAME, AMOUNT, TRANSACTION_TYPE, TIMESTAMP
        ) VALUES (?, ?, ?, ?, ?)
        """,
        transactions,
    )
    connection.executemany(
        """
        INSERT INTO SECURITY_EVENTS (USER_UUID, EVENT_TYPE, CREATED_AT)
        VALUES (?, ?, ?)
        """,
        security_events,
    )


def seed_database() -> bool:
    database_type = load_database_type()
    if database_type != "SQLite3":
        raise RuntimeError(
            'Demo data requires "DATABASE TYPE": "SQLite3" in '
            f"{CONFIG_PATH.relative_to(ROOT)}; found {database_type or 'unset'!r}."
        )

    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
    seed_sql = SEED_PATH.read_text(encoding="utf-8")

    with sqlite3.connect(DATABASE_PATH) as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute("""
            CREATE TABLE IF NOT EXISTS DEMO_SEED (
                SEED_NAME TEXT PRIMARY KEY,
                APPLIED_AT TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """)

        seeded_anything = False
        if not is_seed_applied(connection, "preview-v1"):
            connection.executescript(seed_sql)
            mark_seed_applied(connection, "preview-v1")
            seeded_anything = True

        if not is_seed_applied(connection, LARGE_SEED_NAME):
            seed_large_dataset(connection)
            mark_seed_applied(connection, LARGE_SEED_NAME)
            seeded_anything = True

        if not seeded_anything:
            print("Demo data is already initialized. No changes were made.")
            return False

    print(f"Demo data initialized in {DATABASE_PATH.relative_to(ROOT)}.")
    print("Demo login: alice.demo / DemoPass123!")
    print("Additional showcase users: bob.demo and charlie.demo")
    print("Large preview dataset: preview01 through preview24")
    print("Large-dataset password: DemoPass123!")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Seed the default SQLite database with fictional preview data."
    )
    parser.parse_args()

    try:
        seed_database()
    except (OSError, RuntimeError, sqlite3.Error, json.JSONDecodeError) as error:
        print(f"Demo data initialization failed: {error}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
