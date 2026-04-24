import pytest
from garage import enter_garage, exit_garage, get_available_spots, calculate_fee

def test_enter_garage_carid_in_garage():
    new_garage = {
    "capacity": 10,   # total number of spots
    "cars": {"FJC5751": 1}         # car_id -> entry_hour (int)
    }
    with pytest.raises(ValueError):
        enter_garage(new_garage, "FJC5751", 7)

def test_enter_garage_works():
    new_garage = {
    "capacity": 10,   # total number of spots
    "cars": {"FJC5751": 1}         # car_id -> entry_hour (int)
    }
    expected_garage = {
    "capacity": 10,   # total number of spots
    "cars": {"FJC5751": 1,"FJC5799": 7}         # car_id -> entry_hour (int)
    }
    assert enter_garage(new_garage, "FJC5799", 7) == expected_garage

def test_enter_garage_full():
    new_garage = {
    "capacity": 4,   # total number of spots
    "cars": {"FJC5751": 1, "FJC5752": 2,"FJC5753": 4,"FJC5754":6}         # car_id -> entry_hour (int)
    }
    with pytest.raises(ValueError):
        enter_garage(new_garage, "FJC57588", 7)

def test_enter_garage_entry_int():
    new_garage = {
    "capacity": 4,   # total number of spots
    "cars": {"FJC5751": 1, "FJC5752": 2,"FJC5753": 3}         # car_id -> entry_hour (int)
    }
    with pytest.raises(TypeError):
        enter_garage(new_garage, "FJC57588", "7")

def test_exit_garage_carid_not_in():
    new_garage = {
    "capacity": 4,   # total number of spots
    "cars": {"FJC5751": 1, "FJC5752": 2,"FJC5753": 5}         # car_id -> entry_hour (int)
    }
    with pytest.raises(KeyError):
        exit_garage(new_garage, "FJC57588")

def test_exit_garage_works():
    new_garage = {
    "capacity": 4,   # total number of spots
    "cars": {"FJC5751": 1, "FJC5752": 2,"FJC5753": 3}         # car_id -> entry_hour (int)
    }
    expected_garage = {
    "capacity": 4,   # total number of spots
    "cars": {"FJC5752": 2,"FJC5753": 3}         # car_id -> entry_hour (int)
    }
    assert exit_garage(new_garage, "FJC5751") == expected_garage

def test_get_available_spots_works():
    new_garage = {
    "capacity": 6,   # total number of spots
    "cars": {"FJC5751": 1, "FJC5752": 2,"FJC5753": 3}         # car_id -> entry_hour (int)
    }
    assert get_available_spots(new_garage) == 3

def test_get_available_spots_no_negative_returns():
    new_garage = {
    "capacity": 2,   # total number of spots
    "cars": {"FJC5751": 1, "FJC5752": 2,"FJC5753": 3}         # car_id -> entry_hour (int)
    }
    assert get_available_spots(new_garage) == 0

def test_calculate_fee_works():
    assert calculate_fee(2, 5) == 10.0

@pytest.mark.parametrize("hours, rate, expected", {
    [(1, 10, 10.0),
    (2, 10, 20.0),
    (2.5, 5, 12.5)],
})

def test_calculate_fee_paramterize(hours, rate, expected):
    assert calculate_fee(hours, rate) == expected


def test_calculate_fee_invalid_rate_type():
    with pytest.raises(TypeError):
        calculate_fee(2,"5")