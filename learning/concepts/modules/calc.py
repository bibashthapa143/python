import argparse

# Create the command-line argument parser
parser = argparse.ArgumentParser(description="Simple calculator")

# Add an argument for the first number
parser.add_argument("--a", type=int)

# Add an argument for the second number
parser.add_argument("--b", type=int)

# Add an argument for the mathematical operator
parser.add_argument("--operator", type=str)

# Parse the arguments provided by the user
args = parser.parse_args()

# Perform addition if the operator is "+"
if args.operator == "+":
    print(args.a + args.b)

# Perform subtraction if the operator is "-"
elif args.operator == "-":
    print(args.a - args.b)
