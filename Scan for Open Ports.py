import subprocess

def scan_open_ports():
    command = 'netstat -ano'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Open Ports:")
        print(result.stdout)
    else:
        print(f"Failed to scan open ports: {result.stderr}")

scan_open_ports()