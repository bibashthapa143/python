with open ("ports.txt", "r") as f:
    ports=[int(line.strip()) for line in f]

print(ports)
