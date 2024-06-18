import subprocess

def isolate_endpoint(ip_address):
    command = f'netsh advfirewall firewall add rule name="Isolate Endpoint" dir=in action=block remoteip={ip_address}'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Endpoint with IP '{ip_address}' isolated successfully.")
    else:
        print(f"Failed to isolate endpoint: {result.stderr}")

# Example usage
isolate_endpoint("192.168.1.100")