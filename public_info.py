import requests

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()
        ip_data = response.json()
        return ip_data['ip']
    except requests.RequestException as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    public_ip = get_public_ip()
    print(f"Your public IP address is: {public_ip}")
