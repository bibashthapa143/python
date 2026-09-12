import subprocess

result = subprocess.check_output(
    ["netsh", "wlan", "show", "profiles"],
    text=True,
    encoding="utf-8",
    errors="ignore"
)

for line in result.splitlines():
    if "All User Profile" in line:
        name = line.split(":", 1)[1].strip()

        details = subprocess.check_output(
            ["netsh", "wlan", "show", "profile", name, "key=clear"],
            text=True,
            encoding="utf-8",
            errors="ignore"
        )

        password = "No password found"

        for dline in details.splitlines():
            if "Key Content" in dline:
                password = dline.split(":", 1)[1].strip()
                break

        print(f"Wi-Fi: {name}")
        print(f"Password: {password}")
        print("-" * 30)
