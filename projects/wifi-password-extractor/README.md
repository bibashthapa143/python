<div align="center">

# 🔐 Wi-Fi Password Extractor

**Recover every Wi-Fi password saved on your Windows machine — instantly, with zero external dependencies.**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

</div>

---

### 📖 Overview

A lightweight Python script that pulls every saved Wi-Fi network on a Windows machine and reveals its stored password — using nothing but the built-in `netsh` command. No installs, no third-party libraries, just pure Python.

---

## ✨ Features

| | |
|---|---|
| 📡 **Full network scan** | Lists every Wi-Fi profile ever saved on the machine |
| 🔑 **Password reveal** | Extracts the stored password for each network |
| 🛡️ **Admin-aware** | Detects missing Administrator rights and warns before running |
| ⚡ **Zero dependencies** | Pure Python standard library — nothing to `pip install` |
| 🪶 **Single-file** | One script, runs instantly, no setup required |

---

## 🛠 How It Works

```
┌─────────────────────────┐
│ 1. Check admin rights    │
└────────────┬─────────────┘
             ▼
┌─────────────────────────┐
│ 2. List saved profiles   │  netsh wlan show profiles
└────────────┬─────────────┘
             ▼
┌─────────────────────────┐
│ 3. Reveal each password  │  netsh wlan show profile <name> key=clear
└────────────┬─────────────┘
             ▼
┌─────────────────────────┐
│ 4. Print name + password │
└─────────────────────────┘
```

---

## 📋 Requirements

| Requirement | Details |
|---|---|
| 🖥️ OS | Windows (uses `netsh`, a Windows-only tool) |
| 🐍 Python | 3.x |
| 📦 Dependencies | None — built-in `subprocess` and `ctypes` only |
| 🔑 Permissions | Administrator (required for `key=clear`) |

---

## 🚀 Usage

Run your terminal **as Administrator**, then:

```
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

**If not run as Administrator:**

```
Warning: Not running as Administrator.
Passwords will show as 'Could not read profile' without admin rights.
```

---

## ⚠️ Disclaimer

> This tool only reveals passwords for Wi-Fi networks **already saved on the machine it's run on** — it cannot retrieve passwords for networks you haven't connected to, and it does not attack, crack, or bypass any network security.

**✅ Intended for:**
- Personal use — recovering your own forgotten Wi-Fi passwords
- Educational purposes — understanding how Windows stores credentials locally

**❌ Not intended for:**
- Running on a machine you don't own or don't have explicit permission to access

---

## 📝 Notes

- Must be run with Administrator privileges, or passwords will not be readable
- Networks using non-key authentication may show `"No password found"`
- Profile detection currently matches English-language Windows output only (`"All User Profile"`) — a non-English Windows install may not detect profiles

---

<div align="center">

## 👤 Author

Built by **Bibash** as part of a cybersecurity + Python learning journey.

</div>
