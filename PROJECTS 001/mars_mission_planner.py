# 🪐 Mars Mission Planner — Challenge Steps
#
# 1. Write a function to calculate how long it takes
#    to reach Mars at a given speed.
#    - Mars' average distance is 225,000,000 km.
#    - Use the formula: time = distance ÷ speed
#    - Round the result to the nearest hour.
#
# 2. Write another function to figure out the total fuel cost
#    for a mission.
#    - Formula: total cost = distance × fuel usage × price per liter
#
# 3. Test your functions with the provided mission data:
#    - Pathfinder: 40,000 km/h
#    - Perseverance: 75,000 km/h
#    - Starship: 120,000 km/h
#    - Each mission travels 225 million km,
#      burns 0.3 liters/km, and fuel costs $1.80/L.

#
# 4. For each mission, print a report showing:
#    - Mission name
#    - Travel time (hours)
#    - Total fuel cost

MARS_DISTANCE_KM = 225_000_000

# 1. Function to calculate travel time (rounded to nearest hour)
def calculate_travel_time(speed_kmh):
    time = MARS_DISTANCE_KM / speed_kmh
    return round(time)

# 2. Function to calculate total fuel cost
def calculate_fuel_cost(distance_km, fuel_usage_per_km, price_per_liter):
    return distance_km * fuel_usage_per_km * price_per_liter

# 3. Mission data
missions = [
    {"name": "Pathfinder", "speed": 40_000},
    {"name": "Perseverance", "speed": 75_000},
    {"name": "Starship", "speed": 120_000}
]

FUEL_USAGE_PER_KM = 0.3
FUEL_PRICE_PER_LITER = 1.80

# 4. Print report for each mission
for mission in missions:
    travel_time = calculate_travel_time(mission["speed"])
    total_fuel_cost = calculate_fuel_cost(
        MARS_DISTANCE_KM,
        FUEL_USAGE_PER_KM,
        FUEL_PRICE_PER_LITER
    )
    print(f"Mission: {mission['name']}")
    print(f"  Travel time: {travel_time} hours")
    print(f"  Total fuel cost: ${total_fuel_cost:,.2f}")
    print('---')


