import requests
import base64

# Define the URL of the FastAPI server
url = "http://127.0.0.1:8000/moondream"

# Path to the image you want to test with
image_path = "2banana.jpg"

# Open the image file in binary mode
with open(image_path, "rb") as image_file:
    # Read image data
    image_data = image_file.read()

# Encode image data in base64
encoded_image = base64.b64encode(image_data).decode()

# Prepare the payload for the POST request
payload = {"image": encoded_image}

# Send a POST request with the payload
response = requests.post(url, json=payload)

# Print the response from the server
print(response.json())
