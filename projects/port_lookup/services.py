port_services = {                                                # Known port -> service name mapping
    20: "FTP-DATA",            # FTP data transfer
    21: "FTP",                 # File Transfer Protocol
    22: "SSH",                 # Secure Shell remote access
    23: "Telnet",              # Unencrypted remote terminal access
    25: "SMTP",                # Simple Mail Transfer Protocol
    53: "DNS",                 # Domain Name System
    67: "DHCP",                # DHCP server
    68: "DHCP-Client",         # DHCP client
    69: "TFTP",                # Trivial File Transfer Protocol
    80: "HTTP",                # Unencrypted web traffic
    88: "Kerberos",            # Kerberos authentication
    110: "POP3",               # Email retrieval
    111: "RPCbind",             # Maps RPC services to ports
    119: "NNTP",               # Network News Transfer Protocol
    123: "NTP",                # Network Time Protocol
    135: "MS-RPC",             # Microsoft RPC
    137: "NetBIOS-NS",         # NetBIOS Name Service
    138: "NetBIOS-DGM",        # NetBIOS Datagram Service
    139: "NetBIOS-SSN",        # NetBIOS Session Service
    143: "IMAP",               # Internet Message Access Protocol
    161: "SNMP",               # Simple Network Management Protocol
    162: "SNMP-Trap",          # SNMP trap/notification messages
    179: "BGP",                # Border Gateway Protocol
    194: "IRC",                # Internet Relay Chat
    389: "LDAP",               # Lightweight Directory Access Protocol
    443: "HTTPS",              # Encrypted web traffic over TLS
    445: "SMB",                # Server Message Block
    465: "SMTPS",              # SMTP over implicit TLS
    514: "Syslog",             # Network/system logging
    515: "LPD",                # Line Printer Daemon
    587: "SMTP-Submission",    # Email message submission
    636: "LDAPS",              # LDAP over TLS
    993: "IMAPS",              # IMAP over TLS
    995: "POP3S",              # POP3 over TLS
    1080: "SOCKS",             # SOCKS proxy
    1433: "MSSQL",              # Microsoft SQL Server
    1521: "Oracle-DB",          # Oracle Database
    1723: "PPTP",               # Point-to-Point Tunneling Protocol
    2049: "NFS",                # Network File System
    3306: "MySQL",              # MySQL database
    3389: "RDP",                # Remote Desktop Protocol
    5060: "SIP",                # Session Initiation Protocol
    5432: "PostgreSQL",         # PostgreSQL database
    5500: "HTTP-ALT",           # Alternate HTTP/service port
    5900: "VNC",                # Virtual Network Computing
    6379: "Redis",              # Redis database/cache
    6667: "IRC",                # Internet Relay Chat
    8080: "HTTP-Proxy",         # Common alternate HTTP/proxy port
    8443: "HTTPS-Alt",          # Common alternate HTTPS port
    9200: "Elasticsearch",      # Elasticsearch HTTP API
    27017: "MongoDB",           # MongoDB database
}
