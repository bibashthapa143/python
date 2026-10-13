import json

# Get user details
name = input("Enter your name: ")
age = input("Enter your age: ")

# Store data in dictionary
user = {
    "name": name,
    "age": age
}

# Save data to JSON file
with open("user.json", "w") as file:
    json.dump(user, file)

# Read data from JSON file
with open("user.json", "r") as file:
    data = json.load(file)

print("Name:", data["name"])
print("Age:", data["age"])
