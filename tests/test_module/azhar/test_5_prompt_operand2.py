import pytest
from src.kalkulator.view import prompt_input_operand2

@pytest.mark.parametrize("expected_output", [
    "Masukkan operand kedua:"
])
def test_prompt_operand2(capsys, expected_output):
    """TC6. Memverifikasi Tampilan perintah untuk memasukan operand kedua"""
    prompt_input_operand2()  # Jalankan fungsi
    captured = capsys.readouterr()  # Tangkap stdout
    assert captured.out.strip() == expected_output