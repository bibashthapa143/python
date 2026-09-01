port_services = {22: "SSH", 80: "HTTP", 443: "HTTPS"}

# try:
#     port = int(input("Enter a port number: "))
#     service = port_services.get(port, "Unknown service")
#     print(f"Port {port}: {service}")
# except ValueError:
#     print("Please enter a valid number, not text.")


#except with multiple error types
try:
    port = int(input("Enter a port: "))
except ValueError:
    print("Invalid input.")
else:
    print(f"Got a valid port: {port}")  # runs only if NO error happened
finally:
    print("Done checking.")  # always runs, error or not
