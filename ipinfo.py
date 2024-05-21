import requests

def get_location(ip_address, api_key):
    url = f"https://ipinfo.io/{ip_address}/json?token={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "ip": data.get("ip"),
            "city": data.get("city"),
            "region": data.get("region"),
            "country": data.get("country"),
            "latitude": data.get("loc").split(',')[0],
            "longitude": data.get("loc").split(',')[1]
        }
    else:
        print(f"Error: Unable to reach the API. Status code: {response.status_code}")
        return None

if __name__ == "__main__":
    ip_address =input("Enter IP address: ")
    api_key = input("Enter your API key: ")
    location = get_location(ip_address, api_key)
    if location:
        print(f"IP: {location['ip']}")
        print(f"City: {location['city']}")
        print(f"Region: {location['region']}")
        print(f"Country: {location['country']}")
        print(f"Latitude: {location['latitude']}")
        print(f"Longitude: {location['longitude']}")
