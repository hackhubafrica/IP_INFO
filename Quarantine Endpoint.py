import subprocess

def quarantine_endpoint(ip_address):
    command = f'netsh advfirewall firewall add rule name="Quarantine Endpoint" dir=in action=block remoteip={ip_address}'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Endpoint with IP '{ip_address}' quarantined successfully.")
    else:
        print(f"Failed to quarantine endpoint: {result.stderr}")

# Example usage
quarantine_endpoint("192.168.1.100")