import requests

# Define the API endpoint
url = 'http://127.0.0.1:5000/predict'

# Define the JSON payload with the features
data = {
    "features": [6.0, 2.7, 5.1, 1.6]  # Replace these values with the features for prediction
}

# Send the POST request to the API
response = requests.post(url, json=data)

# Print the response from the server
print(response.json())
