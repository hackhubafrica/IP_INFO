import subprocess

def get_location(ip_address, api_key):
    command = ['curl', f'https://ipinfo.io/{ip_address}/json?token={api_key}']
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        response = result.stdout
        
        # Display the JSON response
        print(response)
        
        # Save the JSON response to a file
        with open(f'{ip_address}_location.json', 'w') as file:
            file.write(response)
            
        print(f"Response saved to {ip_address}_location.json")
        
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ip_address = input("Enter IP address: ")
    api_key = input("Enter your API key: ")
    get_location(ip_address, api_key)
