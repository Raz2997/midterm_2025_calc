from commands.basic_commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
from commands.history_commands import HistoryCommand, SaveHistoryCommand, ClearHistoryCommand

class CommandFactory:
    @staticmethod
    def create_command(command_name):
        commands = {
            "add": AddCommand,
            "subtract": SubtractCommand,
            "multiply": MultiplyCommand,
            "divide": DivideCommand,
            "history": HistoryCommand,
            "save": SaveHistoryCommand,
            "clear": ClearHistoryCommand
        }
        return commands.get(command_name, lambda: None)()