
import logging

logger = logging.getLogger(__name__)

from dotenv import load_dotenv
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
env = os.getenv("ENVIRONMENT", "production")
logger.info(f"CommandManager initialized in {env} environment")


class CommandManager:
    """Manages command registration and execution."""
    
    def __init__(self):
        self.commands = {}

    def register(self, name, command):
        """Register a new command."""
        self.commands[name] = command

    def execute(self, name):
        """Execute a registered command."""
        if name in self.commands:
            logger.info(f"[{env}] Executing command: {name}")
            self.commands[name].execute()
        else:

            logger.warning(f"[{env}] Command '{name}' not found.")

# Add a basic REPL if no main.py exists
if __name__ == "__main__":
    from commands.basic_commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
    from commands.menu_command import MenuCommand
    
    manager = CommandManager()
    manager.register("add", AddCommand())
    manager.register("subtract", SubtractCommand())
    manager.register("multiply", MultiplyCommand())
    manager.register("divide", DivideCommand())
    manager.register("menu", MenuCommand(manager))

    while True:
        cmd = input("Enter command: ").strip().lower()
        if cmd == "exit":
            logger.info("Exiting calculator")
            break
        manager.execute(cmd)

