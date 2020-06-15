from abc import ABC, abstractmethod


class FileExtensionManager(ABC):

    @abstractmethod
    def is_valid(self, filename: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_valid_extension(self) -> str:
        raise NotImplementedError
