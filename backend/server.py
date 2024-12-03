from flask import Flask, jsonify, request
from models.calculator import calculate_tco  # Import your function

app = Flask(__name__)

@app.route('/')
def index():
    return "Truck Titan Tool is running!"

@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.json
    distance = data.get('distance')
    load_capacity = data.get('load_capacity')

    # Use the calculate_tco function from calculator.py
    fuel_price = 1.5  # EUR per liter (dummy value)
    maintenance_cost = 1000  # EUR per year
    insurance_cost = 500  # EUR per year

    tco = calculate_tco(distance, load_capacity, fuel_price, maintenance_cost, insurance_cost)

    return jsonify({
        "tco": tco,
        "distance": distance,
        "load_capacity": load_capacity
    })

if __name__ == "__main__":
    app.run(debug=True)
