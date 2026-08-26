# Look up the service name for a given port number.
# Falls back to "not found" if the port isn't in our dictionary.
def lookup_service(port, services_dict):
    return services_dict.get(port, "not found")


# Known ports mapped to their common services
port_services = {
    21: "FTP",
    22: "SSH",
    80: "HTTP"
}

# Get one or more ports from the user, separated by commas
user_input = input("Enter ports separated by commas: ")
parts = user_input.split(",")  # e.g. "22, 80" -> ['22', ' 80']

# Convert each piece of text into an actual integer
ports = []
for p in parts:
    ports.append(int(p))

# Check every port the user entered and print its service
# for port in ports:
#     service = lookup_service(port, port_services)
#     print(f"Port {port} -> {service}")

def check(n):
    service= lookup_service(n, port_services)
    print(f"Port :{n} -> {service}")


for port in ports:
    check(port)
