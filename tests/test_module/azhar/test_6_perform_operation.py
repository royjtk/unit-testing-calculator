import pytest
from src.kalkulator.calculator import Calculator

calculator = Calculator()

@pytest.mark.parametrize("operator, operand1, operand2, expected", [
    ('+', 2, 3, 5),       
])
def test_perform_operation1(operator, operand1, operand2, expected):
    """TC7. Menguji operasi perhitungan dengan operator +."""
    result = calculator.perform_operation(operator, operand1, operand2)
    assert result == expected

@pytest.mark.parametrize("operator, operand1, operand2, expected", [
    ('-', 5, 3, 2),       
])
def test_perform_operation2(operator, operand1, operand2, expected):
    """TC8. Menguji operasi perhitungan dengan operator -."""
    result = calculator.perform_operation(operator, operand1, operand2)
    assert result == expected
    
@pytest.mark.parametrize("operator, operand1, operand2, expected", [
    ('*', 4, 3, 12),      
])
def test_perform_operation3(operator, operand1, operand2, expected):
    """TC9. Menguji operasi perhitungan dengan operator *."""
    result = calculator.perform_operation(operator, operand1, operand2)
    assert result == expected
    
@pytest.mark.parametrize("operator, operand1, operand2, expected", [
    ('/', 6, 3, 2)        
])
def test_perform_operation4(operator, operand1, operand2, expected):
    """TC10. Menguji operasi perhitungan dengan operator /."""
    result = calculator.perform_operation(operator, operand1, operand2)
    assert result == expected