import pytest
from src.kalkulator.view import show_header

@pytest.mark.parametrize("expected_output", [
    "====== Kalkulator Sederhana ======"
])
def test_show_header_output(capsys, expected_output):
    """TC3. Memverifikasi tampilan header."""
    show_header()  # Jalankan fungsi
    captured = capsys.readouterr()  # Tangkap stdout
    assert captured.out.strip() == expected_output
