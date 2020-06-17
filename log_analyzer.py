from file_extension_manager import FileExtensionManager
from text_config_based_file_extension_manager import TextConfigBasedFileExtensionManager


class LogAnalyzer:
    def __init__(self):
        self._was_last_filename_valid = False
        self.file_extension_manager = TextConfigBasedFileExtensionManager()

    def is_valid_log_filename(self, filename: str) -> bool:
        self._was_last_filename_valid = False

        result = self.file_extension_manager.is_valid(filename)
        self.was_last_filename_valid = result

        return result

    @property
    def was_last_filename_valid(self):
        return self._was_last_filename_valid

    @was_last_filename_valid.setter
    def was_last_filename_valid(self, value: bool):
        self._was_last_filename_valid = value
