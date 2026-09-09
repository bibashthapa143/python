import socket                                                    # built-in module for network connections
from services import port_services                               # port -> service name mapping, kept separate


def lookup_services(port, services_dict):
    return services_dict.get(port, "notfound")


def lookup_range():
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    for port in range(start_port, end_port + 1):
        service = lookup_services(port, port_services)
        if service != "notfound":
            print(f"Port {port} -> {service}")


def lookup_from_file(input_file="ports_input.txt", output_file="ports_output.txt"):
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            line = line.strip()
            try:
                port = int(line)
                service = lookup_services(port, port_services)
                outfile.write(f"{port}: {service}\n")
            except ValueError:
                outfile.write(f"Skipping invalid entry: {line}\n")

    print(f"Done! Check {output_file}")


def scan_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # create a TCP connection tool (boilerplate)
    sock.settimeout(1)                                            # give up after 1 second instead of hanging

    try:
        result = sock.connect_ex((target, port))                  # try connecting; 0 = success (open)
    except socket.gaierror:
        sock.close()                                              # close before exiting
        return "invalid_address"                                  # signal: stop scanning entirely
    except socket.error:
        result = -1                                                # treat any other socket error as closed/unreachable

    sock.close()                                                  # always close the connection when done
    service = port_services.get(port, "Unknown service")          # look up the service name for this port

    if result == 0:
        print(f"Port {port} ({service}): OPEN")                   # connection succeeded
        return "open"                                              # signal: this port was open

    return "closed"                                                # signal: normal result, keep scanning


def live_scan():
    target = input("Enter target IP to scan: ")                   # ask user which address to scan

    while True:
        try:
            port_range = input("Enter port range (e.g. 1-100): ")         # ask user for the range to scan
            start, end = port_range.split("-")
            start = int(start)
            end = int(end)

            if start > end:
                start, end = end, start       # swap them automatically

            print(f"scanning from {start} to {end}")
            break     # valid input received, exit the loop

        except ValueError:
            print("Invalid range format. Please use format like 1-100")

    found_open = False                                             # track whether any open port was found
    status = None

    for port in range(start, end + 1):                      # check every port in the given range
        status = scan_port(target, port)

        if status == "invalid_address":
            print("Invalid or unreachable address — stopping scan.")
            break                                                   # exit the loop early, don't check remaining ports

        if status == "open":
            found_open = True                                      # remember that we found at least one

    if not found_open and status != "invalid_address":
        print("No open ports found in that range.")


if __name__ == "__main__":
    mode = input("Choose mode - (r)ange lookup, (f)ile lookup, (s)can live: ").strip().lower()

    if mode == "r":
        lookup_range()
    elif mode == "f":
        lookup_from_file()
    elif mode == "s":
        live_scan()
    else:
        print("Invalid choice. Enter 'r', 'f', or 's'.")
