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

start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

for port in range(start_port, end_port + 1):
    service = lookup_services(port, port_services)
    if service != "notfound":
        print(f"Port {port} -> {service}")
