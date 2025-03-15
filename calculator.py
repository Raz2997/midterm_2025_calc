from commands.command_manager import CommandManager
from commands.basic_commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
from commands.menu_command import MenuCommand

# Initialize command manager
command_manager = CommandManager()

# Register calculator operations
command_manager.register("add", AddCommand())
command_manager.register("subtract", SubtractCommand())
command_manager.register("multiply", MultiplyCommand())
command_manager.register("divide", DivideCommand())

# Register menu command
command_manager.register("menu", MenuCommand(command_manager))

def main():
    print("Welcome to the Command Pattern Calculator!")
    command_manager.execute("menu")  # Display menu on startup

    while True:
        user_input = input("\nEnter command: ").strip().lower()
        
        if user_input == "exit":
            print("Exiting calculator. Goodbye!")
            break
        
        if user_input in command_manager.commands:
            command_manager.execute(user_input)
        else:
            print("Invalid command. Type 'menu' to see available commands.")

if __name__ == "__main__":
    main()
