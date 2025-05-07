import pytest
from src.kalkulator.view import prompt_input_operator

@pytest.mark.parametrize("expected_output", [
    "Masukkan operator (+, -, *, /):"
])
def test_prompt_operand1(capsys, expected_output):
    """TC5. Memverifikasi Tampilan perintah untuk memasukan operator."""
    prompt_input_operator()  # Jalankan fungsi
    captured = capsys.readouterr()  # Tangkap stdout
    assert captured.out.strip() == expected_output