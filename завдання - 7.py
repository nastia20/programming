import math
def calculate_buses(people, bus_capacity):
    buses_needed = math.ceil(people / bus_capacity)

    return buses_needed
