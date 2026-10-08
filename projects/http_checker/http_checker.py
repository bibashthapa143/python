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
    "permissions-policy",
}

received = {name.lower() for name in response.headers}

present = SECURITY_HEADERS & received
missing = SECURITY_HEADERS - received

print()
print(f"{'HEADER':<30} RESULT")
print("-" * 40)

for header in sorted(SECURITY_HEADERS):
    if header in present:
        result = "PRESENT"
    else:
        result = "MISSING"
    print(f"{header:<30} {result}")

print()
print(f"{len(present)}/{len(SECURITY_HEADERS)} security headers present")


