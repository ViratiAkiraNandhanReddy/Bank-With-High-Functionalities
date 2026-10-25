lazy import json
lazy from pathlib import Path
lazy from time import sleep

lazy from ...utils import root

DATA_PATH: Path = root / "database" / "json" / "database.json"
DATA: dict[str, list[dict[str, object]]] = {}

if DATA_PATH.exists():
    with DATA_PATH.open(encoding="utf-8") as database:
        loaded = json.load(database)
    if not isinstance(loaded, dict) or any(
        not isinstance(table, list) or any(not isinstance(row, dict) for row in table)
        for table in loaded.values()
    ):
        raise ValueError(f"Invalid JSON database structure in {DATA_PATH}")
    DATA.update(loaded)


def ensure_table(table_name: str) -> None:

    if table_name not in DATA:
        DATA[table_name] = []
        save()


def save() -> None:

    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = DATA_PATH.with_suffix(".json.tmp")
    with temporary_path.open("w", encoding="utf-8") as database:
        json.dump(DATA, database, indent=4, ensure_ascii=False)
        database.write("\n")
    for attempt in range(3):
        try:
            temporary_path.replace(DATA_PATH)
            break
        except PermissionError:
            if attempt == 2:
                raise
            sleep(0.02)


def find_user(username_or_uuid: str) -> dict[str, object] | None:

    return next(
        (
            user
            for user in DATA.get("USERS", [])
            if user.get("USERNAME") == username_or_uuid
            or user.get("UUID") == username_or_uuid
        ),
        None,
    )
