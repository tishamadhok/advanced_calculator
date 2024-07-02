from calculator.calculation import Calculation

def test_calculation():
    calc = Calculation('add', 1, 1, 2)
    assert calc.operation == 'add'
    assert calc.a == 1
    assert calc.b == 1
    assert calc.result == 2
    assert repr(calc) == '1 add 1 = 2'
    