import argparse   # lets us accept input directly from the command line instead of input()

# Step 1: declare what arguments this script accepts
parser = argparse.ArgumentParser(description="Simple profile builder")
parser.add_argument("--name", type=str)               # expects text after --name
parser.add_argument("--age", type=int)                 # expects a whole number after --age
parser.add_argument("--student", action="store_true")  # a flag: True if present, False if not (no value needed)

# Step 2: actually read what the user typed and store it in "args"
args = parser.parse_args()

# Step 3: use the values like normal variables
print(f"Name : {args.name}")
print(f"Age : {args.age}")

if args.student:            # True if --student flag was passed, False otherwise
    print(f"Student")
else:
    print("Not a student")
