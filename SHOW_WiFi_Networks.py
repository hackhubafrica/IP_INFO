import subprocess
import re

def get_saved_wifi_profiles():
    profiles_data = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True, text=True).stdout
    profiles = re.findall(r"All User Profile\s*:\s*(.*)", profiles_data)
    return profiles

def get_wifi_password(profile):
    profile_data = subprocess.run(["netsh", "wlan", "show", "profile", profile, "key=clear"], capture_output=True, text=True).stdout
    password_match = re.search(r"Key Content\s*:\s*(.*)", profile_data)
    if password_match:
        return password_match.group(1)
    return None

def save_passwords_to_file(passwords, filename="passwords.txt"):
    with open(filename, "w") as file:
        for profile, password in passwords.items():
            file.write(f"Profile: {profile}\nPassword: {password}\n\n")

def main():
    profiles = get_saved_wifi_profiles()
    passwords = {}

    for profile in profiles:
        password = get_wifi_password(profile)
        if password:
            passwords[profile] = password
        else:
            passwords[profile] = "No password found"

    save_passwords_to_file(passwords)
    print(f"Saved passwords to passwords.txt")

if __name__ == "__main__":
    main()
