from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Truck Titan Tool Backend Running!'

@app.route('/calculate', methods=['POST'])
def calculate():
    # Accept data sent to the server as JSON
    data = request.get_json()

    # Get data from the request (example fields)
    distance = data.get('distance')  # Distance traveled in km
    fuel_efficiency = data.get('fuel_efficiency')  # Fuel efficiency (liters per km)

    # Example calculation: fuel cost
    fuel_cost_per_liter = 1.5  # Euro per liter of fuel (example value)
    total_fuel_cost = distance * fuel_efficiency * fuel_cost_per_liter

    # Send the result back to the frontend
    return jsonify({'total_fuel_cost': total_fuel_cost})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)  # Run the Flask app
