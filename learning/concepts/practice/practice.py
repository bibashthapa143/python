# classify_ports.py

services = {22: "ssh", 80: "http", 443: "https"}  # port: service name

def classify(ports):
    result = {}
    for port in ports:
        result[port] = services.get(port, "UNKNOWN")
    return result

if __name__ == "__main__":
    all_ports = set()                                 # set: no duplicates

    while True:
        user_input = input("Enter ports (done to finish): ")

        if user_input.lower() == "done":              # stop collecting
            break

        try:
            ports = [int(p) for p in user_input.split(",")]
        except ValueError:
            print("Invalid input")
            continue

        if any(p < 1 or p > 65535 for p in ports):
            print("Port out of range (1-65535)")
            continue

        all_ports.update(ports)                       # add to collection, no output yet

    results = classify(all_ports)                     # classify everything once
    known = 0
    unknown = 0

    for port in sorted(results):
        print(f"{port} -> {results[port]}")
        if results[port] == "UNKNOWN":
            unknown += 1
        else:
            known += 1

    print(f"Total: {len(results)}, Known: {known}, Unknown: {unknown}")
