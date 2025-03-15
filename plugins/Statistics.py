from calculator.calculator import Calculator
import logging

logger = logging.getLogger(__name__)

class StatsCommand:
    def execute(self):
        try:
            a, b = map(float, input("Enter two numbers for average: ").split())
            avg = Calculator.add(a, b) / 2
            logger.info(f"Calculated average: {avg}")
            print(f"Average: {avg}")
        except ValueError:
            logger.error("Invalid input for stats command")

def register(command_manager):
    command_manager.register("stats", StatsCommand())