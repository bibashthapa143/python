import argparse
import subprocess
import sys
import xml.etree.ElementTree as ET

TIMEOUT = 60  # max seconds for one scan


def fail(message):
    """Print an error message and stop the program."""
    print(message)
    sys.exit(1)


def run_scan(target, ports):
    """Run nmap and return its output as XML text."""
    command = ["nmap", "-oX", "-"]              # -oX - = XML output to stdout
    if ports:
        command += ["-p", ports]
    command.append(target)

    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=TIMEOUT)

        if result.returncode != 0:
            fail(f"Error: {result.stderr.strip()}")

        # nmap exits with 0 for a bad hostname, so check the message ourselves
        if "Failed to resolve" in result.stderr + result.stdout:
            fail(f"Could not resolve target: {target}")

        return result.stdout

    except FileNotFoundError:
        fail("Nmap not installed!")
    except subprocess.TimeoutExpired:
        fail("Scan took too long and was stopped.")


def parse_open_ports(xml_output):
    """Read nmap's XML and return a list of open TCP ports (as dictionaries)."""
    try:
        root = ET.fromstring(xml_output)
    except ET.ParseError:
        fail("Could not read nmap output.")

    open_ports = []

    for port in root.iter("port"):
        if port.get("protocol") != "tcp":       # TCP only for now
            continue

        state_tag = port.find("state")          # tags can be missing, so check None
        if state_tag is None or state_tag.get("state") != "open":
            continue

        service = port.find("service")
        open_ports.append({
            "port": f"{port.get('portid')}/{port.get('protocol')}",   # e.g. 22/tcp
            "state": "open",
            "service": service.get("name") if service is not None else "unknown",
        })

    return open_ports


def format_results(target, open_ports):
    """Return the results as printable text (used for screen and file)."""
    lines = [f"Open ports on {target}:"]

    if not open_ports:
        lines.append("No open ports found.")
        return "\n".join(lines)

    lines.append(f"{'PORT':<12}{'STATE':<10}SERVICE")
    lines.append("-" * 32)
    for p in open_ports:
        lines.append(f"{p['port']:<12}{p['state']:<10}{p['service']}")
    lines.append(f"\nTotal open ports: {len(open_ports)}")

    return "\n".join(lines)


def save_report(report, filename):
    """Write the report text to a file."""
    try:
        with open(filename, "w") as f:          # "w" overwrites an old file
            f.write(report + "\n")
        print(f"Results saved to {filename}")
    except OSError:                             # no permission, bad path, disk full
        print("Could not save the file!")


def main():
    parser = argparse.ArgumentParser(description="Nmap wrapper - shows open ports only")
    parser.add_argument("--target", required=True, help="IP or hostname to scan")
    parser.add_argument("--ports", default="", help="Port range, e.g. 1-1000 (default: nmap default)")
    parser.add_argument("--save", metavar="FILE", help="Save results to a text file")
    args = parser.parse_args()

    target = args.target.strip()
    ports = args.ports.strip()

    if not target:
        parser.error("target cannot be empty")
    if target.startswith("-"):                  # stop nmap options sneaking in as target
        parser.error("target cannot start with '-'")

    output = run_scan(target, ports)            # 1. run nmap
    open_ports = parse_open_ports(output)       # 2. pick out open ports
    report = format_results(target, open_ports) # 3. build the text

    print("\n" + report)
    if args.save:
        save_report(report, args.save)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nScan cancelled.")
