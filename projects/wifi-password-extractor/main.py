import subprocess

def get_saved_wifi_passwords():
    # Get all saved Wi-Fi profile names from Windows
    result = subprocess.check_output(
        ["netsh", "wlan", "show", "profiles"],
        text=True,
        encoding="utf-8",
        errors="ignore"
    )

    # Extract profile names from lines like "All User Profile: MyWifi"
    profiles = [
        line.split(":", 1)[1].strip()
        for line in result.splitlines()
        if "All User Profile" in line
    ]

    for name in profiles:
        try:
            # Fetch full profile details, including the password in clear text
            details = subprocess.check_output(
                ["netsh", "wlan", "show", "profile", name, "key=clear"],
                text=True,
                encoding="utf-8",
                errors="ignore"
            )
        except subprocess.CalledProcessError:
            # Fails without admin rights - skip gracefully instead of crashing
            print(f"Wi-Fi: {name}")
            print("Password: Could not read profile (run as admin?)")
            print("-" * 30)
            continue

        password = "No password found"
        # Look for the "Key Content" line, which holds the actual password
        for dline in details.splitlines():
            if "Key Content" in dline:
                password = dline.split(":", 1)[1].strip()
                break

        print(f"Wi-Fi: {name}")
        print(f"Password: {password}")
        print("-" * 30)


if __name__ == "__main__":
    # Only run when executed directly, not when imported as a module
    get_saved_wifi_passwords()
