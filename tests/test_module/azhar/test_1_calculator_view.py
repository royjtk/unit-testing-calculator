import pytest
from unittest.mock import patch
from src.kalkulator.calculator import Calculator
from src.kalkulator.validator import Validator
from src.kalkulator.calculator_view import calculator_view

@pytest.fixture
def mock_calculator_and_validator():
    """Fixture untuk mock Calculator dan Validator."""
    calc = Calculator()
    validator = Validator()
    return calc, validator

def test_calculator_view_valid(mock_calculator_and_validator, capsys):
    """TC1. Menguji calculator view dengan inputan yang valid."""
    calc, validator = mock_calculator_and_validator

    # Mocking input
    with patch('builtins.input', side_effect=['3', '+', '2']):
        with patch('src.kalkulator.calculator_view.show_header') as mock_show_header:
            with patch('src.kalkulator.calculator_view.show_error') as mock_show_error:
                with patch('src.kalkulator.calculator_view.prompt_input_operand1'), \
                     patch('src.kalkulator.calculator_view.prompt_input_operator'), \
                     patch('src.kalkulator.calculator_view.prompt_input_operand2'), \
                     patch('src.kalkulator.calculator_view.prompt_exit'):
                    # Calling the calculator_view function
                    calculator_view()

                    # Memastikan show_header() dipanggil
                    mock_show_header.assert_called_once()

                    # Tangkap dan verifikasi output yang dicetak
                    captured = capsys.readouterr()
                    assert "Hasil: 3.0 + 2.0 = 5.0" in captured.out

def test_calculator_view_invalid(mock_calculator_and_validator, capsys):
    """TC2. Menguji calculator view dengan error handler."""
    calc, validator = mock_calculator_and_validator

    # Mocking input untuk operand tidak valid
    with patch('builtins.input', side_effect=['3', '!', '2']):
        with patch('src.kalkulator.calculator_view.show_header') as mock_show_header:
            with patch('src.kalkulator.calculator_view.prompt_input_operand1'), \
                 patch('src.kalkulator.calculator_view.prompt_input_operator'), \
                 patch('src.kalkulator.calculator_view.prompt_input_operand2'), \
                 patch('src.kalkulator.calculator_view.prompt_exit'):
                # Calling the calculator_view function
                calculator_view()

                # Memastikan show_header() dipanggil
                mock_show_header.assert_called_once()

                # Tangkap dan verifikasi output yang dicetak
                captured = capsys.readouterr()
                assert "Error: Operator yang valid hanya +, -, *, /." in captured.out