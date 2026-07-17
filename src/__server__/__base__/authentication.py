from abc import ABC, abstractmethod


class UserAuthenticationBase(ABC):

    @classmethod
    @abstractmethod
    def password(cls, username_or_uuid: str, password: str) -> bool:

        pass

    @classmethod
    @abstractmethod
    def backup_code(cls, username_or_uuid: str, backup_code: str) -> bool:

        pass

    @classmethod
    @abstractmethod
    def email_address(cls, username_or_uuid: str, email_address: str) -> bool:

        pass

    @classmethod
    @abstractmethod
    def update_last_login(cls, username_or_uuid: str) -> None:

        pass


class AdminAuthenticationBase(ABC):

    @classmethod
    @abstractmethod
    def password(cls, username: str, password: str) -> bool:

        pass

    @classmethod
    @abstractmethod
    def backup_code(cls, username: str, backup_code: str) -> bool:

        pass

    @classmethod
    @abstractmethod
    def email_address(cls, username: str, email_address: str) -> bool:

        pass
