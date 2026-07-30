from abc import ABC, abstractmethod


class UserManagementBase(ABC):

    @classmethod
    @abstractmethod
    def deposit(cls, username_or_uuid: str, password: str, amount: float) -> bool:

        pass

    @classmethod
    @abstractmethod
    def change_password(cls, username_or_uuid: str, new_password: str) -> bool:

        pass

    @classmethod
    @abstractmethod
    def change_username(cls, old_username_or_uuid: str, new_username: str) -> bool:

        pass

    @classmethod
    @abstractmethod
    def delete(cls, username_or_uuid: str) -> bool:

        pass


class AdminManagementBase(ABC):

    @classmethod
    @abstractmethod
    def change_password(cls, username: str, new_password: str) -> bool:

        pass


class ApplicationManagementBase(ABC):

    @classmethod
    @abstractmethod
    def update_announcement(cls, announcement: str = "No new announcements.") -> bool:

        pass
