import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--score", type=int)
parser.add_argument("--scale", choices=["normal", "strict"], default="normal")

args = parser.parse_args()

if args.scale == "normal":
    if args.score >= 90:
        print("A")
    elif args.score >= 80:
        print("B")
    elif args.score >= 70:
        print("C")
    else:
        print("F")
else:
    if args.score >= 95:
        print("A")
    elif args.score >= 85:
        print("B")
    elif args.score >= 75:
        print("C")
    else:
        print("F")
