import sys
import requests

if len(sys.argv) != 2:
    print("Usage: python3 http_checker.py <url>")
    sys.exit(1)

url = sys.argv[1]

try:
    response = requests.get(url, timeout=10)
except requests.exceptions.RequestException as error:
    print(f"Request failed: {error}")
    sys.exit(1)
print(f"Status code: {response.status_code}")

SECURITY_HEADERS = {
    "strict-transport-security",
    "content-security-policy",
    "x-frame-options",
    "x-content-type-options",
    "referrer-policy",
    "permission-policy",
}

received = {name.lower() for name in response.headers}

present = SECURITY_HEADERS & received
missing = SECURITY_HEADERS - received

print(f"present: {sorted(present)}")
print(f"Missing: {sorted(missing)}")

