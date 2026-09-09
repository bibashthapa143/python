port_services = {
    20: "FTP-DATA",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    8080: "HTTP-Proxy"
}

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


if __name__ == "__main__":
    mode = input("Choose mode - (r)ange or (f)ile: ").strip().lower()

    if mode == "r":
        lookup_range()
    elif mode == "f":
        lookup_from_file()
    else:
        print("Invalid choice. Enter 'r' or 'f'.")
