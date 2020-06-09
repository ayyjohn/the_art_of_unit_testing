import pytest

from log_analyzer import LogAnalyzer


class TestLogAnalyzer:
    def test__is_valid_log_filename__bad_extension__returns_false(self):
        analyzer = self._make_log_analyzer()

        result = analyzer.is_valid_log_filename("filewithbadextension.foo")

        assert not result

    @pytest.mark.parametrize(
        "input", ["filewithgoodextensionlower.slf", "filewithgoodextensionupper.SLF", ]
    )
    def test__is_valid_log_filename__valid_extension__returns_true(self, input: str):
        analyzer = self._make_log_analyzer()

        result = analyzer.is_valid_log_filename(input)

        assert result

    @pytest.mark.exceptions
    def test__is_valid_log_filename__empty_filename__throws_argument_exception(self):
        analyzer = self._make_log_analyzer()

        with pytest.raises(ValueError):
            analyzer.is_valid_log_filename("")

    @pytest.mark.parametrize(
        "input,expected", [("invalidname.foo", False), ("validname.slf", True), ]
    )
    def test__is_valid_log_filename__when_called__changes_was_last_filename_valid(
            self, input: str, expected: bool
    ):
        analyzer = self._make_log_analyzer()

        analyzer.is_valid_log_filename(input)

        assert analyzer.was_last_filename_valid == expected

    def _make_log_analyzer(self):
        return LogAnalyzer()