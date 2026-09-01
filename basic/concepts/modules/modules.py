# 1. Built-in module
# Python provides many modules that are already included.
import random

number = random.randint(1, 100)
print("Random number:", number)


# 2. Importing a specific function from a built-in module
# We can import only the function we need.
from math import sqrt

result = sqrt(25)
print("Square root:", result)


# 3. Importing a module with an alias
# 'datetime' is renamed to 'dt' for shorter code.
import datetime as dt

today = dt.date.today()
print("Today's date:", today)


# 4. User-defined module
# A module can be a Python file created by you.
# Example: suppose we have a file named mymodule.py
#
# import mymodule
# mymodule.greet()


# 5. Third-party module
# These modules are installed separately using tools like pip.
# Example:
#
# import requests
# response = requests.get("https://example.com")
# print(response.status_code)


# 6. Importing everything from a module
# This is possible, but generally not recommended for large programs.
#
# from math import *
# print(sin(0))
