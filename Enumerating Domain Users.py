import subprocess

def enumerate_domain_users(domain_controller):
    command = f"net user /domain /domain:{domain_controller}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Domain Users:")
        print(result.stdout)
    else:
        print(f"Failed to enumerate domain users: {result.stderr}")

# Example usage
enumerate_domain_users("domain-controller.example.com")