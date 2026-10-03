import argparse                                 # read --target / --ports / --save from the terminal
import subprocess                               # run nmap from Python
import sys                                      # sys.exit() to stop the program
import xml.etree.ElementTree as ET              # read nmap's XML output
from typing import NoReturn                     # tells VS Code a function never returns

TIMEOUT = 60                                    # max seconds for one scan


def fail(message) -> NoReturn:
    """Print an error message and stop the program (never returns)."""
    print(message)
    sys.exit(1)                                 # exit code 1 = something went wrong


def run_scan(target, ports):
    """Run nmap and return its output as XML text."""
    command = ["nmap", "-oX", "-"]              # -oX - = XML output to stdout
    if ports:                                   # add -p only if ports were given
        command += ["-p", ports]
    command.append(target)                      # e.g. ['nmap','-oX','-','-p','1-1000','host']

    try:
        # capture_output = save stdout/stderr, text = get strings, timeout = max seconds
        result = subprocess.run(command, capture_output=True, text=True, timeout=TIMEOUT)

        if result.returncode != 0:              # non-zero = nmap itself failed
            fail(f"Error: {result.stderr.strip()}")

        # nmap exits with 0 for a bad hostname, so check the message ourselves
        if "Failed to resolve" in result.stderr + result.stdout:
            fail(f"Could not resolve target: {target}")

        return result.stdout                    # the XML text

    except FileNotFoundError:                   # nmap is not installed
        fail("Nmap not installed!")
    except subprocess.TimeoutExpired:           # scan ran longer than TIMEOUT
        fail("Scan took too long and was stopped.")


def parse_open_ports(xml_output):
    """Read nmap's XML and return a list of open TCP ports (as dictionaries)."""
    try:
        root = ET.fromstring(xml_output)        # turn XML text into a tree
    except ET.ParseError:                       # output was not valid XML
        fail("Could not read nmap output.")

    open_ports = []                             # results go here

    for port in root.iter("port"):              # go through every <port> tag
        if port.get("protocol") != "tcp":       # TCP only for now
            continue

        state_tag = port.find("state")          # tags can be missing, so check for None
        if state_tag is None or state_tag.get("state") != "open":
            continue                            # skip closed/filtered ports

        service = port.find("service")          # <service> can be missing too
        open_ports.append({
            "port": f"{port.get('portid')}/{port.get('protocol')}",   # e.g. 22/tcp
            "state": "open",                    # we only get here if it is open
            "service": service.get("name") if service is not None else "unknown",
        })

    return open_ports


def format_results(target, open_ports):
    """Return the results as printable text (used for screen and file)."""
    lines = [f"Open ports on {target}:"]       # build the report line by line

    if not open_ports:                          # empty list = nothing found
        lines.append("No open ports found.")
        return "\n".join(lines)

    lines.append(f"{'PORT':<12}{'STATE':<10}SERVICE")   # <12 = left-align in 12 spaces
    lines.append("-" * 32)
    for p in open_ports:                        # one row per open port
        lines.append(f"{p['port']:<12}{p['state']:<10}{p['service']}")
    lines.append(f"\nTotal open ports: {len(open_ports)}")

    return "\n".join(lines)                     # join all lines into one text


def save_report(report, filename):
    """Write the report text to a file."""
    try:
        with open(filename, "w") as f:          # "w" overwrites an old file
            f.write(report + "\n")
        print(f"Results saved to {filename}")
    except OSError:                             # no permission, bad path, disk full
        print("Could not save the file!")


def main():
    # ---- define the command-line arguments ----
    parser = argparse.ArgumentParser(description="Nmap wrapper - shows open ports only")
    parser.add_argument("--target", required=True, help="IP or hostname to scan")
    parser.add_argument("--ports", default="", help="Port range, e.g. 1-1000 (default: nmap default)")
    parser.add_argument("--save", metavar="FILE", help="Save results to a text file")
    args = parser.parse_args()                  # read what the user typed

    target = args.target.strip()                # remove extra spaces
    ports = args.ports.strip()

    # ---- validate input ----
    if not target:
        parser.error("target cannot be empty")  # prints message and exits
    if target.startswith("-"):                  # stop nmap options sneaking in as target
        parser.error("target cannot start with '-'")

    # ---- scan -> parse -> show -> (save) ----
    output = run_scan(target, ports)            # 1. run nmap, get XML
    open_ports = parse_open_ports(output)       # 2. pick out open ports
    report = format_results(target, open_ports) # 3. build the text

    print("\n" + report)                        # show on screen
    if args.save:                               # only if --save was given
        save_report(report, args.save)


if __name__ == "__main__":                      # run only when started directly
    try:
        main()
    except KeyboardInterrupt:                   # Ctrl+C
        print("\nScan cancelled.")
