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
        cls, username_or_uuid: str, limit: int
    ) -> list[tuple[str, float, str]]:

        pass


class AdminLookupBase(ABC):

    @classmethod
    @abstractmethod
    def exists(cls, username: str) -> bool:

        pass
