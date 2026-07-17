from datetime import datetime
from abc import ABC, abstractmethod


class UserLookupBase(ABC):

    @classmethod
    @abstractmethod
    def exists(cls, username_or_uuid: str) -> bool:

        pass

    @classmethod
    @abstractmethod
    def balance(cls, username_or_uuid: str) -> float:

        pass

    @classmethod
    @abstractmethod
    def resolve_uuid(cls, username: str) -> str | None:

        pass

    @classmethod
    @abstractmethod
    def transactions(
        cls, username_or_uuid: str, limit: int = 5
    ) -> list[tuple[str, str, float, str]]:

        pass

    @classmethod
    @abstractmethod
    def full_name(cls, username_or_uuid: str) -> str:

        pass

    @classmethod
    @abstractmethod
    def last_login(cls, username_or_uuid: str) -> datetime | None:

        pass


class AdminLookupBase(ABC):

    @classmethod
    @abstractmethod
    def exists(cls, username: str) -> bool:

        pass
