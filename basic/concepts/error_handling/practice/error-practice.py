port_services = {
    21: "FTP", 22: "SSH", 80: "HTTP", 443: "HTTPS", 8080: "HTTP-ALT"
}

try:
    port = int(input("Enter port number: "))       # try converting input to int
    service = port_services.get(port, "unknown port")  # lookup, safe even if not found
except ValueError:
    print("Invalid inputs!!!!!!!!!!!!")             # runs only if int() fails
else:
    print(f"port {port}:{service}")                 # runs only if try succeeded
finally:
    print("Check complete!!!!!")                    # always runs, error or not
