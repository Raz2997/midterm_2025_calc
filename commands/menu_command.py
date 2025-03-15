class MenuCommand:
    """Command to display available commands."""
    
    def __init__(self, command_manager):
        self.command_manager = command_manager

    def execute(self):
        print("\nAvailable Commands:")
        for command in self.command_manager.commands.keys():
            print(f"- {command}")
        print("Type 'exit' to quit the calculator.")