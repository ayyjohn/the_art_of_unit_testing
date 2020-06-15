from file_extension_manager import FileExtensionManager


class LogAnalyzer:
    def __init__(self):
        self._was_last_filename_valid = False

    def is_valid_log_filename(self, filename: str) -> bool:
        manager = FileExtensionManager()
        self._was_last_filename_valid = False

        result = manager.is_valid(filename)
        self.was_last_filename_valid = result

        return result

    @property
    def was_last_filename_valid(self):
        return self._was_last_filename_valid

    @was_last_filename_valid.setter
    def was_last_filename_valid(self, value: bool):
        self._was_last_filename_valid = value
