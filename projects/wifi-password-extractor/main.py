import subprocess

def get_saved_wifi_passwords():
    result = subprocess.check_output(
        ["netsh", "wlan", "show", "profiles"],
        text=True,
        encoding="utf-8",
        errors="ignore"
    )

    profiles = [
        line.split(":", 1)[1].strip()
        for line in result.splitlines()
        if "All User Profile" in line
    ]

    for name in profiles:
        try:
            details = subprocess.check_output(
                ["netsh", "wlan", "show", "profile", name, "key=clear"],
                text=True,
                encoding="utf-8",
                errors="ignore"
            )
        except subprocess.CalledProcessError:
            print(f"Wi-Fi: {name}")
            print("Password: Could not read profile (run as admin?)")
            print("-" * 30)
            continue

        password = "No password found"
        for dline in details.splitlines():
            if "Key Content" in dline:
                password = dline.split(":", 1)[1].strip()
                break

        print(f"Wi-Fi: {name}")
        print(f"Password: {password}")
        print("-" * 30)


if __name__ == "__main__":
    get_saved_wifi_passwords()
