import pytest
from src.kalkulator.view import show_error

def test_show_error(capsys):
    """TC16. Verifikasi Halaman tampilan error."""
    
    # Simulasikan pemanggilan fungsi show_error dengan pesan tertentu
    show_error("Angka harus berada dalam rentang -32,768 hingga 32,767.")
    
    # Tangkap output dari fungsi yang dipanggil
    captured = capsys.readouterr()
    
    # Verifikasi apakah output yang dicetak sesuai dengan yang diharapkan
    assert captured.out.strip() == "Error: Angka harus berada dalam rentang -32,768 hingga 32,767."
