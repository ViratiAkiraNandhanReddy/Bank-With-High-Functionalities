from abc import ABC, abstractmethod


class UserLookupBase(ABC):

    @classmethod
    @abstractmethod
    def exists(cls, username_or_uuid: str) -> bool:

        pass


class AdminLookupBase(ABC):

    @classmethod
    @abstractmethod
    def exists(cls, username: str) -> bool:

        pass
