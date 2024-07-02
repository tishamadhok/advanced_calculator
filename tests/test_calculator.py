import pytest
from calculator.calculator import Calculator

def test_add(fake_data):
    a, b, operation, expected_result = fake_data
    if operation == 'add':
        assert Calculator.add(a, b) == expected_result

def test_subtract(fake_data):
    a, b, operation, expected_result = fake_data
    if operation == 'subtract':
        assert Calculator.subtract(a, b) == expected_result

def test_multiply(fake_data):
    a, b, operation, expected_result = fake_data
    if operation == 'multiply':
        assert Calculator.multiply(a, b) == expected_result

def test_divide(fake_data):
    a, b, operation, expected_result = fake_data
    if operation == 'divide' and b != 0:
        assert Calculator.divide(a, b) == expected_result

def test_divide_by_zero():
    with pytest.raises(ValueError):
        Calculator.divide(10, 0)
