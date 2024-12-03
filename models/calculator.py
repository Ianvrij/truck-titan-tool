# Function to calculate savings
def calculate_savings(license_plate, distance_traveled, load_capacity, truck_lifetime):
    # Example savings calculation based on distance and load
    fuel_cost_per_km = 0.5  # Example value, could be based on actual fuel efficiency
    total_savings = distance_traveled * load_capacity * fuel_cost_per_km
    return total_savings

# Function to calculate emission reduction
def calculate_emissions(license_plate, distance_traveled):
    # Example emission calculation based on distance
    emission_factor = 2.31  # CO2 emissions per liter of fuel
    total_emissions = distance_traveled * emission_factor
    return total_emissions

# Function to recommend subsidies (just a placeholder example)
def recommend_subsidies(license_plate):
    # Example of a fixed subsidy recommendation
    subsidies = {
        'electric_truck': 5000,
        'hybrid_truck': 2000,
    }
    return subsidies
