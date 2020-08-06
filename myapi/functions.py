import math


def get_fuel_tank(airplane_id: float) -> float:
    """A function to compute the fuel tank of an airplane"""
    return airplane_id * 200


def get_fuel_consumption(airplane_id: float, passenger: float) -> float:
    """A function to compute the fuel consumption of an airplane with regards to the number of passengers"""
    return (math.log(airplane_id) * 0.8) + (passenger * 0.002)



def get_maximum_mins(fuel_tank: float, fuel_consumption_per_minute: float) -> float:
    """A function to compute the maximum minutes an airplane able to fly"""
    return fuel_tank / fuel_consumption_per_minute


get_fuel_tank(1)
get_fuel_consumption(1, 2)
get_maximum_mins(200, 0.0014)
