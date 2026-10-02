# nmap_wrapper

A simple Python command-line tool that runs Nmap using `subprocess` and shows only the open ports.

> ⚠️ Only scan machines you own or have permission to test. `scanme.nmap.org` is safe for practice.

## Requirements

- Python 3
- Nmap installed and available in your PATH

Install Nmap:

```bash
# Kali / Ubuntu / Debian
sudo apt install nmap

# macOS
brew install nmap
```

On Windows, download it from https://nmap.org/download.html (keep "add to PATH" ticked).

Check it works:

```bash
nmap --version
```

## Usage

```bash
python3 nmap_wrapper.py --target <ip-or-hostname> [--ports <range>]
```

| Argument   | Required | Description                                         |
|------------|----------|-----------------------------------------------------|
| `--target` | Yes      | IP address or hostname to scan                      |
| `--ports`  | No       | Ports to scan, e.g. `1-1000` or `22,80,443` (default: Nmap's default) |

Examples:

```bash
python3 nmap_wrapper.py --target scanme.nmap.org
python3 nmap_wrapper.py --target scanme.nmap.org --ports 1-1000
python3 nmap_wrapper.py --target 192.168.56.101 --ports 22,80,443
python3 nmap_wrapper.py --help
```

## Example Output

```
Open ports on scanme.nmap.org:
PORT        STATE     SERVICE
--------------------------------
22/tcp      open      ssh
80/tcp      open      http

Total open ports: 2
```

## How It Works

1. Reads `--target` and `--ports` using `argparse`.
2. Runs `nmap` with `subprocess.run()` (60 second timeout).
3. Stops with a clear message if Nmap is missing, times out, fails, or the target can't be resolved.
4. Reads the output line by line and keeps only lines containing `/tcp` and ` open `.
5. Splits each line into port, state and service, and prints them as a table.

## Project Structure

```
nmap_wrapper/
├── nmap_wrapper.py
└── README.md
```

## Future Improvements

- [x] Let the user choose the port range
- [x] Split each line into port, state, and service
- [x] Add an `argparse` command-line interface
- [ ] Add UDP port support
- [ ] Save results to a file
