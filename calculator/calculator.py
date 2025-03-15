import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from commands.command_manager import CommandManager
from commands.basic_commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
from commands.menu_command import MenuCommand
import logging
from commands.plugin_loader import PluginLoader
PluginLoader.load_plugins(command_manager)
from commands.history_commands import HistoryCommand, SaveHistoryCommand, ClearHistoryCommand
command_manager.register("history", HistoryCommand())
command_manager.register("save", SaveHistoryCommand())
command_manager.register("clear", ClearHistoryCommand())
from dotenv import load_dotenv


load_dotenv()
log_level = os.getenv("LOG_LEVEL", "INFO")
log_file = os.getenv("LOG_FILE", None)
env = os.getenv("ENVIRONMENT", "production")

logging.basicConfig(
    level=getattr(logging, log_level.upper()),
    format='%(asctime)s - [%(env)s] - %(levelname)s - %(message)s',
    filename=log_file if log_file else None,
    filemode='a' if log_file else None
)
logger = logging.getLogger(__name__)
logger.info(f"Initialized logging in {env} environment")

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

command_manager = CommandManager()

command_manager.register("add", AddCommand())
command_manager.register("subtract", SubtractCommand())
command_manager.register("multiply", MultiplyCommand())
command_manager.register("divide", DivideCommand())
command_manager.register("menu", MenuCommand(command_manager))

def main():
    logger.info("Starting calculator application")
    print("Welcome to the Advanced Calculator!")
    command_manager.execute("menu")

    while True:
        user_input = input("\nEnter command: ").strip().lower()
        if user_input == "exit":
            logger.info("Exiting calculator")
            print("Goodbye!")
            break
        command_manager.execute(user_input)

if __name__ == "__main__":
    main()