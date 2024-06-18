import subprocess

def disable_defender_realtime_protection():
    command = "powershell -Command \"Set-MpPreference -DisableRealtimeMonitoring $true\""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Windows Defender real-time protection disabled successfully.")
    else:
        print(f"Failed to disable Windows Defender real-time protection: {result.stderr}")

disable_defender_realtime_protection()