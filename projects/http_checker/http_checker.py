# HTTP Header Checker
# Usage: python3 http_checker.py <url>
# Checks which security headers a website sends and saves the result to result.json

import json  # for saving the result to a file
import sys  # for reading the URL from the command line
import requests  # for sending the HTTP request

# --- Step 1: Get the URL from the command line ---
# sys.argv = [script name, url], so we need exactly 2 items
if len(sys.argv) != 2:
    print("Usage: python3 http_checker.py <url>")
    sys.exit(1)  # 1 means the script ended with an error

url = sys.argv[1]

# --- Step 2: Send the request and show the status code ---
try:
    # timeout=10 means don't wait forever for a response
    response = requests.get(url, timeout=10)
except requests.exceptions.RequestException as error:
    # Catches bad URLs, timeouts, and connection errors
    print(f"Request failed: {error}")
    sys.exit(1)
print(f"Status code: {response.status_code}")

# --- Step 3: Compare headers using sets ---
# The security headers we want to see (lowercase, so comparing is easy)
SECURITY_HEADERS = {
    "strict-transport-security",
    "content-security-policy",
    "x-frame-options",
    "x-content-type-options",
    "referrer-policy",
    "permissions-policy",
}

# The headers the server actually sent, lowercased
received = {name.lower() for name in response.headers}

present = SECURITY_HEADERS & received  # in both sets
missing = SECURITY_HEADERS - received  # wanted, but not sent

# --- Step 4: Print the present/missing table ---
print()
print(f"{'HEADER':<30} RESULT")
print("-" * 40)

for header in sorted(SECURITY_HEADERS):
    if header in present:
        result = "PRESENT"
    else:
        result = "MISSING"
    # :<30 pads the name to 30 characters so the columns line up
    print(f"{header:<30} {result}")

print()
print(f"{len(present)}/{len(SECURITY_HEADERS)} security headers present")


# --- Step 5: Save the result to result.json ---
# JSON can't store sets, so we convert them to sorted lists
result = {
    "url":url,
    "status_code": response.status_code,
    "present": sorted(present),
    "missing": sorted(missing),
}
# "w" opens the file for writing (overwrites the old file each run)
with open("result.json", "w") as f:
    json.dump(result, f, indent=2)

print("Saved to result.json")
