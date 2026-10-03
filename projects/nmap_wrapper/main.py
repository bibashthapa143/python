import argparse
import subprocess
import xml.etree.ElementTree as ET


def run_scan(target, ports):
    """Run nmap and return its output as XML text."""
    command = ["nmap", "-oX", "-"]              # -oX - = XML output to stdout
    if ports:                                   # add -p only if ports were given
        command += ["-p", ports]
    command.append(target)

    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=60)

        if result.returncode != 0:              # nmap itself failed
            print("Error:", result.stderr.strip())
            exit(1)

        if "Failed to resolve" in result.stderr or "Failed to resolve" in result.stdout:
            print("Could not resolve target:", target)   # nmap ran, target invalid
            exit(1)

        return result.stdout

    except FileNotFoundError:                   # nmap is not installed
        print("Nmap not installed!")
        exit(1)

    except subprocess.TimeoutExpired:           # scan ran longer than 60s
        print("Scan took too long and was stopped.")
        exit(1)


def parse_open_ports(xml_output):
    """Read nmap's XML and return a list of open TCP ports (as dictionaries)."""
    try:
        root = ET.fromstring(xml_output)        # turn XML text into a tree
    except ET.ParseError:                       # output was not valid XML
        print("Could not read nmap output.")
        exit(1)

    open_ports = []

    for port in root.iter("port"):              # go through every <port> tag
        if port.get("protocol") != "tcp":       # TCP only for now
            continue

        state = port.find("state").get("state")
        if state != "open":                     # skip closed/filtered ports
            continue

        service = port.find("service")          # <service> can be missing
        open_ports.append({
            "port": f"{port.get('portid')}/{port.get('protocol')}",   # e.g. 22/tcp
            "state": state,
            "service": service.get("name") if service is not None else "unknown",
        })

    return open_ports


def show_results(target, open_ports):
    """Print the open ports as a small table."""
    print(f"\nOpen ports on {target}:")

    if not open_ports:
        print("No open ports found.")
        return

    print(f"{'PORT':<12}{'STATE':<10}SERVICE")
    print("-" * 32)
    for p in open_ports:
        print(f"{p['port']:<12}{p['state']:<10}{p['service']}")

    print(f"\nTotal open ports: {len(open_ports)}")


def main():
    # ---- define the command-line arguments ----
    parser = argparse.ArgumentParser(description="Nmap wrapper - shows open ports only")
    parser.add_argument("--target", required=True, help="IP or hostname to scan")
    parser.add_argument("--ports", default="", help="Port range, e.g. 1-1000 (default: nmap default)")
    args = parser.parse_args()

    target = args.target.strip()
    ports = args.ports.strip()

    # ---- validate input ----
    if not target:
        parser.error("target cannot be empty")
    if target.startswith("-"):                  # stop nmap options sneaking in as target
        parser.error("target cannot start with '-'")

    # ---- scan -> parse -> show ----
    output = run_scan(target, ports)
    open_ports = parse_open_ports(output)
    show_results(target, open_ports)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:                   # Ctrl+C
        print("\nScan cancelled.")
