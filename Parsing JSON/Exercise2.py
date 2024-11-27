import json

# Step 1: Use the dictionary from Exercise 1
data = {
    "name": "Alice",
    "age": 25,
    "is_student": False,
    "hobbies": ["reading", "coding", "traveling"],
    "address": {"city": "Wonderland", "postcode": "12345"}
}

# Step 2: Write JSON data to a file
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)
print("Data written to data.json")

# Step 3: Read JSON data back from the file
with open("data.json", "r") as file:
    loaded_data = json.load(file)

# Step 4: Print the loaded data
print("\nLoaded Data from data.json:")
print(loaded_data)
