from enum import Enum


class CalculationMode(Enum):
    ADDITION = 'addition'
    SUBTRACTION = 'subtraction'
    MULTIPLICATION = 'multiplication'
    DIVISION = 'division'
    SQUARES = 'squares'

    def getSign(self):
        if self.name == self.ADDITION:
            return '+'
        if self.name == self.SUBTRACTION:
            return '-'
        if self.name == self.MULTIPLICATION:
            return '*'
        if self.name == self.DIVISION:
            return '//'
        if self.name == self.SQUARES:
            return '^'
        return None