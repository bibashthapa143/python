import subprocess

# 1. Ask for target and port range
target = input("Enter target (e.g. scanme.nmap.org): ")
ports = input("Enter port range (e.g. 1-1000) or press Enter for default: ")

# 2. Build the nmap command as a list
command = ["nmap"]

if ports:                      # only add -p if the user typed something
    command += ["-p", ports]

command.append(target)

# 3. Run nmap and capture the output
result = subprocess.run(command, capture_output=True, text=True)

# 4. Stop if nmap reported an error (bad range, bad target, etc.)
if result.returncode != 0:
    print("Error:", result.stderr.strip())
    exit()

# 5. Keep only open ports
print(f"\nOpen ports on {target}:")
found = False

for line in result.stdout.splitlines():
    if "/tcp" in line and " open " in line:
        print(line)
        found = True

if not found:
    print("No open ports found.")
