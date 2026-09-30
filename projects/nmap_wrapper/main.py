import subprocess

# 1. Ask for a target
target = input("Enter target (e.g. scanme.nmap.org): ")

# 2. Run nmap and capture its output
result = subprocess.run(["nmap", target], capture_output=True, text=True)
output = result.stdout

# 3. Go through the output line by line, keep only open ports
print(f"\nOpen ports on {target}:")
found = False

for line in output.splitlines():
    if "/tcp" in line and "open" in line:
        print(line)
        found = True

if not found:
    print("No open ports found.")
