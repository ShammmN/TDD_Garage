import pytest
from garage import enter_garage

def test_enter_garage_carid_in_garage():
    new_garage = {
    "capacity": 10,   # total number of spots
    "cars": {"FJC5751"}         # car_id -> entry_hour (int)
    }
    with pytest.raises(ValueError):
        enter_garage(new_garage, "FJC5751", 7)

