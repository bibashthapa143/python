import json

result = {
    "status_code": 200,
    "missing_headers": ["cache-control"]
}

with open("result.json", "w") as file:
    json.dump(result, file, indent=2)
