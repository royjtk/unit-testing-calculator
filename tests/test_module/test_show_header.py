# test_calculator.py

import pytest
from src.kalkulator.view import show_header

@pytest.mark.parametrize("expected_output", [
    "====== Kalkulator Sederhana ======"
])
def test_show_header_output(capsys, expected_output):
    """Menguji output dari fungsi show_header()."""
    show_header()  # Jalankan fungsi
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output

