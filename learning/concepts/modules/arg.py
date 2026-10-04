import argparse  # Import Python's argparse module

parser = argparse.ArgumentParser()  # Create a parser to handle command-line arguments


parser.add_argument(
    "--something",
    required=True
)  # Required optional-style argument; the user must provide --something

parser.add_argument(
    "--nothing"
)  # Optional argument; the user can provide --nothing or leave it out

parser.add_argument(
    "--number",
    type=int,
    default=10,
    help="The number to use",
    nargs="+"
)  # Accepts one or more integers; uses 10 if --number is not provided

parser.add_argument(
    "--verbose",
    action="store_true"
)  # Boolean flag; True if --verbose is provided, otherwise False

parser.add_argument(
    "--color",
    choices=["red", "blue", "green"]
)  # Only allows red, blue, or green as the value





args = parser.parse_args()  # Read the command-line arguments and store them in args

print(f"Something: {args.something}")  # Print the value provided for --something

print(f"Nothing: {args.nothing}")  # Print the value of --nothing (None if not provided)

print(f"Age: {args.number}")  # Print the number(s) provided for --number

if args.verbose:  # Check if --verbose was included in the command
    print(f"args.verbose= {args.verbose}")  # Print True when --verbose is present

print(f"Color: {args.color}")  # Print the selected color (None if not provided)


