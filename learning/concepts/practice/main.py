# import requests

# url = "https://api.github.com"

# response = requests.get(url, timeout = 10)

# print(f"{response.status_code}")
# # print(f"{response.headers}")

# received = set(response.headers.keys())
# print(f"Headers key: {received}")

# if "Content-Type" in received:
#     print("Exist")

# content_type = response.headers.get("Content-Type")
# print(content_type)

# if "application/json" in content_type:
#     data = response.json()
#     print(data["current_user_url"])
# else:
#     print("NO-JSON")
