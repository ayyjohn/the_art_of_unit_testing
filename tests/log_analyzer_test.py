import pytest

from log_analyzer import LogAnalyzer
from file_extension_manager import FileExtensionManager
from fake_file_extension_manager import FakeFileExtensionManager
from file_extension_manager_factory import FILE_EXTENSION_MANAGER_FACTORY


class TestLogAnalyzer:
    def test__is_valid_log_filename__bad_extension__returns_false(self):
        stub = _get_always_invalid_fake_file_extension_manager()

        log_analyzer = _make_log_analyzer(stub)

        result = log_analyzer.is_valid_log_filename("filewithbadextension.foo")

        assert not result

    @pytest.mark.parametrize(
        "input_", ["filewithgoodextensionlower.slf", "filewithgoodextensionupper.SLF", ]
    )
    def test__is_valid_log_filename__valid_extension__returns_true(self, input_: str):
        stub = _get_always_valid_fake_file_extension_manager()

        log_analyzer = _make_log_analyzer(stub)

        result = log_analyzer.is_valid_log_filename(input_)

        assert result

    @pytest.mark.parametrize(
        "input_,expected", [("invalidname.foo", False), ("validname.slf", True), ]
    )
    def test__is_valid_log_filename__when_called__changes_was_last_filename_valid(
            self, input_: str, expected: bool
    ):
        stub = _get_fake_file_extension_manager_with_output(expected)

        analyzer = _make_log_analyzer(stub)

        analyzer.is_valid_log_filename(input_)

        assert analyzer.was_last_filename_valid == expected


def _make_log_analyzer(file_extension_manager: FileExtensionManager):
    return LogAnalyzer(file_extension_manager)


def _get_always_valid_fake_file_extension_manager():
    return _get_fake_file_extension_manager_with_output(True)


def _get_always_invalid_fake_file_extension_manager():
    return _get_fake_file_extension_manager_with_output(False)


def _get_fake_file_extension_manager_with_output(output: bool):
    manager = FakeFileExtensionManager()
    manager.will_be_valid = output
    return manager
