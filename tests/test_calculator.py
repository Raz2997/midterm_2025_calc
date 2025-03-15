import pytest
from commands.command_manager import CommandManager
from commands.basic_commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
from commands.menu_command import MenuCommand
from calculator.calculator import Calculator, Calculations

@pytest.fixture
def setup_commands():
    manager = CommandManager()
    manager.register("add", AddCommand())
    manager.register("subtract", SubtractCommand())
    manager.register("multiply", MultiplyCommand())
    manager.register("divide", DivideCommand())
    manager.register("menu", MenuCommand(manager))
    return manager

def test_menu_command(setup_commands, capsys):
    setup_commands.execute("menu")
    captured = capsys.readouterr()
    assert "Available Commands:" in captured.out

@pytest.mark.parametrize("command", ["add", "subtract", "multiply", "divide", "menu"])
def test_registered_commands(setup_commands, command):
    assert command in setup_commands.commands

# Calculator tests
def test_calculator_add():
    assert Calculator.add(2, 3) == 5
    last = Calculations.get_last_calculation()
    assert str(last) == "2.0 + 3.0 = 5.0"

def test_calculator_subtract():
    assert Calculator.subtract(5, 3) == 2
    last = Calculations.get_last_calculation()
    assert str(last) == "5.0 - 3.0 = 2.0"

def test_calculator_multiply():
    assert Calculator.multiply(4, 3) == 12
    last = Calculations.get_last_calculation()
    assert str(last) == "4.0 * 3.0 = 12.0"

def test_calculator_divide():
    assert Calculator.divide(6, 2) == 3
    last = Calculations.get_last_calculation()
    assert str(last) == "6.0 / 2.0 = 3.0"

def test_calculator_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(1, 0)

def test_calculations_history():
    Calculations.clear_history()
    Calculator.add(1, 2)
    Calculator.subtract(5, 3)
    assert len(Calculations.history) == 2
    assert str(Calculations.get_last_calculation()) == "5.0 - 3.0 = 2.0"