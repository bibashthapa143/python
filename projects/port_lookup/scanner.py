import socket                                                  # built-in module for network connections

port_services = {                                              # known port -> service name mapping
    21: "FTP", 22: "SSH", 80: "HTTP", 443: "HTTPS", 5500: "HTTP-ALT"
}

def scan_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # create a TCP connection tool (boilerplate)
    sock.settimeout(1)                                          # give up after 1 second instead of hanging

    try:
        result = sock.connect_ex((target, port))                # try connecting; 0 = success (open)
    except socket.gaierror:
        sock.close()                                            # close before exiting
        return "invalid_address"                                # signal: stop scanning entirely
    except socket.error:
        result = -1                                             # treat any other socket error as closed/unreachable

    sock.close()                                                # always close the connection when done
    service = port_services.get(port, "Unknown service")        # look up the service name for this port

    if result == 0:
        print(f"Port {port} ({service}): OPEN")                 # connection succeeded
        return "open"                                            # signal: this port was open

    return "closed"                                              # signal: normal result, keep scanning


target = input("Enter target IP to scan: ")                     # ask user which address to scan

while True:
    try:
        port_range = input("Enter port range (e.g. 1-100): ")           # ask user for the range to scan
        start, end = port_range.split("-")
        start=int(start)
        end =int(end)

        if start > end:
            start, end = end, start     #swap them automatically

        print(f"scanning from {start} to {end}")
        break   #valid input received, exit the loop

    except ValueError:
        print("Invalid range format. Please use format like 1-100")

found_open = False                                               # track whether any open port was found

for port in range((start), (end) + 1):                    # check every port in the given range
    status = scan_port(target, port)

    if status == "invalid_address":
        print("Invalid or unreachable address — stopping scan.")
        break                                                     # exit the loop early, don't check remaining ports

    if status == "open":
        found_open = True                                        # remember that we found at least one

if not found_open:
        print("No open ports found in that range.")                 # friendly message if nothing was open
