import json

# Python dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "Kathmandu"
}

# Convert Python dictionary to JSON string
json_data = json.dumps(person, indent=4)
print(json_data)

# Convert JSON string back to Python dictionary
data = json.loads(json_data)
print(data["name"])
