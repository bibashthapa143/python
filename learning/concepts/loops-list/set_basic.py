received = {
    "content-type", "server", "date"
}
wanted = {
    "content-type", "server", "cache-control"
}
missing = wanted - received
extra = received - wanted
common = wanted & received
union = wanted | received
print(f"Missing value: {missing}")
print(f"Extra value: {extra}")
print(f"Common value: {common}")
print(f"Union value: {union}")
