# HTTP Header Checker

> A command-line tool that checks which security headers a website sends and saves the result as JSON

Status: ✅ Completed

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![requests](https://img.shields.io/badge/library-requests-2E8B57)
![Type](https://img.shields.io/badge/type-CLI%20tool-informational)

---

## 📌 Overview

Security headers are instructions a server sends to the browser to help protect users from common attacks. This tool sends a request to a URL, then reports which important security headers are **present** and which are **missing**.

## ✨ Features

- Takes a URL from the command line
- Shows the HTTP status code
- Checks 6 key security headers
- Prints a clean PRESENT / MISSING table with a summary score
- Saves the full result to `result.json`
- Handles bad URLs, timeouts, and connection errors without crashing

## 🔐 Headers Checked

| Header | What it does |
|---|---|
| `Strict-Transport-Security` | Forces browsers to use HTTPS |
| `Content-Security-Policy` | Limits where scripts and resources can load from (helps prevent XSS) |
| `X-Frame-Options` | Stops the page from being embedded in frames (helps prevent clickjacking) |
| `X-Content-Type-Options` | Stops browsers from guessing file types (MIME sniffing) |
| `Referrer-Policy` | Controls how much URL information is shared with other sites |
| `Permissions-Policy` | Controls browser features such as camera, microphone, and location |

## 🛠️ Setup

```bash
cd projects/http_checker
python3 -m venv .venv
```

Activate the virtual environment:

```bash
# Linux / macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

Install the dependency:

```bash
pip install -r requirements.txt
```

## 🚀 Usage

```bash
python3 http_checker.py <url>
```

Example:

```bash
python3 http_checker.py https://github.com
```

## 📟 Example Output

```
Status code: 200

HEADER                         RESULT
----------------------------------------
content-security-policy        PRESENT
permissions-policy             MISSING
referrer-policy                PRESENT
strict-transport-security      PRESENT
x-content-type-options         PRESENT
x-frame-options                PRESENT

5/6 security headers present
```

## 💾 JSON Output

Each run writes `result.json`:

```json
{
  "url": "https://github.com",
  "status_code": 200,
  "present": [
    "content-security-policy",
    "referrer-policy",
    "strict-transport-security",
    "x-content-type-options",
    "x-frame-options"
  ],
  "missing": [
    "permissions-policy"
  ]
}
```

## ⚙️ How It Works

1. Reads the URL from `sys.argv`
2. Sends a GET request with `requests` (10-second timeout)
3. Lowercases the response header names into a set
4. Compares it with the set of wanted headers:
   - `wanted & received` gives the **present** headers
   - `wanted - received` gives the **missing** headers
5. Prints the table and saves the result with `json.dump`

## 📚 Skills Practiced

- Virtual environments and `pip`
- The `requests` library (status codes, headers, error handling)
- Working with JSON files
- Set operations (`&`, `-`)
- Command-line arguments with `sys.argv`

## 🔮 Possible Improvements

- `--insecure` flag for sites with self-signed certificates
- Show where a URL redirects to
- Check a list of URLs from a file

## ⚠️ Disclaimer

This tool is for learning and for testing sites you own or have permission to test.
