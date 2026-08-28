raw ="22, 80, 443, 3306"
ports= raw.split(",")

clean_port = []
for p in ports:
    clean_port.append(p.strip())

print(clean_port)

print("-------------------------------------")

clean_ports=[p.strip() for p in ports]

integer=[ int(p.strip()) for p in clean_ports]

print(clean_ports)
print(integer)
