from abc import ABC, abstractmethod


class AdminSchemaBase(ABC):

    @classmethod
    @abstractmethod
    def create(cls) -> bool:

        pass


class TransactionSchemaBase(ABC):

    @classmethod
    @abstractmethod
    def create(cls) -> bool:

        pass


class UserSchemaBase(ABC):

    @classmethod
    @abstractmethod
    def create(cls) -> bool:

        pass
