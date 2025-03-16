import pytest
import pandas as pd
import os
from calculator.calculator import Calculator, Calculation, Calculations  # Add Calculation here
from calculator.history_facade import HistoryFacade
from calculator.strategy import AddStrategy, SubtractStrategy
from commands.command_manager import CommandManager
from commands.basic_commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
from commands.history_commands import HistoryCommand, SaveHistoryCommand, ClearHistoryCommand
from commands.command_factory import CommandFactory
from commands.plugin_loader import PluginLoader
from unittest.mock import patch

# Fixtures
@pytest.fixture
def calc():
    """Fixture for Calculator instance."""
    return Calculator()

@pytest.fixture
def history_facade():
    """Fixture for HistoryFacade with clean state."""
    facade = HistoryFacade()
    facade.clear_history()
    return facade

@pytest.fixture
def command_manager():
    """Fixture for CommandManager with basic commands registered."""
    manager = CommandManager()
    manager.register("add", AddCommand())
    manager.register("subtract", SubtractCommand())
    manager.register("multiply", MultiplyCommand())
    manager.register("divide", DivideCommand())
    manager.register("history", HistoryCommand())
    manager.register("save", SaveHistoryCommand())
    manager.register("clear", ClearHistoryCommand())
    return manager

# Calculator Operation Tests
def test_add(calc):
    """Test basic addition operation."""
    assert calc.add(2, 3) == 5
    last = Calculations.get_last_calculation()
    assert str(last) == "2.0 + 3.0 = 5.0"

def test_subtract(calc):
    """Test subtraction operation."""
    assert calc.subtract(5, 2) == 3
    last = Calculations.get_last_calculation()
    assert str(last) == "5.0 - 2.0 = 3.0"

def test_multiply(calc):
    """Test multiplication operation."""
    assert calc.multiply(4, 3) == 12
    last = Calculations.get_last_calculation()
    assert str(last) == "4.0 * 3.0 = 12.0"

def test_divide(calc):
    """Test division operation."""
    assert calc.divide(6, 2) == 3
    last = Calculations.get_last_calculation()
    assert str(last) == "6.0 / 2.0 = 3.0"

def test_divide_by_zero(calc):
    """Test division by zero raises exception."""
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        calc.divide(1, 0)

# HistoryFacade Tests
def test_history_save_load(history_facade):
    """Test saving and loading history."""
    history_facade.add_calculation(Calculation(1, 2, "+", 3))
    history_facade.save_history("test_history.csv")
    history_facade.clear_history()
    history_facade.load_history("test_history.csv")
    df = history_facade.get_history()
    assert not df.empty
    assert df.iloc[0]["result"] == 3
    os.remove("test_history.csv")  # Cleanup

def test_history_clear(history_facade):
    """Test clearing history."""
    history_facade.add_calculation(Calculation(1, 2, "+", 3))
    history_facade.clear_history()
    assert history_facade.get_history().empty

def test_load_nonexistent_history(history_facade):
    """Test loading a non-existent history file."""
    history_facade.clear_history()
    history_facade.load_history("nonexistent.csv")
    assert history_facade.get_history().empty

# CommandManager and Command Tests
def test_command_execution(command_manager):
    """Test executing a registered command."""
    with patch("builtins.input", return_value="2 3"), patch("logging.Logger.info") as mock_log:
        command_manager.execute("add")
        mock_log.assert_called()

def test_unknown_command(command_manager):
    """Test executing an unknown command."""
    with patch("logging.Logger.warning") as mock_log:
        command_manager.execute("unknown")
        mock_log.assert_called_once()

def test_command_factory():
    """Test CommandFactory creates correct commands."""
    cmd = CommandFactory.create_command("add")
    assert isinstance(cmd, AddCommand)
    cmd = CommandFactory.create_command("invalid")
    assert cmd is None

# Strategy Pattern Tests
def test_add_strategy(calc):
    """Test AddStrategy execution."""
    strategy = AddStrategy()
    assert strategy.execute(2, 3) == 5

def test_subtract_strategy(calc):
    """Test SubtractStrategy execution."""
    strategy = SubtractStrategy()
    assert strategy.execute(5, 2) == 3

# Integration Test
def test_full_workflow(command_manager, history_facade):
    """Test a full workflow: operation -> history -> save."""
    calc = Calculator()
    calc.add(4, 5)
    history_facade.add_calculation(Calculations.get_last_calculation())
    history_facade.save_history("workflow_test.csv")
    assert not history_facade.get_history().empty
    os.remove("workflow_test.csv")  # Cleanup