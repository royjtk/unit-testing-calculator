import pytest
from src.kalkulator.main import Calculator, Validator


def test_add():
    calc = Calculator()
    assert calc.add(1, 2) == 3

def test_subtract():
    calc = Calculator()
    assert calc.subtract(5, 3) == 2

def test_multiply():
    calc = Calculator()
    assert calc.multiply(2, 3) == 6

def test_divide():
    calc = Calculator()
    assert calc.divide(6, 3) == 2.0

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(6, 0)

def test_validate_operand():
    validator = Validator()
    assert validator.validate_operand(100) == 100
    with pytest.raises(ValueError):
        validator.validate_operand("abc")

def test_validate_operator():
    validator = Validator()
    assert validator.validate_operator("+") == "+"
    with pytest.raises(ValueError):
        validator.validate_operator("!")