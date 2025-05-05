import pytest
from src.kalkulator.validator import Validator

def test_validate_operand_not_number():
    """Menguji validasi dengan operand yang bukan angka (string 'lima') yang seharusnya menghasilkan ValueError."""
    validator = Validator()
    with pytest.raises(ValueError) as excinfo:
        validator.validate_operand("lima")
    assert str(excinfo.value) == "Error: Operand harus berupa angka."

@pytest.mark.parametrize("operand", [-32769, 32770])
def test_validate_operand_out_of_range(operand):
    """Menguji validasi dengan operand di luar rentang (-32768...32767) yang seharusnya menghasilkan ValueError."""
    validator = Validator()
    with pytest.raises(ValueError) as excinfo:
        validator.validate_operand(operand)
    assert str(excinfo.value) == "Error: Angka harus berada dalam rentang -32,768 hingga 32,767."

def test_validate_operand_valid():
    """Menguji validasi dengan operand valid (10) yang seharusnya mengembalikan nilai operand tersebut."""
    validator = Validator()
    result = validator.validate_operand(10)
    assert result == 10
