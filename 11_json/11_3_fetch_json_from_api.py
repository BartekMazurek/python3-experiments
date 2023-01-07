# FETCH JSON FROM API
import json.decoder
import requests

try:
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    data = response.json()

except json.decoder.JSONDecodeError:
    print('Wrong JSON structure')

else:
    print('Parsed data :', data)
