import subprocess
import json

def get_location(ip_address):
    command = ['curl', f'https://ipapi.co/{ip_address}/json/']
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
    get_location(ip_address)
