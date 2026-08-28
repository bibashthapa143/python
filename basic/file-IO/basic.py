with open("ports.txt", "r") as f:
    content = f.read() #f.read reads entire file as one big string

print(content)

print("------------------------------------------------------")
#Reading line by line (more common for lists of things)
with open("ports.txt", "r") as f:
    for line in f:
        clean_line = line.strip()
        print(clean_line)

print("---------------------------------------------------------")
#Reading all lines into a list at once
with open("ports.txt", "r") as f:
    lines = f.readlines()

print(lines)
# ['22\n', '80\n', '443\n', '3306\n']

ports = [int(line.strip()) for line in lines]
print(ports)
# [22, 80, 443, 3306]

print("------------------------------------------")
#Writing to a file
with open("output.txt", "w") as f:
    f.write("Port 443 is open\n")
    f.write("Port 22 is open\n")


