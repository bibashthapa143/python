# Create a list containing three languages
language = ["japanese", "nepali", "English"]

# Print the original list
print(language)

print("-------------")

# Add "chinese" to the end of the list
language.append("chinese")

# Print the list after adding an item
print(language)

print("---------------")

# Remove "japanese" from the list
language.remove("japanese")

# Find the number of items in the list
n = len(language)

# Loop through the list using indexes
for i in range(n):
    print(language[i])

print("----------------")

# Easier way to loop through the list
for lang in language:
    print(lang)
