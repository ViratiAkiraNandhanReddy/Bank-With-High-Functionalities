from abc import ABC, abstractmethod


class UserManagementBase(ABC):

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
    def delete(cls, username_or_uuid: str, password: str) -> bool:

        pass


class AdminManagementBase(ABC):

    @classmethod
    @abstractmethod
    def change_password(cls, username: str, new_password: str) -> bool:

        pass
