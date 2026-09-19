# 🔐 Wi-Fi Password Extractor

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?logo=windows)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

> A simple Python script that extracts saved Wi-Fi network names and their passwords from a Windows machine using the built-in `netsh` command — no external libraries required.

---

## ✨ Features

- 📡 Lists every Wi-Fi network saved on your machine
- 🔑 Reveals the stored password for each network
- 🛡️ Detects if not running as Administrator and warns upfront
- ⚡ Pure Python standard library — no installs needed
- 🪶 Lightweight — single script, runs instantly

---

## 🛠 How It Works

1. Checks if the script is running with Administrator privileges and warns if not
2. Runs `netsh wlan show profiles` to list all saved Wi-Fi profiles
3. For each profile, runs `netsh wlan show profile <name> key=clear` to reveal its password
4. Parses and prints each network name alongside its password

---

## 📋 Requirements

| Requirement | Details |
|---|---|
| OS | Windows (uses `netsh`, a Windows-only tool) |
| Python | 3.x |
| Dependencies | None — built-in `subprocess` and `ctypes` modules only |
| Permissions | Administrator (required to reveal passwords with `key=clear`) |

---

## 🚀 Usage

Run your terminal **as Administrator**, then:

    python main.py

**Example output:**

    Wi-Fi: HomeNetwork
    Password: mypassword123
    ------------------------------
    Wi-Fi: OfficeWiFi
    Password: No password found
    ------------------------------

If not run as Administrator, you'll see:

    Warning: Not running as Administrator.
    Passwords will show as 'Could not read profile' without admin rights.

---

## ⚠️ Disclaimer

This tool only reveals passwords for Wi-Fi networks **already saved on the machine it's run on** — it cannot retrieve passwords for networks you haven't connected to, and it does not attack, crack, or bypass any network security.

Intended for:
- ✅ Personal use — recovering your own forgotten Wi-Fi passwords
- ✅ Educational purposes — understanding how Windows stores credentials locally

❌ Do not run this on a machine you don't own or don't have explicit permission to access.

---

## 📝 Notes

- Must be run with Administrator privileges, or passwords will not be readable.
- Some profiles may show "No password found" if they use a different authentication method (e.g. open networks).
- Profile detection currently matches English-language Windows output only (`"All User Profile"`); on a non-English Windows install, this string is localized and profiles may not be detected.

---

## 👤 Author

Built by **Bibash** as part of a cybersecurity + Python learning journey.
