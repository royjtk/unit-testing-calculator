import pytest
from src.kalkulator.view import prompt_input_operand1

@pytest.mark.parametrize("expected_output", [
    "Masukkan operand pertama:"
])
def test_prompt_operand1(capsys, expected_output):
    """TC4. Memverifikasi Tampilan perintah untuk memasukan operand pertama"""
    prompt_input_operand1()  # Jalankan fungsi
    captured = capsys.readouterr()  # Tangkap stdout
    assert captured.out.strip() == expected_output
