# name & greeting are normal parameters
# greeting has a default value, used only if not provided
# *hobbies collects any extra positional arguments into a tuple
# **extra collects any extra keyword arguments into a dictionary

def profile(name, greeting="Hello", **extra):
    print(f"{greeting}, {name}!")          # uses default or given greeting
               # tuple of extra positional args
    print(f"Extra info: {extra}")           # dictionary of extra keyword args

profile(
    "Eros",
        # goes into *hobbies as a tuple
    college="Morgan International College",  # goes into **extra as a dict
    age=20
)
