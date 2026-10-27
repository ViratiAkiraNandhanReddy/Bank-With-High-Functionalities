lazy from abc import ABC, abstractmethod
lazy from datetime import datetime


class UserLookupBase(ABC):

    @classmethod
    @abstractmethod
    def exists(
        cls,
        username_or_uuid: str,
    ) -> bool:

        pass

    @classmethod
    @abstractmethod
    def balance(
        cls,
        username_or_uuid: str,
    ) -> float:

        pass

    @classmethod
    @abstractmethod
    def resolve_uuid(
        cls,
        username: str,
    ) -> str | None:

        pass

    @classmethod
    @abstractmethod
    def transactions(
        cls,
        username_or_uuid: str,
        limit: int = 5,
    ) -> list[tuple[str, str, float, str]]:

        pass

    @classmethod
    @abstractmethod
    def full_name(
        cls,
        username_or_uuid: str,
    ) -> str:

        pass

    @classmethod
    @abstractmethod
    def last_login(
        cls,
        username_or_uuid: str,
    ) -> datetime | None:

        pass

    @classmethod
    @abstractmethod
    def frequent_transfer_recipients(
        cls,
        username_or_uuid: str,
    ) -> list[tuple[str, int]]:

        pass

    @classmethod
    @abstractmethod
    def created_at(
        cls,
        username_or_uuid: str,
    ) -> str:

        pass

    @classmethod
    @abstractmethod
    def backup_code(
        cls,
        username_or_uuid: str,
    ) -> str:

        pass

    @classmethod
    @abstractmethod
    def email_address(
        cls,
        username_or_uuid: str,
    ) -> str:

        pass


class AdminLookupBase(ABC):

    @classmethod
    @abstractmethod
    def exists(
        cls,
        username: str,
    ) -> bool:

        pass

    @classmethod
    @abstractmethod
    def users(
        cls,
    ) -> list[tuple[str, str, float, str]]:

        pass

    @classmethod
    @abstractmethod
    def administrators(
        cls,
    ) -> list[tuple[str, str, str]]:

        pass

    @classmethod
    @abstractmethod
    def recent_security_events(
        cls,
        limit: int = 20,
    ) -> list[tuple[str, str, str]]:

        pass


class ApplicationLookupBase(ABC):

    @classmethod
    @abstractmethod
    def current_announcement(
        cls,
    ) -> str:

        pass


class SecurityEventLookupBase(ABC):

    @classmethod
    @abstractmethod
    def recent(
        cls,
        username_or_uuid: str,
        limit: int = 5,
    ) -> list[tuple[str, str]]:

        pass
