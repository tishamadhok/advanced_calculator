from calculator.calculations import Calculations
from calculator.calculation import Calculation

def test_add_calculation():
    calc = Calculation('add', 1, 1, 2)
    Calculations.add_calculation(calc)
    assert Calculations.get_last_calculation() == calc

def test_clear_history():
    Calculations.clear_history()
    assert Calculations.count_history() == 0
    