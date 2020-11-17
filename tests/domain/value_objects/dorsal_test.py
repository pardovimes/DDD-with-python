import pytest
from app.domain.exceptions import InvalidDorsalNumber
from app.domain.value_objects.dorsal import Dorsal

class DorsalTestCase:

    @pytest.mark.parametrize("valid_number", [1, 2, 3])
    def test_valid_number(self, valid_number):
        dorsal = Dorsal(valid_number)
        assert dorsal.number == valid_number

    @pytest.mark.parametrize("invalid_number", [-1, -2, -3])
    def test_invalid_number(self,invalid_number):
        with pytest.raises(InvalidDorsalNumber):
            Dorsal(invalid_number)
