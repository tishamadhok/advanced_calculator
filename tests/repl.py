import pytest
from unittest.mock import patch, MagicMock
from calculator.repl import repl
from calculator.core import Calculator
from calculator.history import History
import builtins

# Create a fixture for Calculator and History
@pytest.fixture
def calculator():
    return Calculator()

@pytest.fixture
def history():
    return History(filename='test_history.csv')

def test_repl_addition(calculator, history):
    inputs = iter(['add 1 2', 'exit'])
    with patch.object(builtins, 'input', lambda _: next(inputs)):
        with patch('builtins.print') as mock_print:
            repl()
            mock_print.assert_any_call('Result: 3')

def test_repl_subtraction(calculator, history):
    inputs = iter(['subtract 5 3', 'exit'])
    with patch.object(builtins, 'input', lambda _: next(inputs)):
        with patch('builtins.print') as mock_print:
            repl()
            mock_print.assert_any_call('Result: 2')

def test_repl_multiplication(calculator, history):
    inputs = iter(['multiply 3 4', 'exit'])
    with patch.object(builtins, 'input', lambda _: next(inputs)):
        with patch('builtins.print') as mock_print:
            repl()
            mock_print.assert_any_call('Result: 12')

def test_repl_division(calculator, history):
    inputs = iter(['divide 8 2', 'exit'])
    with patch.object(builtins, 'input', lambda _: next(inputs)):
        with patch('builtins.print') as mock_print:
            repl()
            mock_print.assert_any_call('Result: 4.0')

def test_repl_divide_by_zero(calculator, history):
    inputs = iter(['divide 8 0', 'exit'])
    with patch.object(builtins, 'input', lambda _: next(inputs)):
        with patch('builtins.print') as mock_print:
            repl()
            mock_print.assert_any_call('Error: Cannot divide by zero')

def test_repl_history(calculator, history):
    inputs = iter(['add 1 2', 'history', 'exit'])
    with patch.object(builtins, 'input', lambda _: next(inputs)):
        with patch('builtins.print') as mock_print:
            repl()
            mock_print.assert_any_call("  operation  a  b  result\n0       add  1  2       3")

def test_repl_invalid_command(calculator, history):
    inputs = iter(['unknown 1 2', 'exit'])
    with patch.object(builtins, 'input', lambda _: next(inputs)):
        with patch('builtins.print') as mock_print:
            repl()
            mock_print.assert_any_call('Unknown operation: unknown')
