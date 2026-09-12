# 🔐 Wi-Fi Password Extractor

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?logo=windows)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

A simple Python script that extracts saved Wi-Fi network names and their passwords from a Windows machine using the built-in `netsh` command — no external libraries required.

---

## ✨ Features

- 📡 Lists every Wi-Fi network saved on your machine
- 🔑 Reveals the stored password for each network
- ⚡ Pure Python standard library — no installs needed
- 🪶 Lightweight — single script, runs instantly

---

## 🛠 How It Works

1. Runs `netsh wlan show profiles` to list all saved Wi-Fi profiles
2. For each profile, runs `netsh wlan show profile <name> key=clear` to reveal its password
3. Parses and prints each network name alongside its password

---

## 📋 Requirements

| Requirement | Details |
|---|---|
| OS | Windows (uses `netsh`, a Windows-only tool) |
| Python | 3.x |
| Dependencies | None — built-in `subprocess` module only |

---

## 🚀 Usage

```bash
python main.py
```

**Example output:**
```
Wi-Fi: HomeNetwork
Password: mypassword123
------------------------------
Wi-Fi: OfficeWiFi
Password: No password found
------------------------------
```

---

## ⚠️ Disclaimer

This tool only reveals passwords for Wi-Fi networks **already saved on the machine it's run on** — it cannot retrieve passwords for networks you haven't connected to, and it does not attack, crack, or bypass any network security.

Intended for:
- ✅ Personal use — recovering your own forgotten Wi-Fi passwords
- ✅ Educational purposes — understanding how Windows stores credentials locally

❌ Do not run this on a machine you don't own or don't have explicit permission to access.

---

## 📝 Notes

- Run in a terminal with sufficient permissions to query network profiles.
- Some profiles may show "No password found" if they use a different authentication method (e.g. open networks).

---

## 👤 Author

Built by **Bibash** as part of a cybersecurity + Python learning journey.
