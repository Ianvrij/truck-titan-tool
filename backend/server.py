
pip install Flask
python backend/server.py

from flask import Flask, request, jsonify

app = Flask(__name__)

# Home route for testing
@app.route('/')
def home():
    return "Welcome to the Truck Titan Tool!"

# Example route for calculating potential savings (you can modify this based on your logic)
@app.route('/api/calculate', methods=['POST'])
def calculate_savings():
    data = request.get_json()  # Get data sent in the request body
    
    # Example: Extract data
    distance = data.get('distance')
    load_capacity = data.get('load_capacity')
    
    # Perform your calculations here (e.g., savings or emissions)
    savings = distance * load_capacity * 0.1  # This is just an example calculation
    
    # Return the result as JSON
    return jsonify({'savings': savings})

if __name__ == '__main__':
    app.run(debug=True)

