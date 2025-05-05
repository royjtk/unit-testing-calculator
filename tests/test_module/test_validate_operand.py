import pytest
from src.kalkulator.validator import Validator

v = Validator()

# --- TC1 : operand bukan angka ---------------------------------------------
def test_validate_operand_not_number():
    """Menguji validasi dengan operand yang bukan angka (string 'lima') yang seharusnya menghasilkan ValueError."""
    with pytest.raises(ValueError, match=r"Error: Operand harus berupa angka"):
        v.validate_operand("lima")          # string → error

# --- TC2 : operand di luar rentang -32768…32767 ----------------------------
@pytest.mark.parametrize("value", [-32769, 32770])
def test_validate_operand_out_of_range(value):
    """Menguji validasi dengan operand di luar rentang (-32768...32767) yang seharusnya menghasilkan ValueError."""
    with pytest.raises(ValueError, match=r"Error: Angka harus berada dalam rentang -32,768 hingga 32,767."):
        v.validate_operand(value)

# --- TC3 : operand valid ----------------------------------------------------
def test_validate_operand_valid():
    """Menguji validasi dengan operand valid (10) yang seharusnya mengembalikan nilai operand tersebut."""
    assert v.validate_operand(10) == 10      # harus dikembalikan apa adanya
