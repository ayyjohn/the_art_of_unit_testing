import unittest
from log_analyzer import LogAnalyzer


class LogAnalyzerTests(unittest.TestCase):
    def test__is_valid_log_filename__bad_extension__returns_false(self):
        analyzer = LogAnalyzer()

        result = analyzer.is_valid_log_filename("filewithbadextension.foo")

        self.assertFalse(result)

    def test__is_valid_log_filename__good_extension_lowercase_returns_true(self):
        assert False

    def test__is_valid_log_filename__good_extension_uppercase_returns_true(self):
        assert False


if __name__ == "__main__":
    unittest.main()