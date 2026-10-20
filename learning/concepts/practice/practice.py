# classify_ports.py

services = {22: "ssh", 80: "http", 443: "https"}  # port: service name

def classify(ports):
    result = {}
    for port in ports:                                # check each port
        result[port] = services.get(port, "UNKNOWN")  # UNKNOWN if not found
    return result

if __name__ == "__main__":
    while True:
        user_input = input("Enter ports (or q to quit): ")

        if user_input.lower() == "q":                 # exit condition
            break

        try:
            ports = [int(p) for p in user_input.split(",")]
        except ValueError:                            # letters, empty input
            print("Invalid input")
            continue

        if any(p < 1 or p > 65535 for p in ports):    # range check
            print("Port out of range (1-65535)")
            continue

        results = classify(ports)
        known = 0                                     # reset on every input
        unknown = 0

        for port in sorted(results):                  # ports in order
            service = results[port]
            print(f"{port} -> {service}")

            if service == "UNKNOWN":                  # count each type
                unknown += 1
            else:
                known += 1

        print(f"Known: {known}, Unknown: {unknown}")
