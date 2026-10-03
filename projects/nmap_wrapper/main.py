import argparse                                 # read --target / --ports from the terminal
import subprocess                               # run nmap from Python
import xml.etree.ElementTree as ET              # read nmap's XML output


def run_scan(target, ports):
    """Run nmap and return its output as XML text."""
    command = ["nmap", "-oX", "-"]              # -oX - = XML output to stdout
    if ports:                                   # add -p only if ports were given
        command += ["-p", ports]
    command.append(target)                      # e.g. ['nmap','-oX','-','-p','1-1000','host']

    try:
        # capture_output = save stdout/stderr, text = get strings, timeout = max 60s
        result = subprocess.run(command, capture_output=True, text=True, timeout=60)

        if result.returncode != 0:              # non-zero = nmap itself failed
            print("Error:", result.stderr.strip())
            exit(1)

        # nmap exits with 0 for a bad hostname, so check the message ourselves
        if "Failed to resolve" in result.stderr or "Failed to resolve" in result.stdout:
            print("Could not resolve target:", target)
            exit(1)

        return result.stdout                    # the XML text

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

    open_ports = []                             # results go here

    for port in root.iter("port"):              # go through every <port> tag
        if port.get("protocol") != "tcp":       # TCP only for now
            continue

        state_tag = port.find("state")          # may be None if the tag is missing
        if state_tag is None or state_tag.get("state") != "open":
            continue                            # skip closed/filtered ports

        service = port.find("service")          # <service> can be missing
        open_ports.append({
            "port": f"{port.get('portid')}/{port.get('protocol')}",   # e.g. 22/tcp
            "state": "open",                    # we only get here if it is open
            "service": service.get("name") if service is not None else "unknown",
        })

    return open_ports


def show_results(target, open_ports):
    """Print the open ports as a small table."""
    print(f"\nOpen ports on {target}:")

    if not open_ports:                          # empty list = nothing found
        print("No open ports found.")
        return

    print(f"{'PORT':<12}{'STATE':<10}SERVICE")  # <12 = left-align in 12 spaces
    print("-" * 32)
    for p in open_ports:                        # one row per open port
        print(f"{p['port']:<12}{p['state']:<10}{p['service']}")

    print(f"\nTotal open ports: {len(open_ports)}")


def main():
    # ---- define the command-line arguments ----
    parser = argparse.ArgumentParser(description="Nmap wrapper - shows open ports only")
    parser.add_argument("--target", required=True, help="IP or hostname to scan")
    parser.add_argument("--ports", default="", help="Port range, e.g. 1-1000 (default: nmap default)")
    args = parser.parse_args()                  # read what the user typed

    target = args.target.strip()                # remove extra spaces
    ports = args.ports.strip()

    # ---- validate input ----
    if not target:
        parser.error("target cannot be empty")  # prints message and exits
    if target.startswith("-"):                  # stop nmap options sneaking in as target
        parser.error("target cannot start with '-'")

    # ---- scan -> parse -> show ----
    output = run_scan(target, ports)            # 1. run nmap, get XML
    open_ports = parse_open_ports(output)       # 2. pick out open ports
    show_results(target, open_ports)            # 3. print the table


if __name__ == "__main__":                      # run only when started directly
    try:
        main()
    except KeyboardInterrupt:                   # Ctrl+C
        print("\nScan cancelled.")
