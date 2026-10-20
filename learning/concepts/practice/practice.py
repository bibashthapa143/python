# classify_ports.py

services = {22: "ssh", 80: "http", 443: "https"}  # port: service name

def classify(ports):
    result = {}
    for port in ports:                                # check each port
        result[port] = services.get(port, "UNKNOWN")  # UNKNOWN if not found
    return result                                     # after the loop

if __name__ == "__main__":                            # run only when file is run directly
    while True:
        user_input = input("Enter ports (or q to quit): ")

        if user_input.lower() == "q":                 # exit condition
            break

        try:
            ports = [int(p) for p in user_input.split(",")]
        except ValueError:                            # letters, empty input, etc.
            print("Invalid input")
            continue

        # range check: any() is True if at least one port is bad
        if any(p < 1 or p > 65535 for p in ports):
            print("Port out of range (1-65535)")
            continue

        for port, service in classify(ports).items():
            print(f"{port} -> {service}")
