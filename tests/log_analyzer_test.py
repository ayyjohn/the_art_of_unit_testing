import pytest
from log_analyzer import LogAnalyzer


class TestLogAnalyzer:
    def test__is_valid_log_filename__bad_extension__returns_false(self):
        analyzer = LogAnalyzer()

        result = analyzer.is_valid_log_filename("filewithbadextension.foo")

        assert not result

    @pytest.mark.parametrize(
        "input",
        [
            "filewithgoodextensionlower.slf",
            "filewithgoodextensionupper.SLF",
        ]
    )
    def test__is_valid_log_filename__valid_extension__returns_true(
        self,
        input
    ):
        analyzer = LogAnalyzer()

        result = analyzer.is_valid_log_filename(input)

        assert result

    def test__is_valid_log_filename__empty_filename__throws_argument_exception(self):
        analyzer = LogAnalyzer()

        with pytest.raises(ValueError):
            result = analyzer.is_valid_log_filename("")
