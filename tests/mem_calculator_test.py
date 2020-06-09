import pytest

from mem_calculator import MemCalculator


class TestMemCalculator:
    def test__sum__by_default__returns_zero(self):
        calculator = self._make_calculator()

        last_total = calculator.total()

        assert last_total == 0

    def test__add__when_called__changes_sum(self):
        calculator = self._make_calculator()

        calculator.add(1)
        total = calculator.total()

        assert total == 1

    def test__total__when_called__resets_total(self):
        calculator = self._make_calculator()

        calculator.add(1)
        calculator.total()
        second_total = calculator.total()

        assert second_total == 0

    def _make_calculator(self):
        return MemCalculator()
