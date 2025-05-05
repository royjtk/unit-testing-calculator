import pytest
from src.kalkulator.validator import Validator

def test_is_not_zero_divisor_with_zero():
    """Menguji validasi pembagi nol yang seharusnya menghasilkan ValueError."""
    validator = Validator()
    with pytest.raises(ValueError) as excinfo:
        validator.is_not_zero_divisor(0)
    assert str(excinfo.value) == "Error: Pembagi tidak boleh nol."

def test_is_not_zero_divisor_valid():
    """Menguji validasi pembagi bukan nol yang seharusnya mengembalikan nilai operand tersebut."""
    validator = Validator()
    result = validator.is_not_zero_divisor(2)
    assert result == 2

def test_is_number_with_valid_number():
    """Menguji fungsi is_number dengan operand berupa angka yang seharusnya mengembalikan True."""
    validator = Validator()
    result = validator.is_number(1)
    assert result is True

def test_is_number_with_invalid_number():
    """Menguji fungsi is_number dengan operand bukan angka yang seharusnya mengembalikan False."""
    validator = Validator()
    result = validator.is_number("satu")
    assert result is False

def test_is_number_in_range_valid_min():
    """Menguji fungsi is_number_in_range dengan nilai minimum valid yang seharusnya mengembalikan True."""
    validator = Validator()
    result = validator.is_number_in_range(-32768)
    assert result is True

def test_is_number_in_range_valid_max():
    """Menguji fungsi is_number_in_range dengan nilai maximum valid yang seharusnya mengembalikan True."""
    validator = Validator()
    result = validator.is_number_in_range(32767)
    assert result is True

def test_is_number_in_range_invalid_below_min():
    """Menguji fungsi is_number_in_range dengan nilai di bawah minimum yang seharusnya mengembalikan False."""
    validator = Validator()
    result = validator.is_number_in_range(-32769)
    assert result is False

def test_is_number_in_range_invalid_above_max():
    """Menguji fungsi is_number_in_range dengan nilai di atas maximum yang seharusnya mengembalikan False."""
    validator = Validator()
    result = validator.is_number_in_range(32768)
    assert result is False