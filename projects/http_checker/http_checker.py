import sys
import requests

if len(sys.argv) != 2:
    print("Usage: python3 http_checker.py <url>")
    sys.exit(1)

url = sys.argv[1]

response = requests.get(url, timeout=10)
print(f"Status code: {response.status_code}")

