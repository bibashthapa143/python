# 🔍 Port Lookup

> A Python CLI tool that looks up port-to-service mappings and performs live TCP port scans — offline reference lookup and real network scanning in one tool.

Status: 🚧 In Progress

---

## 📖 Overview

Port Lookup started as a simple dictionary lookup (port number → service name) and has grown into a small toolkit with three modes: offline range lookup, offline file-based lookup, and a real live network port scanner using Python's `socket` module.

---

## 🗂️ Files

| File | Purpose |
|---|---|
| `main.py` | Entry point — lets you choose a mode and runs the corresponding logic |
| `services.py` | Holds the `port_services` dictionary (port → service name), kept separate from logic |
| `ports_input.txt` | Sample input file for file-lookup mode (one port per line) |
| `ports_output.txt` | Generated output from file-lookup mode |

---

## 🚀 Usage

Run the script and choose a mode when prompted:

```bash
python main.py
```

```
Choose mode - (r)ange lookup, (f)ile lookup, (s)can live:
```

### Mode `r` — Range Lookup

Checks a range of port numbers against the known `port_services` dictionary. Purely offline — doesn't touch the network.

```
Enter start port: 20
Enter end port: 100

Port 21 -> FTP
Port 22 -> SSH
Port 25 -> SMTP
Port 53 -> DNS
Port 80 -> HTTP
```

### Mode `f` — File Lookup

Reads ports from `ports_input.txt` (one per line), looks each one up, and writes the results to `ports_output.txt`. Invalid lines are logged instead of crashing the program.

**`ports_input.txt`**
```
22
80
443
9999
abc
```

**`ports_output.txt`** (generated)
```
22: SSH
80: HTTP
443: HTTPS
9999: notfound
Skipping invalid entry: abc
```

### Mode `s` — Live Scan

Actually connects to a real target over the network to check which ports are genuinely open. Uses a TCP connection attempt (`socket.connect_ex`) with a 1-second timeout per port.

```
Enter target IP to scan: 192.168.1.1
Enter port range (e.g. 1-100): 1-100

scanning from 1 to 100
Port 80 (HTTP): OPEN
Port 443 (HTTPS): OPEN
```

Handles invalid/unreachable addresses gracefully and stops the scan early instead of crashing.

---

## 🧠 How It Works

- **`port_services`** (in `services.py`) is a dictionary mapping known port numbers to service names — the shared reference data used by all three modes.
- **`lookup_services()`** does a simple dictionary `.get()` lookup with a fallback for unknown ports.
- **`scan_port()`** opens a real TCP socket connection to a given `(target, port)` pair. A `connect_ex()` result of `0` means the connection succeeded — the port is open and something is actively listening.
- Each mode is its own function (`lookup_range`, `lookup_from_file`, `live_scan`), called based on the user's menu choice in `if __name__ == "__main__":`.

---

## ⚙️ Requirements

- Python 3.x
- No external packages — uses only the standard library (`socket`)

---

## 🗺️ Possible Next Steps

- [ ] Multi-threaded scanning for faster live scans
- [ ] Export live scan results to a file (like file-lookup mode does)
- [ ] Command-line arguments instead of interactive prompts
- [ ] Banner grabbing to identify service versions on open ports
