import subprocess


def run_scan(target, ports):
    """Run nmap and return its output text."""
    command = ["nmap"]
    if ports:                                   # add -p only if user gave ports
        command += ["-p", ports]
    command.append(target)

    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=60)

        if result.returncode != 0:                      # nmap itself failed
            print("Error:", result.stderr.strip())
            exit()

        if "Failed to resolve" in result.stderr or "Failed to resolve" in result.stdout:
            print("Could not resolve target:", target)  # nmap ran, but target is invalid
        exit()

        return result.stdout                            # everything is fine, give back the output

    except FileNotFoundError:                   # nmap is not installed
        print("Nmap not installed!")
        exit()

    except subprocess.TimeoutExpired:           # scan ran longer than 60s
        print("Scan took too long and was stopped.")
        exit()


def parse_open_ports(output):
    """Turn nmap output into a list of open ports (as dictionaries)."""
    open_ports = []

    for line in output.splitlines():
        if "/tcp" in line and " open " in line:     # keep only open port lines
            parts = line.split()                    # ['22/tcp', 'open', 'ssh']
            open_ports.append({
                "port": parts[0],
                "state": parts[1],
                "service": parts[2] if len(parts) > 2 else "unknown",
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


def save_results(target, open_ports, filename="scan_results.txt"):
    """Write the open ports to a text file."""
    with open(filename, "w") as f:                  # "w" overwrites old file
        f.write(f"Open ports on {target}:\n")
        for p in open_ports:
            f.write(f"{p['port']:<12}{p['state']:<10}{p['service']}\n")
        f.write(f"\nTotal open ports: {len(open_ports)}\n")

    print(f"Results saved to {filename}")


# ---- main program ----
try:
    while True:                                     # ask until target is not empty
        target = input("Enter target (e.g. scanme.nmap.org): ").strip()
        if target:
            break
        print("Target cannot be empty!")

    ports = input("Enter port range (e.g. 1-1000) or press Enter for default: ").strip()

    output = run_scan(target, ports)                # 1. scan
    open_ports = parse_open_ports(output)           # 2. pick out open ports
    show_results(target, open_ports)                # 3. show them

    if open_ports:                                  # 4. offer to save
        choice = input("\nSave results to a file? (y/n): ").lower()
        if choice == "y":
            save_results(target, open_ports)

except KeyboardInterrupt:                           # Ctrl+C
    print("\nScan cancelled.")
