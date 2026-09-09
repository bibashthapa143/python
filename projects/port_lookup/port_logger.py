port_services = {21: "FTP", 22: "SSH", 80: "HTTP", 443: "HTTPS"}

def lookup_port(port):
    return port_services.get(port, "Unknown")

with open("ports_input.txt", "r") as infile, open("ports_output.txt", "w") as outfile:
    for line in infile:
        line = line.strip()
        try:
            port = int(line)
            service = lookup_port(port)
            outfile.write(f"{port}: {service}\n")
        except ValueError:
            outfile.write(f"Skipping invalid entry: {line}\n")

print("Done! Check ports_output.txt")
