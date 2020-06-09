class MemCalculator:
    def __init__(self):
        self._total = 0

    @property
    def total(self):
        return self._total

    def add(self, number: int):
        self._total += number