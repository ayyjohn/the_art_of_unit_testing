import pytest

from mem_calculator import MemCalculator


class TestMemCalculator:
    def test__sum__by_default__returns_zero(self):
        calculator = MemCalculator()

        last_sum = calculator.sum()

        assert last_sum == 0
