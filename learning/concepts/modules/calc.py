import argparse

# Create calculator parser
parser = argparse.ArgumentParser(description="Simple calculator")

parser.add_argument("--a", type=int)          # First number
parser.add_argument("--b", type=int)          # Second number
parser.add_argument("--operator", type=str)   # Operator

args = parser.parse_args()

# Perform calculation
if args.operator == "+":
    print(args.a + args.b)
elif args.operator == "-":
    print(args.a - args.b)
