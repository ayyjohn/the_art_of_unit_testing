from file_extension_manager import FileExtensionManager


class LogAnalyzer:
    def __init__(self, file_extension_manager: FileExtensionManager):
        self._was_last_filename_valid = False
        self.file_extension_manager = file_extension_manager

    def is_valid_log_filename(self, filename: str) -> bool:
        self._was_last_filename_valid = False

        result = self._is_valid(filename)
        self.was_last_filename_valid = result

        return result

    def _is_valid(self, filename: str):
        result = self.file_extension_manager.is_valid(filename)
        return result

    @property
    def was_last_filename_valid(self):
        return self._was_last_filename_valid

    @was_last_filename_valid.setter
    def was_last_filename_valid(self, value: bool):
        self._was_last_filename_valid = value
