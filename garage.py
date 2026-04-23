def enter_garage(garage, car_id, entry_hour):
    if car_id in garage["cars"]:
        raise ValueError("Car is already in garage!")

def exit_garage(garage, car_id):
    pass

def get_available_spots(garage):
    pass

def calculate_fee(hours, rate):
    pass

