# test_calculator.py

import pytest
from src.kalkulator.view import show_result

@pytest.mark.parametrize(
    "operand1, operator, operand2, result, expected_output",
    [
        (2, '+', 3, 5, "Hasil: 2 + 3 = 5"),
        (10, '-', 4, 6, "Hasil: 10 - 4 = 6"),
        (6, '*', 7, 42, "Hasil: 6 * 7 = 42"),
        (8, '/', 2, 4.0, "Hasil: 8 / 2 = 4.0"),
    ]
)
def test_show_result_output(operand1, operator, operand2, result, expected_output, capsys):
    """Menguji output dari fungsi show_result() untuk berbagai kombinasi operand dan operator."""
    show_result(operand1, operator, operand2, result)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output
