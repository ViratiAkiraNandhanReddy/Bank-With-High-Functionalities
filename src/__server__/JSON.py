import pathlib
from . import DIR_PATH


class SERVER:

    class traversal:

        def __init__(self) -> None:
            pass

        def is_user_exists(self, username: str) -> bool:

            return pathlib.Path(rf"{DIR_PATH}\database\json\{username}.json").exists()
