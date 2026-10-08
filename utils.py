from math import ceil

def calculate_trip_cost(distance, fuel_consumption, fuel_price):
    fuel_needed = (distance * fuel_consumption) / 100
    raw_cost = fuel_needed * fuel_price
    return ceil(raw_cost)

# 2. Розрахунок для поїздки Київ — Малин
kyiv_malyn_distance = 105
avg_fuel_consumption = 8.0
current_fuel_price = 98.0

total_cost = calculate_trip_cost(
    distance=kyiv_malyn_distance,
    fuel_consumption=avg_fuel_consumption,
    fuel_price=current_fuel_price
)

print(f"Орієнтовна вартість поїздки з Києва в Малин: {total_cost} грн")