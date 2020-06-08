class LogAnalyzer:
    def is_valid_log_filename(self, filename: str) -> bool:
        if not filename:
            raise ValueError("filename has to be provided")

        if not filename.upper().endswith(".SLF"):
            return False
        return True
