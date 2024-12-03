from flask import Flask, render_template, request, jsonify
import pandas as pd
from calculator import calculate_savings, calculate_emissions, recommend_subsidies

app = Flask(__name__)

# Route to serve the frontend
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission and return calculations
@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    
    # Extract data from the request
    license_plate = data['licensePlate']
    distance_traveled = data['distanceTraveled']
    load_capacity = data['loadCapacity']
    truck_lifetime = data['truckLifetime']
    
    # Perform calculations
    savings = calculate_savings(license_plate, distance_traveled, load_capacity, truck_lifetime)
    emission_reduction = calculate_emissions(license_plate, distance_traveled)
    subsidies = recommend_subsidies(license_plate)
    
    # Return results as JSON
    return jsonify({
        'savings': savings,
        'emissionReduction': emission_reduction,
        'subsidies': subsidies
    })

if __name__ == '__main__':
    app.run(debug=True)
