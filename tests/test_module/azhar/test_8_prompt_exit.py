import pytest
from unittest.mock import patch
from src.kalkulator.view import prompt_exit


@pytest.mark.parametrize("expected_output", [
    "Tekan tombol apa saja untuk keluar..."
])
def test_prompt_exit_output(capsys, expected_output):
    """TC15. Memverifikasi tampilan exit program"""
    prompt_exit()  # Jalankan fungsi
    captured = capsys.readouterr()  # Tangkap stdout
    assert captured.out.strip() == expected_output
