import pytest
from unittest.mock import patch
from src.kalkulator.get_input import get_operator


@pytest.mark.parametrize("user_input, expected", [
    ("+", "+")
])
def test_get_operator1(user_input, expected):
    """TC21. Menguji input operator +."""
    with patch('builtins.input', return_value=user_input):
        result = get_operator()
        assert result == expected
        
@pytest.mark.parametrize("user_input, expected", [
    ("-", "-")
])
def test_get_operator2(user_input, expected):
    """TC22. Menguji input operator -."""
    with patch('builtins.input', return_value=user_input):
        result = get_operator()
        assert result == expected
        
@pytest.mark.parametrize("user_input, expected", [
    ("*", "*")
])
def test_get_operator3(user_input, expected):
    """TC23. Menguji input operator *."""
    with patch('builtins.input', return_value=user_input):
        result = get_operator()
        assert result == expected
        
@pytest.mark.parametrize("user_input, expected", [
    ("/", "/")
])
def test_get_operator4(user_input, expected):
    """TC24. Menguji input operator /."""
    with patch('builtins.input', return_value=user_input):
        result = get_operator()
        assert result == expected
        
@pytest.mark.parametrize("user_input, expected", [
    ("1", "1")
])
def test_get_operator5(user_input, expected):
    """TC25. Menguji input operator 1."""
    with patch('builtins.input', return_value=user_input):
        result = get_operator()
        assert result == expected
        
@pytest.mark.parametrize("user_input, expected", [
    ("a", "a")
])
def test_get_operator6(user_input, expected):
    """TC26. Menguji input operator a."""
    with patch('builtins.input', return_value=user_input):
        result = get_operator()
        assert result == expected
