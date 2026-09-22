# Read ports as integers
with open("ports.txt", "r") as f:
    ports = [int(line.strip()) for line in f]

print(ports)

print("-------------------------------")

# Read and print the file content
with open("ports.txt", "r") as file:
    content = file.read()
    print(content)

print("------------------------------")

# Append new ports and read the file
with open("ports.txt", "a+") as file:
    file.write("500\n")
    file.write("100\n")
    file.seek(0)
    content = file.read()
    print(content)

print("----------------------")

# Overwrite the file and read the new content
with open("ports.txt", "w+") as file:
    a = "Apple\n"
    b = "ball"

    file.write(a)
    file.write(b)
    file.seek(0)

    print(file.read())
