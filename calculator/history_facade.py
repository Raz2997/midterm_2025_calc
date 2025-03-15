import pandas as pd
from calculator.calculator import Calculations, Calculation
import logging
from typing import List

logger = logging.getLogger(__name__)

class HistoryFacade:
    """Facade for managing calculation history with Pandas."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(HistoryFacade, cls).__new__(cls)
            cls._instance.df = pd.DataFrame(columns=["operand1", "operand2", "operation", "result"])
        return cls._instance

    def add_calculation(self, calc: Calculation):
        new_row = pd.DataFrame([{
            "operand1": calc.operand1,
            "operand2": calc.operand2,
            "operation": calc.operation,
            "result": calc.result
        }])
        self.df = pd.concat([self.df, new_row], ignore_index=True)
        logger.info(f"Added calculation to history: {calc}")

    def save_history(self, filepath="history.csv"):
        self.df.to_csv(filepath, index=False)
        logger.info(f"Saved history to {filepath}")

    def load_history(self, filepath="history.csv"):
        if not os.path.exists(filepath):  # LBYL
            logger.warning(f"No history file found at {filepath}")
            return
        try:
            self.df = pd.read_csv(filepath)
            logger.info(f"Loaded history from {filepath}")
        except Exception as e:
            logger.error(f"Failed to load history: {str(e)}")

    def clear_history(self):
        self.df = pd.DataFrame(columns=["operand1", "operand2", "operation", "result"])
        logger.info("Cleared calculation history")

    def get_history(self) -> pd.DataFrame:
        return self.df