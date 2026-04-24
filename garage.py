def enter_garage(garage, car_id, entry_hour):
    if car_id in garage["cars"]:
        raise ValueError("Car is already in garage!")
    if len(garage["cars"]) >= garage["capacity"]:
        raise ValueError("Garage is full")
    if not isinstance(entry_hour, int):
        raise TypeError("Entry hour must be int")

    garage["cars"][car_id] = entry_hour
    return garage

def exit_garage(garage, car_id):
    if car_id not in garage["cars"]:
        raise KeyError("Car is not in garage!")

    del garage["cars"][car_id]
    return garage

def get_available_spots(garage):
    if garage["capacity"] - len(garage["cars"]) <= 0:
        return 0
    return garage["capacity"] - len(garage["cars"])

def calculate_fee(hours, rate):
    if not isinstance(hours, (int, float)) or not isinstance(rate, (int, float)):
        raise TypeError("Not correct data type")
    if hours < 0 or rate < 0:
        raise ValueError("no negatives")
    return round(hours * rate, 2)

