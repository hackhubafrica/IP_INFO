import subprocess

def scan_weak_ssl_tls():
    command = 'sslscan localhost'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Scanning for weak SSL/TLS configurations:")
        print(result.stdout)
    else:
        print(f"Failed to scan SSL/TLS configurations: {result.stderr}")

scan_weak_ssl_tls()