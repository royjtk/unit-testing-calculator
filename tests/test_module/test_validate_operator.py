import pytest
from src.kalkulator.validator import Validator

def test_validate_operator_invalid():
    """Menguji validasi dengan operator yang tidak valid (:) yang seharusnya menghasilkan ValueError."""
    validator = Validator()
    with pytest.raises(ValueError) as excinfo:
        validator.validate_operator(":")
    assert str(excinfo.value) == "Error: Operator yang valid hanya +, -, *, /."

@pytest.mark.parametrize("operator", ["+", "-", "*", "/"])
def test_validate_operator_valid(operator):
    """Menguji validasi dengan operator yang valid (+, -, *, /) yang seharusnya mengembalikan operator tersebut."""
    validator = Validator()
    result = validator.validate_operator(operator)
    assert result == operator
