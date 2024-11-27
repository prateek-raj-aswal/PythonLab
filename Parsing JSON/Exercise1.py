import json

# Step 1: Create the dictionary
data = {
    "name": "Alice",
    "age": 25,
    "is_student": False,
    "hobbies": ["reading", "coding", "traveling"],
    "address": {"city": "Wonderland", "postcode": "12345"}
}

# Step 2: Serialize the dictionary to a JSON string
json_string = json.dumps(data, indent =1)
print("Serialized JSON String:")
print(json_string)

# Step 3: Deserialize the JSON string back to a Python dictionary
deserialized_data = json.loads(json_string)

# Step 4: Print the name and city values
print("\nDeserialized Data:")
print(f"Name: {deserialized_data['name']}")
print(f"City: {deserialized_data['address']['city']}")
