from file_extension_manager import FileExtensionManager


class FakeFileExtensionManager(FileExtensionManager):
    def __init__(self):
        self.will_be_valid = False

    def is_valid(self, filename: str) -> bool:
        if not filename:
            raise ValueError("filename has to be provided")
        return self.will_be_valid
