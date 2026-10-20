# classify_ports.py

services = {22: "ssh", 80: "http", 443: "https"}  # port: service name

def classify(ports):
    result = {}
    for port in ports:                 # check each port
        result[port] = service.get(port, "UNKNOWN") # "unknown" if not found
    return result                      # after the loop

if __name__ == "__main__":             # run only when file is run directly
    classified = classify([22, 24, 80, 443, 999])
    for port, service in classified.items():   # port and service together
        print(f"{port} -> {service}")
