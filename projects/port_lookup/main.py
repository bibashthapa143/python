import socket                                                    # built-in module for network connections
import argparse                                                  # for parsing command-line flags
import logging                                                   # for logging scan activity to console + file
from services import port_services                               # port -> service name mapping, kept separate

# ============================================================================
# LOGGING SETUP
# ============================================================================

def setup_logging():
    logger = logging.getLogger("port_scanner")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()   # avoid duplicate handlers if setup_logging() is ever called twice

    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Console handler — shows in terminal while scanning
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # File handler — keeps a permanent record in scan.log
    file_handler = logging.FileHandler("scan.log")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


logger = setup_logging()


# ============================================================================
# CORE SCANNING LOGIC
# ============================================================================

def scan_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # create a TCP connection tool (boilerplate)
    sock.settimeout(1)                                            # give up after 1 second instead of hanging

    try:
        result = sock.connect_ex((target, port))                  # try connecting; 0 = success (open)
    except socket.gaierror:
        sock.close()                                              # close before exiting
        logger.error(f"Invalid or unreachable address: {target}")
        return "invalid_address"                                  # signal: stop scanning entirely
    except socket.timeout:
        sock.close()
        return "closed"                                            # timeout = treat as closed, keep scanning
    except OSError as e:
        sock.close()
        logger.warning(f"Socket error on port {port}: {e}")
        return "closed"                                            # treat any other socket error as closed/unreachable

    sock.close()                                                  # always close the connection when done
    service = port_services.get(port, "Unknown service")          # look up the service name for this port

    if result == 0:
        logger.info(f"Port {port} ({service}): OPEN")             # connection succeeded
        return "open"                                              # signal: this port was open

    return "closed"                                                # signal: normal result, keep scanning


# ============================================================================
# USER-FACING SCAN LOOP
# ============================================================================

def live_scan(target=None, port_range=None):
    if target is None:
        target = input("Enter target IP to scan: ").strip()       # ask user which address to scan
    else:
        target = target.strip()

    if not target:
        logger.error("Target cannot be empty.")
        return

    while True:
        try:
            if port_range is None:
                port_range = input("Enter port range (e.g. 1-100): ")     # ask user for the range to scan

            start, end = port_range.split("-")
            start = int(start)
            end = int(end)

            if start < 0 or end > 65535:
                print("Ports must be between 0 and 65535.")
                port_range = None
                continue

            if start > end:
                start, end = end, start       # swap them automatically

            break     # valid input received, exit the loop

        except ValueError:
            print("Invalid range format. Please use format like 1-100")
            port_range = None

    logger.info(f"Starting scan on {target}, ports {start}-{end}")

    found_open = False                                             # track whether any open port was found
    status = None

    for port in range(start, end + 1):                      # check every port in the given range
        status = scan_port(target, port)

        if status == "invalid_address":
            break                                                   # exit the loop early, don't check remaining ports

        if status == "open":
            found_open = True                                      # remember that we found at least one

    if status == "invalid_address":
        logger.info(f"Scan stopped early for {target} due to invalid address.")
    elif not found_open:
        logger.info(f"Scan complete for {target}: no open ports found in range {start}-{end}.")
    else:
        logger.info(f"Scan complete for {target}.")


# ============================================================================
# CLI ARGUMENT PARSING
# ============================================================================

def build_parser():
    parser = argparse.ArgumentParser(
        prog="port_scanner",
        description="Live TCP port scanner — checks a host for open ports."
    )
    parser.add_argument("--host", help="Target IP or hostname")
    parser.add_argument("--ports", help="Port range, e.g. 1-100")
    return parser


# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()

    if args.host and args.ports:
        live_scan(args.host, args.ports)
    else:
        # No CLI args given — fall back to interactive prompts
        live_scan()
