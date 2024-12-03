from flask import Flask, request, jsonify
from calculations import calculate_tco, calculate_emissions, calculate_savings, calculate_subsidy

app = Flask(__name__)

# Home route for testing
@app.route('/')
def home():
    return "Welcome to the Truck Titan Tool!"

# Route for calculating savings and emissions
@app.route('/api/calculate', methods=['POST'])
def calculate_savings_and_emissions():
    data = request.get_json()
    
    # Extract data
    distance = data.get('distance')
    load_capacity = data.get('load_capacity')
    fuel_cost = data.get('fuel_cost')
    insurance_cost = data.get('insurance_cost')
    maintenance_cost = data.get('maintenance_cost')
    euro_class = data.get('euro_class')
    
    # Perform calculations
    tco = calculate_tco(fuel_cost, insurance_cost, maintenance_cost)
    emissions = calculate_emissions(euro_class, distance)
    savings = calculate_savings(tco, load_capacity * fuel_cost)  # Example savings calculation
    subsidy = calculate_subsidy(data.get('vehicle_type'), euro_class)

    # Return calculated results
    return jsonify({
        'tco': tco,
        'emissions': emissions,
        'savings': savings,
        'subsidy': subsidy
    })

if __name__ == '__main__':
    app.run(debug=True)
