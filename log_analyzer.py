class LogAnalyzer:
    def __init__(self):
        self._was_last_filename_valid = False

    def is_valid_log_filename(self, filename: str) -> bool:
        if not filename:
            raise ValueError("filename has to be provided")

        if not filename.upper().endswith(".SLF"):
            return False

        return True

    @property
    def was_last_filename_valid(self):
        return self._was_last_filename_valid

    @was_last_filename_valid.setter
    def was_last_filename_valid(self, value: bool):
        self._was_last_filename_valid = value
