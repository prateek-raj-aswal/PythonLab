import json

# Write to JSON
data = {"name": "Alice", "age": 25, "city": "New York"}
with open('data.json', 'w') as file:
    json.dump(data, file)
    print("Data written to data.json.")

# Read from JSON
with open('data.json', 'r') as file:
    read_data = json.load(file)
    print("Read JSON Data:")
    print(read_data)
