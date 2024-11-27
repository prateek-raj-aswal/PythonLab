import json

data = {'name': 'Alice', 'age': 25, 'city': 'Wonderland'}
json_string = json.dumps(data)  # Convert Python dict to JSON string
print(json_string)

# Convert JSON string back to Python dict
python_dict = json.loads(json_string)
print(python_dict['name'])
