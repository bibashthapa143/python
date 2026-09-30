# nmap_wrapper

A simple Python script that runs Nmap using `subprocess` and shows only the open ports.

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
python3 nmap_basic.py
```

Enter a target when asked, for example `scanme.nmap.org`.

## Example Output

```
Open ports on scanme.nmap.org:
22/tcp   open  ssh
80/tcp   open  http
```

## How It Works

1. Asks the user for a target.
2. Runs `nmap <target>` with `subprocess.run()`.
3. Reads the output line by line.
4. Prints only the lines that contain `/tcp` and `open`.

## Project Structure

```
nmap_wrapper/
├── nmap_basic.py
└── README.md
```

## Future Improvements

- [ ] Add UDP port support
- [ ] Let the user choose the port range
- [ ] Split each line into port, state, and service
- [ ] Save results to a file
