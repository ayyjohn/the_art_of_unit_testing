import pytest

from mem_calculator import MemCalculator


class TestMemCalculator:
    def test__sum__by_default__returns_zero(self):
        calculator = MemCalculator()

        last_sum = calculator.total()

        assert last_sum == 0

    def test__add__when_called__changes_sum(self):
        calculator = MemCalculator()

        calculator.add(1)
        total = calculator.total

        assert total == 1