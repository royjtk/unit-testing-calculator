import pytest
from src.kalkulator.validator import Validator

def test_validate_operand_not_number():
    """TC1: Menguji validasi dengan operand yang bukan angka (string 'lima') yang seharusnya menghasilkan ValueError."""
    validator = Validator()
    with pytest.raises(ValueError) as excinfo:
        validator.validate_operand("lima")
    assert str(excinfo.value) == "Error: Operand harus berupa angka."
    
def test_validate_operand_min_boundary():
    """TC2: Menguji validasi dengan operand pada batas minimum valid (-32768) yang seharusnya mengembalikan nilai operand tersebut."""
    validator = Validator()
    result = validator.validate_operand(-32768)
    assert result == -32768

def test_validate_operand_max_boundary():
    """TC3: Menguji validasi dengan operand pada batas maximum valid (32767) yang seharusnya mengembalikan nilai operand tersebut."""
    validator = Validator()
    result = validator.validate_operand(32767)
    assert result == 32767


@pytest.mark.parametrize("operand", [-32769, 32770])
def test_validate_operand_out_of_range(operand):
    """TC4/TC5: Menguji validasi dengan operand di luar rentang (-32768...32767) yang seharusnya menghasilkan ValueError."""
    validator = Validator()
    with pytest.raises(ValueError) as excinfo:
        validator.validate_operand(operand)
    assert str(excinfo.value) == "Error: Angka harus berada dalam rentang -32,768 hingga 32,767."

def test_validate_operand_valid():
    """TC6: Menguji validasi dengan operand valid (10) yang seharusnya mengembalikan nilai operand tersebut."""
    validator = Validator()
    result = validator.validate_operand(10)
    assert result == 10

