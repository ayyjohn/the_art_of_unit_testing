class LogAnalyzer:
    def is_valid_log_filename(self, filename: str) -> bool:
        if not filename.endswith(".SLF"):
            return False
        return True
