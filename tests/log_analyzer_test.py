from log_analyzer import LogAnalyzer


class TestLogAnalyzer:
    def test__is_valid_log_filename__bad_extension__returns_false(self):
        analyzer = LogAnalyzer()

        result = analyzer.is_valid_log_filename("filewithbadextension.foo")

        assert not result

    def test__is_valid_log_filename__good_extension_lowercase_returns_true(self):
        analyzer = LogAnalyzer()

        result = analyzer.is_valid_log_filename("filewithgoodextensionlower.slf")

        assert result

    def test__is_valid_log_filename__good_extension_uppercase_returns_true(self):
        analyzer = LogAnalyzer()

        result = analyzer.is_valid_log_filename("filewithgoodextensionupper.SLF")

        assert result
