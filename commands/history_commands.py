from calculator.history_facade import HistoryFacade
import logging

logger = logging.getLogger(__name__)

class HistoryCommand:
    def execute(self):
        history = HistoryFacade().get_history()
        if history.empty:
            print("No history available.")
        else:
            print(history)

class SaveHistoryCommand:
    def execute(self):
        HistoryFacade().save_history()
        print("History saved to history.csv")

class ClearHistoryCommand:
    def execute(self):
        HistoryFacade().clear_history()
        print("History cleared")