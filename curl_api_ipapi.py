import subprocess
import json

def get_location(ip_address, access_key):
    command = ['curl', f'http://api.ipapi.com/{ip_address}?access_key={access_key}']
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        response = result.stdout
        
        # Parse the JSON response to a Python dictionary
        data = json.loads(response)
        
        # Display the JSON response
        print(json.dumps(data, indent=4))
        
        # Save the JSON response to a file with proper formatting
        with open(f'{ip_address}_location.json', 'w') as file:
            json.dump(data, file, indent=4)
            
        print(f"Response saved to {ip_address}_location.json")
        
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")

if __name__ == "__main__":
    ip_address = input("Enter IP address: ")
    access_key = input("Enter your API key: ")
    get_location(ip_address, access_key)
