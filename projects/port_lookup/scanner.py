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
    else:
        print(f"Port {port} ({service}): CLOSED")                # connection failed

    return "ok"                                                  # signal: normal result, keep scanning

target = input("Enter target IP to scan: ")                     # ask user which address to scan

for port in port_services:                                       # check every port in the dictionary
    status = scan_port(target, port)
    if status == "invalid_address":
        print("Invalid or unreachable address — stopping scan.")
        break                                                     # exit the loop early, don't check remaining ports
