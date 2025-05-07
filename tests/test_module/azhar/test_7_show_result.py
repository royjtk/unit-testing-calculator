import pytest
from src.kalkulator.view import show_result

@pytest.mark.parametrize(
    "operand1, operator, operand2, result, expected_output",
    [
        (2, '+', 3, 5, "Hasil: 2 + 3 = 5")
    ]
)
def test_show_result_output1(operand1, operator, operand2, result, expected_output, capsys):
    """TC11. Memverifikasi tampilan result dengan operasi tambah."""
    show_result(operand1, operator, operand2, result)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output

@pytest.mark.parametrize(
    "operand1, operator, operand2, result, expected_output",
    [
        (10, '-', 4, 6, "Hasil: 10 - 4 = 6")
    ]
)
def test_show_result_output2(operand1, operator, operand2, result, expected_output, capsys):
    """TC12. Memverifikasi tampilan result dengan operasi kurang."""
    show_result(operand1, operator, operand2, result)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output
@pytest.mark.parametrize(
    "operand1, operator, operand2, result, expected_output",
    [
        (6, '*', 7, 42, "Hasil: 6 * 7 = 42")
    ]
)
def test_show_result_output3(operand1, operator, operand2, result, expected_output, capsys):
    """TC13. Memverifikasi tampilan result dengan operasi kali."""
    show_result(operand1, operator, operand2, result)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output
@pytest.mark.parametrize(
    "operand1, operator, operand2, result, expected_output",
    [
        (8, '/', 2, 4.0, "Hasil: 8 / 2 = 4.0")
    ]
)
def test_show_result_output(operand1, operator, operand2, result, expected_output, capsys):
    """TC14. Memverifikasi tampilan result dengan operasi bagi."""
    show_result(operand1, operator, operand2, result)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output