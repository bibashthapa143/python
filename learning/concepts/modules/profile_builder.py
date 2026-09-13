import argparse

parser = argparse.ArgumentParser(description = "Simple profile builder")
parser.add_argument("--name", type=str)
parser.add_argument("--age", type=int)
parser.add_argument("--student", action="store_true")

args = parser.parse_args()
print(f"Name : {args.name}")
print(f"Age : {args.age}")
if args.student == True:
    print(f"Student")
else:
    print("Not a student")




