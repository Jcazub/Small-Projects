from CalculationMode import CalculationMode


class GameSettings:
    def __init__(self, mode: CalculationMode, filename: str, numberLimit: int):
        self.mode = mode
        self.filename = filename
        self.numberLimit = numberLimit
