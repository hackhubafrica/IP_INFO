import subprocess

def analyze_security_logs():
    command = 'powershell -Command "Get-WinEvent -FilterHashTable @{LogName=\'Security\'; ID=4624} | Format-Table -Property TimeCreated,Message -AutoSize"'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Analyzing Windows Security logs for authentication events:")
        print(result.stdout)
    else:
        print(f"Failed to analyze Security logs: {result.stderr}")

analyze_security_logs()