import pytest
from calculator.plugins.example_plugin import square

def test_square():
    assert square(2) == 4
    assert square(-3) == 9
    assert square(0) == 0
    assert square(1.5) == 2.25
