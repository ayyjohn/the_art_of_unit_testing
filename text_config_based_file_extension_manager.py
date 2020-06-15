from file_extension_manager import FileExtensionManager


class TextConfigBasedFileExtensionManager(FileExtensionManager):
    @staticmethod
    def is_valid(filename: str) -> bool:
        valid_extension = TextConfigBasedFileExtensionManager.get_valid_extension()

        if not filename:
            raise ValueError("filename has to be provided")

        return filename.upper().endswith(valid_extension)

    @staticmethod
    def get_valid_extension() -> str:
        with open('valid_file_extension.txt', 'r') as config:
            valid_extension = config.read().strip()
            return valid_extension
