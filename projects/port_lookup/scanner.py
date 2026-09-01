import socket                                              # built-in module for network connections

port_services = {                                          # known port -> service name mapping
    21: "FTP", 22: "SSH", 80: "HTTP", 443: "HTTPS", 8080: "HTTP-ALT"
}

def scan_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # create a TCP connection tool (boilerplate)
    result = sock.connect_ex((target, port))                   # try connecting; 0 = success (open)
    sock.close()                                                # always close the connection when done

    service = port_services.get(port, "Unknown service")       # look up the service name for this port

    if result == 0:
        print(f"Port {port} ({service}): OPEN")                # connection succeeded
    else:
        print(f"Port {port} ({service}): CLOSED")               # connection failed

target = "127.0.0.1"                                        # 127.0.0.1 = your own machine (localhost)
for port in port_services:                                  # check every port in the dictionary
    scan_port(target, port)
