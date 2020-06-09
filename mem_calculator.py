class MemCalculator:
    def __init__(self):
        self._total = 0

    @property
    def total(self):
        output = self._total
        self._total = 0
        return output

    def add(self, number: int):
        self._total += number