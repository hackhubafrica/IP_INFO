import subprocess

def disable_powershell_execution():
    command = 'powershell -Command "Set-ExecutionPolicy -ExecutionPolicy Restricted -Scope LocalMachine"'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("PowerShell script execution disabled successfully.")
    else:
        print(f"Failed to disable PowerShell script execution: {result.stderr}")

disable_powershell_execution()