from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def index():
    return "Truck Titan Tool is running!"

@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.json
    # Dummy calculation for now
    distance = data.get('distance')
    load_capacity = data.get('load_capacity')

    # You will replace this with your real calculation later
    tco = distance * load_capacity * 0.1  # Just an example formula
    
    return jsonify({
        "tco": tco,
        "distance": distance,
        "load_capacity": load_capacity
    })

if __name__ == "__main__":
    app.run(debug=True)
