import pytest
from src.kalkulator.calculator import Calculator

calc = Calculator()

def test_add():
    """Menguji fungsi penjumlahan dengan dua angka positif (2 + 3 = 5)."""
    assert calc.add(2, 3) == 5

def test_add_negative():
    """Menguji fungsi penjumlahan dengan angka negatif (2 + (-3) = -1)."""
    assert calc.add(2, -3) == -1

def test_subtract():
    """Menguji fungsi pengurangan dengan dua angka positif (5 - 3 = 2)."""
    assert calc.subtract(5, 3) == 2

def test_subtract_negative():
    """Menguji fungsi pengurangan dengan hasil negatif (3 - 5 = -2)."""
    assert calc.subtract(3, 5) == -2

def test_multiply():
    """Menguji fungsi perkalian dengan dua angka positif (2 * 3 = 6)."""
    assert calc.multiply(2, 3) == 6

def test_multiply_negative():
    """Menguji fungsi perkalian dengan satu angka negatif (2 * (-3) = -6)."""
    assert calc.multiply(2, -3) == -6

def test_divide():
    """Menguji fungsi pembagian dengan dua angka positif (6 / 3 = 2)."""
    assert calc.divide(6, 3) == 2.0

def test_divide_decimal():
    """Menguji fungsi pembagian dengan hasil desimal (5 / 2 = 2.5)."""
    assert calc.divide(5, 2) == 2.5

def test_divide_by_zero():
    """Menguji fungsi pembagian dengan pembagi nol yang seharusnya menghasilkan ValueError."""
    with pytest.raises(ValueError, match="Error: Pembagi tidak boleh nol."):
        calc.divide(6, 0)