services = {
    22: "ssh",
    80: "http",
    443: "https"
}

def classify(test_ports):
    result = {}
    for port in test_ports:
        if port in services:
            result[port] = services[port]
        else:
            result[port] = "unknown"
    return result


if __name__ == "__main__":
    test_ports = [22, 24, 30, 40, 80, 443, 999]
    classified = classify(test_ports)

    for port, service in classified.items():
        print(f"{port} -> {service}")
