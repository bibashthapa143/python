import socket                                                    # built-in module for network connections
from services import port_services                               # port -> service name mapping, kept separate

# ============================================================================
# SHARED HELPER
# ============================================================================

def lookup_services(port, services_dict):
    return services_dict.get(port, "notfound")


def get_valid_port(prompt):
    """Keep asking until the user gives an integer between 0 and 65535."""
    while True:
        try:
            port = int(input(prompt))
        except ValueError:
            print("Invalid input — please enter a whole number.")
            continue

        if port < 0 or port > 65535:
            print("Port must be between 0 and 65535.")
            continue

        return port


# ============================================================================
# MODE 1: RANGE LOOKUP  (look up a range of ports against the dictionary)
# ============================================================================

def lookup_range():
    start_port = get_valid_port("Enter start port: ")
    end_port = get_valid_port("Enter end port: ")

    if start_port > end_port:
        start_port, end_port = end_port, start_port   # swap so the range always makes sense
        print(f"Swapped order — scanning {start_port} to {end_port}")

    for port in range(start_port, end_port + 1):
        service = lookup_services(port, port_services)
        if service != "notfound":
            print(f"Port {port} -> {service}")


# ============================================================================
# MODE 2: FILE LOOKUP  (read ports from a file, write results to another)
# ============================================================================

def lookup_from_file(input_file="ports_input.txt", output_file="ports_output.txt"):
    try:
        infile = open(input_file, "r")
    except FileNotFoundError:
        print(f"Error: '{input_file}' not found. Check the filename/path and try again.")
        return
    except PermissionError:
        print(f"Error: no permission to read '{input_file}'.")
        return

    try:
        with infile, open(output_file, "w") as outfile:
            for line in infile:
                line = line.strip()
                if not line:
                    continue                          # skip blank lines quietly
                try:
                    port = int(line)
                    if port < 0 or port > 65535:
                        outfile.write(f"Skipping out-of-range port: {line}\n")
                        continue
                    service = lookup_services(port, port_services)
                    outfile.write(f"{port}: {service}\n")
                except ValueError:
                    outfile.write(f"Skipping invalid entry: {line}\n")
    except PermissionError:
        print(f"Error: no permission to write '{output_file}'.")
        return
    except OSError as e:
        print(f"Unexpected file error: {e}")
        return

    print(f"Done! Check {output_file}")


# ============================================================================
# MODE 3: LIVE SCAN — CORE SCANNING LOGIC
# ============================================================================

def scan_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # create a TCP connection tool (boilerplate)
    sock.settimeout(1)                                            # give up after 1 second instead of hanging

    try:
        result = sock.connect_ex((target, port))                  # try connecting; 0 = success (open)
    except socket.gaierror:
        sock.close()                                              # close before exiting
        return "invalid_address"                                  # signal: stop scanning entirely
    except socket.timeout:
        sock.close()
        return "closed"                                            # timeout = treat as closed, keep scanning
    except OSError as e:
        sock.close()
        print(f"Socket error on port {port}: {e}")
        return "closed"                                            # treat any other socket error as closed/unreachable

    sock.close()                                                  # always close the connection when done
    service = port_services.get(port, "Unknown service")          # look up the service name for this port

    if result == 0:
        print(f"Port {port} ({service}): OPEN")                   # connection succeeded
        return "open"                                              # signal: this port was open

    return "closed"                                                # signal: normal result, keep scanning


# ============================================================================
# MODE 3: LIVE SCAN — USER-FACING LOOP
# ============================================================================

def live_scan():
    target = input("Enter target IP to scan: ").strip()           # ask user which address to scan
    if not target:
        print("Error: target cannot be empty.")
        return

    while True:
        try:
            port_range = input("Enter port range (e.g. 1-100): ")         # ask user for the range to scan
            start, end = port_range.split("-")
            start = int(start)
            end = int(end)

            if start < 0 or end > 65535:
                print("Ports must be between 0 and 65535.")
                continue

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


# ============================================================================
# ENTRY POINT
# ============================================================================

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
