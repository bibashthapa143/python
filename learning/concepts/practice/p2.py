raw = "22, 80, 443, 3306"

# Split the string into individual ports
ports = raw.split(",")

# Clean extra spaces
clean_port = []
for p in ports:
    clean_port.append(p.strip())

print(clean_port)

print("-------------------------------------")

# Clean ports using list comprehension
clean_ports = [p.strip() for p in ports]

# Convert ports from strings to integers
integer = [int(p.strip()) for p in clean_ports]

print(clean_ports)
print(integer)
