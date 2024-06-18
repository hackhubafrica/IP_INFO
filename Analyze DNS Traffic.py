import subprocess

def analyze_dns_traffic(interface):
    command = f'tshark -i {interface} -f "port 53" -Y "dns"'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("DNS Traffic Analysis:")
        print(result.stdout)
    else:
        print(f"Failed to analyze DNS traffic: {result.stderr}")

# Example usage
analyze_dns_traffic("eth0")