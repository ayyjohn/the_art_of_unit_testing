from file_extension_manager import FileExtensionManager


class AlwaysValidFakeFileExtensionManager(FileExtensionManager):

    @staticmethod
    def is_valid(filename: str) -> bool:
        return True
