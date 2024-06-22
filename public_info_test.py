import requests
import json

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()
        ip_data = response.json()
        return ip_data['ip']
    except requests.RequestException as e:
        return f"An error occurred while fetching the public IP: {e}"

def get_location(ip_address, access_key):
    url = f'http://api.ipapi.com/{ip_address}?access_key={access_key}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        # Parse the JSON response to a Python dictionary
        data = response.json()
        
        # Display the JSON response
        print(json.dumps(data, indent=4))
        
        # Save the JSON response to a file with proper formatting
        with open(f'{ip_address}_location.json', 'w') as file:
            json.dump(data, file, indent=4)
            
        print(f"Response saved to {ip_address}_location.json")
        
    except requests.RequestException as e:
        print(f"Error: {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")

if __name__ == "__main__":
    public_ip = get_public_ip()
    if public_ip.startswith("An error occurred"):
        print(public_ip)
    else:
        print(f"Your public IP address is: {public_ip}")
        access_key = 'af63d5fe78c6c43f6ebc4b7f82a62ca5'
        get_location(public_ip, access_key)
