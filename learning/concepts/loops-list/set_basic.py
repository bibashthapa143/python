received = {
    "content-type", "server", "date"
}

wanted = {
    "content-type", "server", "cache-control"
}

missing = wanted - received    # Wanted but not received
extra = received - wanted      # Received but not wanted
common = wanted & received     # Present in both
union = wanted | received      # Everything from both

print(f"Missing headers: {missing}")
print(f"Extra headers: {extra}")
print(f"Common headers: {common}")
print(f"Union headers: {union}")
