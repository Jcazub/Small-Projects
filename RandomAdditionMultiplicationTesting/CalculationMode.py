from enum import Enum


class CalculationMode(Enum):
    ADDITION = 'addition'
    SUBTRACTION = 'subtraction'
    MULTIPLICATION = 'multiplication'
    DIVISION = 'division'
    SQUARES = 'squares'

    def getSign(self):
        if self == CalculationMode.ADDITION:
            return '+'
        if self == CalculationMode.SUBTRACTION:
            return '-'
        if self == CalculationMode.MULTIPLICATION:
            return '*'
        if self == CalculationMode.DIVISION:
            return '//'
        if self == CalculationMode.SQUARES:
            return '^'
        return None