import pytest
from garage import enter_garage, exit_garage

def test_enter_garage_carid_in_garage():
    new_garage = {
    "capacity": 10,   # total number of spots
    "cars": {"FJC5751"}         # car_id -> entry_hour (int)
    }
    with pytest.raises(ValueError):
        enter_garage(new_garage, "FJC5751", 7)

def test_enter_garage_full():
    new_garage = {
    "capacity": 4,   # total number of spots
    "cars": {"FJC5751", "FJC5752","FJC5753","FJC5754"}         # car_id -> entry_hour (int)
    }
    with pytest.raises(ValueError):
        enter_garage(new_garage, "FJC57588", 7)

def test_enter_garage_entry_int():
    new_garage = {
    "capacity": 4,   # total number of spots
    "cars": {"FJC5751", "FJC5752","FJC5753"}         # car_id -> entry_hour (int)
    }
    with pytest.raises(TypeError):
        enter_garage(new_garage, "FJC57588", "7")

def test_exit_garage_carid_not_in():
    new_garage = {
    "capacity": 4,   # total number of spots
    "cars": {"FJC5751", "FJC5752","FJC5753"}         # car_id -> entry_hour (int)
    }
    with pytest.raises(KeyError):
        exit_garage(new_garage, "FJC57588")

def test_exit_garage_works():
    new_garage = {
    "capacity": 4,   # total number of spots
    "cars": {"FJC5751", "FJC5752","FJC5753"}         # car_id -> entry_hour (int)
    }
    expected_garage = {
    "capacity": 4,   # total number of spots
    "cars": {"FJC5752","FJC5753"}         # car_id -> entry_hour (int)
    }
    assert exit_garage(new_garage, "FJC5751") == expected_garage
