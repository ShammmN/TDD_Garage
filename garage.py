def enter_garage(garage, car_id, entry_hour):
    if car_id in garage["cars"]:
        raise ValueError("Car is already in garage!")
    if len(garage["cars"]) >= garage["capacity"]:
        raise ValueError("Garage is full")
    if not isinstance(entry_hour, int):
        raise TypeError("Entry hour must be int")

    garage["cars"].append(car_id)
    return garage

def exit_garage(garage, car_id):
    if car_id not in garage["cars"]:
        raise KeyError("Car is not in garage!")
        
    garge["cars"].pop(car_id)
    return garage
def get_available_spots(garage):
    pass

def calculate_fee(hours, rate):
    pass

