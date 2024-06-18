import subprocess

def block_malicious_ip(ip_address):
    command = f'netsh advfirewall firewall add rule name="Block Malicious IP" dir=in action=block remoteip={ip_address}'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"IP address '{ip_address}' blocked successfully.")
    else:
        print(f"Failed to block IP address '{ip_address}': {result.stderr}")

# Example usage
block_malicious_ip("192.168.1.100")