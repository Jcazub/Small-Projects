from typing import List

from CalculationMode import CalculationMode


class Calculator:
    def __init__(self):
        pass

    @classmethod
    def generateExpression(cls, operands: tuple, mode: CalculationMode):
        return '{} {} {} = '.format(operands[0], mode.getSign(), operands[1])

    @classmethod
    def calculate(cls, operand1: int, operand2: int, mode: CalculationMode):
        return cls.calculate((operand1, operand2), mode)

    @classmethod
    def calculate(cls, operands: tuple, mode: CalculationMode):
        if mode == CalculationMode.ADDITION:
            return operands[0] + operands[1]
        elif mode == CalculationMode.MULTIPLICATION or mode == CalculationMode.SQUARES:
            return operands[0] * operands[1]
        elif mode == CalculationMode.SUBTRACTION:
            return operands[0] - operands[1]
        elif mode == CalculationMode.DIVISION:
            return operands[0] // operands[1]
        raise ArithmeticError
