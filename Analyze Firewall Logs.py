import subprocess

def analyze_firewall_logs():
    command = 'powershell -Command "Get-WinEvent -FilterHashTable @{LogName=\'Security\'; ID=5152} | Format-Table -Property TimeCreated,Message -AutoSize"'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Analyzing Windows Firewall logs for blocked connections:")
        print(result.stdout)
    else:
        print(f"Failed to analyze Firewall logs: {result.stderr}")

analyze_firewall_logs()