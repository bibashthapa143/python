import requests

# The website we want to contact
url = "https://example.com"

# Send a GET request to the website
# timeout=10 means don't wait forever for a response
response = requests.get(url, timeout=10)

# Show the HTTP status code
# 200 usually means the request was successful
print("Status code:", response.status_code)

# Show all response headers
# Headers contain information/metadata about the response
print("Headers:", response.headers)

# Get one specific header
# .get() returns None if the header doesn't exist
print("Content-Type:", response.headers.get("Content-Type"))

# Show the content returned by the website
# For a normal webpage, this is usually HTML
print("Page content:", response.text)

# If the server returned JSON, we can convert it
# into Python data using response.json()
#
# Don't use this on a normal HTML page.
# data = response.json()
# print(data)

# Check whether the request returned an HTTP error
# For example, 404 or 500 will raise an exception
response.raise_for_status()

