import pytest
from src.kalkulator.validator import Validator   # sesuaikan import kalau modulmu di path berbeda

v = Validator()

# --- TC1 : operator tidak valid --------------------------------------------
def test_validate_operator_invalid():
    """Menguji validasi dengan operator yang tidak valid (:) yang seharusnya menghasilkan ValueError."""
    # parameter ":" seharusnya me-raise ValueError
    with pytest.raises(ValueError, match=r"Error: Operator yang valid hanya \+, -, \*, /."):
        v.validate_operator(":")

# --- TC2 : keempat operator valid ------------------------------------------
@pytest.mark.parametrize("op", ["+", "-", "*", "/"])
def test_validate_operator_valid(op):
    """Menguji validasi dengan operator yang valid (+, -, *, /) yang seharusnya mengembalikan operator tersebut."""
    # fungsi harus mengembalikan operator yang sama
    assert v.validate_operator(op) == op
