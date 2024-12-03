import pandas as pd

# Load your Excel data here
def load_datasets():
    # Example: load the truck specifications dataset
    truck_specs = pd.read_excel('truck_specs.xlsx')
    emissions_data = pd.read_excel('emissions_data.xlsx')
    subsidies_data = pd.read_excel('subsidies_data.xlsx')
    return truck_specs, emissions_data, subsidies_data

# Function to calculate potential savings
def calculate_savings(license_plate, distance_traveled, load_capacity, truck_lifetime):
    truck_specs, _, _ = load_datasets()
    # Example logic for calculating savings based on the truck's fuel efficiency and maintenance cost
    truck = truck_specs[truck_specs['license_plate'] == license_plate].iloc[0]
    fuel_efficiency = truck['fuel_efficiency']
    maintenance_cost = truck['maintenance_cost']
    
    # Calculate fuel cost savings (example calculation)
    fuel_price = 1.5  # Example fuel price per liter
    fuel_used = distance_traveled / fuel_efficiency  # Calculate fuel used for the trip
    fuel_cost = fuel_used * fuel_price
    total_maintenance_cost = maintenance_cost * truck_lifetime
    
    # Return total savings (simplified)
    savings = fuel_cost + total_maintenance_cost
    return f"€{savings:.2f}"

# Function to calculate CO2 emissions
def calculate_emissions(license_plate, distance_traveled):
    _, emissions_data, _ = load_datasets()
    truck_emissions = emissions_data[emissions_data['license_plate'] == license_plate].iloc[0]
    emission_factor = truck_emissions['co2_emission_factor']  # CO2 emission in grams per kilometer
    total_emissions = emission_factor * distance_traveled  # Total emissions for the distance traveled
    return f"{total_emissions:.2f} grams of CO2"

# Function to recommend subsidies
def recommend_subsidies(license_plate):
    _, _, subsidies_data = load_datasets()
    # Example: recommend subsidies based on Euro class
    truck = pd.read_excel('truck_specs.xlsx')[pd.read_excel('truck_specs.xlsx')['license_plate'] == license_plate]
    euro_class = truck['euro_class'].iloc[0]
    
    eligible_subsidies = subsidies_data[subsidies_data['euro_class'] == euro_class]
    return eligible_subsidies['subsidy_name'].tolist()
