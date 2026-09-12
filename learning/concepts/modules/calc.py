import argparse

parser = argparse.ArgumentParser(description="Simple calculator")
parser.add_argument("--a", type=int)
parser.add_argument("--b", type=int)
parser.add_argument("--operator", type=str)

args = parser.parse_args()

if args.op == "+":
    print(args.a + args.b)
elif args.op == "-":
    print(args.a - args.b)
