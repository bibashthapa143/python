# Define a function to greet a person
def greet(name):
    print(f"Hello, {name}!")

# Call the greet function with the name "Eros"
greet("Eros")


# Ask the user to enter a number
a = int(input("Enter the number to check odd or even: "))


# Define a function to check whether a number is even
def is_even(n):
    return n % 2 == 0


# Call the function and store the result
result = is_even(a)

# Print True if the number is even, otherwise False
print(result)
