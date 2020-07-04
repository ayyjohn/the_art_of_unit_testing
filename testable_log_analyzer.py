from log_analyzer import LogAnalyzer


class TestableLogAnalyzer(LogAnalyzer):
    def __init__(self):
        self.is_supported = False

    def _is_valid(self, filename: str) -> bool:
        return self.is_supported
