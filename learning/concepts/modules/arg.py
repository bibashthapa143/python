import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--something", required=True)
parser.add_argument("--nothing")
parser.add_argument("--number", type=int, default=10)
parser.add_argument("--verbose", action="store_true")
parser.add_argument("--color", choices=["red", "blue", "green"])



args = parser.parse_args()

print(f"Something: {args.something}")
print(f"Nothing: {args.nothing}")
print(f"Age: {args.number}")
if args.verbose:
    print(f"args.verbose= {args.verbose}")
print(f"Color: {args.color}")


