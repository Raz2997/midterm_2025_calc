from calculator.calculator import Calculator

class OperationStrategy:
    def execute(self, a: float, b: float) -> float:
        pass

class AddStrategy(OperationStrategy):
    def execute(self, a: float, b: float) -> float:
        return Calculator.add(a, b)

class SubtractStrategy(OperationStrategy):
    def execute(self, a: float, b: float) -> float:
        return Calculator.subtract(a, b)

