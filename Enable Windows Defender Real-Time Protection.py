import subprocess

def enable_defender_realtime_protection():
    command = "powershell -Command \"Set-MpPreference -DisableRealtimeMonitoring $false\""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Windows Defender real-time protection enabled successfully.")
    else:
        print(f"Failed to enable Windows Defender real-time protection: {result.stderr}")

enable_defender_realtime_protection()