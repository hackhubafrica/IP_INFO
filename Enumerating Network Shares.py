import subprocess

def enumerate_network_shares():
    command = "net view"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Network Shares:")
        print(result.stdout)
    else:
        print(f"Failed to enumerate network shares: {result.stderr}")

enumerate_network_shares()