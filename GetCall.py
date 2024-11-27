import requests
import json

response = requests.get('https://reqres.in/api/users?page=2')
json_data = response.json()
jsonString=json.dumps(json_data, indent=4)# Automatically parses the JSON
print(jsonString)
