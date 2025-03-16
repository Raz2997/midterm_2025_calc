import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AddCommand:
    def __init__(self):
        from calculator.strategy import AddStrategy  # Import inside __init__ to avoid circularity
        self.strategy = AddStrategy()

    def execute(self):
        try:
            a, b = map(float, input("Enter two numbers separated by space: ").split())
            result = self.strategy.execute(a, b)
            logger.info(f"Result: {result}")
            print(f"Result: {result}")
        except ValueError:
            logger.error("Invalid input! Please enter two numbers.")

class SubtractCommand:
    def __init__(self):
        from calculator.strategy import SubtractStrategy  # Import inside __init__ to avoid circularity
        self.strategy = SubtractStrategy()

    def execute(self):
        try:
            a, b = map(float, input("Enter two numbers separated by space: ").split())
            result = self.strategy.execute(a, b)
            logger.info(f"Result: {result}")
            print(f"Result: {result}")
        except ValueError:
            logger.error("Invalid input! Please enter two numbers.")

class MultiplyCommand:
    def execute(self):
        try:
            a, b = map(float, input("Enter two numbers separated by space: ").split())
            logger.info(f"Result: {a * b}")
            print(f"Result: {a * b}")
        except ValueError:
            logger.error("Invalid input! Please enter two numbers.")

class DivideCommand:
    def execute(self):
        try:
            a, b = map(float, input("Enter two numbers separated by space: ").split())
            if b == 0:
                logger.error("Error: Cannot divide by zero!")
                print("Error: Cannot divide by zero!")
            else:
                logger.info(f"Result: {a / b}")
                print(f"Result: {a / b}")
        except ValueError:
            logger.error("Invalid input! Please enter two numbers.")