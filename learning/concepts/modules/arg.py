import argparse 

parser = argparse.ArgumentParser(description="Show name and address")

parser.add_argument("name", help="Your name")
parser.add_argument("-a","--address",default="Not given", help="Your address")

args = parser.parse_args()

print(f"Name: {args.name}")
print(f"Address: {args.address}")



