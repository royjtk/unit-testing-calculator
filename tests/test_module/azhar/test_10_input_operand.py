import pytest
from unittest.mock import patch
from src.kalkulator.get_input import get_operand


@pytest.mark.parametrize("user_input, expected", [
    ("3", 3)
])
def test_get_operand1(user_input, expected):
    """TC17. Menguji input operand integer positif, dengan input angka 3."""
    with patch('builtins.input', return_value=user_input):
        result = get_operand()
        assert result == expected
        
@pytest.mark.parametrize("user_input, expected", [
    ("-5", -5)
])
def test_get_operand2(user_input, expected):
    """TC18. Menguji input operand intger negatif, dengan input angka -5."""
    with patch('builtins.input', return_value=user_input):
        result = get_operand()
        assert result == expected
        
@pytest.mark.parametrize("user_input, expected", [
    ("5.5", 5.5)
])
def test_get_operand3(user_input, expected):
    """TC19. Menguji input operand float positif, dengan input angka  5.5."""
    with patch('builtins.input', return_value=user_input):
        result = get_operand()
        assert result == expected
        
@pytest.mark.parametrize("user_input, expected", [
    ("-5.5", -5.5)
])
def test_get_operand4(user_input, expected):
    """TC20. Menguji input operand float negatif, dengan input angka  -5.5."""
    with patch('builtins.input', return_value=user_input):
        result = get_operand()
        assert result == expected
