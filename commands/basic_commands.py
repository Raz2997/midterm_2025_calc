import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AddCommand:
    def execute(self):
        try:
            a, b = map(float, input("Enter two numbers separated by space: ").split())
            logger.info(f"Result: {a + b}")
        except ValueError:
            logger.error("Invalid input! Please enter two numbers.")

class SubtractCommand:
    def execute(self):
        try:
            a, b = map(float, input("Enter two numbers separated by space: ").split())
            logger.info(f"Result: {a - b}")
        except ValueError:
            logger.error("Invalid input! Please enter two numbers.")

class MultiplyCommand:
    def execute(self):
        try:
            a, b = map(float, input("Enter two numbers separated by space: ").split())
            logger.info(f"Result: {a * b}")
        except ValueError:
            logger.error("Invalid input! Please enter two numbers.")

class DivideCommand:
    def execute(self):
        try:
            a, b = map(float, input("Enter two numbers separated by space: ").split())
            if b == 0:
                logger.error("Error: Cannot divide by zero!")
            else:
                logger.info(f"Result: {a / b}")
        except ValueError:
            logger.error("Invalid input! Please enter two numbers.")