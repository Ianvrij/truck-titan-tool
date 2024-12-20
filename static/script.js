function sendData() {
  // Gather data from the inputs
  const distance = document.getElementById('distance').value;
  const fuelEfficiency = document.getElementById('fuel_efficiency').value;
  const emissionFactor = 2.31;  // Example emission factor (kg CO2 per liter of fuel)

  // Prepare the data to send to the backend
  const data = {
    distance: distance,
    fuel_efficiency: fuelEfficiency,
    emission_factor: emissionFactor
  };

  // Send the data to the backend via a POST request
  fetch('http://127.0.0.1:5000/api/calculate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
  .then(response => response.json())
  .then(result => {
    // Show the result in the webpage
    document.getElementById('result').innerText = 'Total Fuel Cost: €' + result.total_fuel_cost;
    document.getElementById('emissions').innerText = 'Total CO2 Emissions: ' + result.total_emissions + ' kg';
  })
  .catch(error => console.error('Error:', error));
}

