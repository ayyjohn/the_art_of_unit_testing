import pytest

from log_analyzer import LogAnalyzer
from fake_file_extension_manager import FakeFileExtensionManager


class TestLogAnalyzer:
    def test__is_valid_log_filename__bad_extension__returns_false(self):
        log_analyzer = _make_log_analyzer_with_invalid_file_extension_manager()

        result = log_analyzer.is_valid_log_filename("filewithbadextension.foo")

        assert not result

    @pytest.mark.parametrize(
        "input_", ["filewithgoodextensionlower.slf", "filewithgoodextensionupper.SLF", ]
    )
    def test__is_valid_log_filename__valid_extension__returns_true(self, input_: str):
        log_analyzer = _make_log_analyzer_with_valid_file_extension_manager()

        result = log_analyzer.is_valid_log_filename(input_)

        assert result

    @pytest.mark.parametrize(
        "input_,expected", [("invalidname.foo", False), ("validname.slf", True), ]
    )
    def test__is_valid_log_filename__when_called__changes_was_last_filename_valid(
            self, input_: str, expected: bool
    ):
        analyzer = _make_log_analyzer()
        analyzer.file_extension_manager.will_be_valid = expected

        analyzer.is_valid_log_filename(input_)

        assert analyzer.was_last_filename_valid == expected


def _make_log_analyzer():
    return LogAnalyzer()


def _make_log_analyzer_with_valid_file_extension_manager():
    always_valid_fake_file_extension_manager = FakeFileExtensionManager()
    always_valid_fake_file_extension_manager.will_be_valid = True
    log_analyzer = LogAnalyzer()
    log_analyzer.file_extension_manager = always_valid_fake_file_extension_manager
    return log_analyzer


def _make_log_analyzer_with_invalid_file_extension_manager():
    always_invalid_fake_file_extension_manager = FakeFileExtensionManager()
    always_invalid_fake_file_extension_manager.will_be_valid = False
    log_analyzer = LogAnalyzer()
    log_analyzer.file_extension_manager = always_invalid_fake_file_extension_manager
    return log_analyzer
