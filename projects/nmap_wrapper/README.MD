<h1 align="center">🔍 nmap_wrapper</h1>

<p align="center">
  A simple Python CLI that runs <b>Nmap</b> for you and shows <b>only the open ports</b>.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python 3">
  <img src="https://img.shields.io/badge/Requires-Nmap-informational" alt="Requires Nmap">
  <img src="https://img.shields.io/badge/Interface-CLI-success" alt="CLI">
  <img src="https://img.shields.io/badge/Status-Learning%20Project-orange" alt="Learning project">
</p>

> ⚠️ **Only scan machines you own or have permission to test.**
> `scanme.nmap.org` is safe for practice.

---

## ✨ Features

- 🖥️ Simple command-line interface (`--target`, `--ports`, `--save`)
- 🎯 Shows open ports only, with state and service name
- 💾 Save results to a text file
- 🛡️ Clear error messages (Nmap missing, timeout, bad target)
- 🐍 Pure Python standard library, no `pip install` needed

---

## 📸 Demo

![nmap_wrapper demo](images\Screenshot 2026-10-06 222459.png)

Example output:

```
Open ports on scanme.nmap.org:
PORT        STATE     SERVICE
--------------------------------
22/tcp      open      ssh
80/tcp      open      http

Total open ports: 2
```

---

## 📦 Requirements

- Python 3
- Nmap installed and available in your PATH

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

---

## 🚀 Usage

```bash
python3 nmap_wrapper.py --target <ip-or-hostname> [--ports <range>] [--save <file>]
```

| Argument   | Required | Description                                                          |
|------------|:--------:|----------------------------------------------------------------------|
| `--target` | ✅       | IP address or hostname to scan                                       |
| `--ports`  | ❌       | Ports to scan, e.g. `1-1000` or `22,80,443` (default: Nmap default) |
| `--save`   | ❌       | Save results to a text file, e.g. `results.txt`                      |

**Examples**

```bash
python3 nmap_wrapper.py --target scanme.nmap.org
python3 nmap_wrapper.py --target scanme.nmap.org --ports 1-1000
python3 nmap_wrapper.py --target 192.168.56.101 --ports 22,80,443
python3 nmap_wrapper.py --target scanme.nmap.org --ports 1-1000 --save results.txt
python3 nmap_wrapper.py --help
```

---

## ⚙️ How It Works

```
--target / --ports  →  nmap (subprocess)  →  parse XML  →  open ports table  →  (save)
```

1. Reads `--target`, `--ports` and `--save` using `argparse`.
2. Runs `nmap` with `subprocess.run()` and XML output (`-oX -`), with a 60 second timeout.
3. Stops with a clear message if Nmap is missing, times out, fails, or the target can't be resolved.
4. Parses the XML with `xml.etree.ElementTree` and keeps only open TCP ports.
5. Prints each port with its state and service as a table.
6. If `--save` is given, writes the same table to a file.

---

## 📁 Project Structure

```
nmap_wrapper/
├── images/
│   └── demo.png
├── nmap_wrapper.py
└── README.md
```

---

## 🗺️ Roadmap

- [x] Let the user choose the port range
- [x] Split each line into port, state, and service
- [x] Add an `argparse` command-line interface
- [x] Parse Nmap XML output
- [x] Save results to a file
- [ ] Add UDP port support
