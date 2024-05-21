import requests

def get_location(ip_address, api_key):
    url = f"http://api.ipapi.com/{ip_address}?access_key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        try:
            data = response.json()
        except ValueError:
            print("Error: Unable to decode JSON response")
            return None

        if 'error' in data:
            print(f"Error: {data['error']['info']}")
            return None
        else:
            return {
                "ip": data.get("ip"),
                "city": data.get("city"),
                "region": data.get("region_name"),
                "country": data.get("country_name"),
                "latitude": data.get("latitude"),
                "longitude": data.get("longitude")
            }
    else:
        print(f"Error: Unable to reach the API. Status code: {response.status_code}")
        return None

if __name__ == "__main__":
    ip_address = input("Enter IP address: ")
    api_key = input("Enter your API key: ")
    location = get_location(ip_address, api_key)
    if location:
        print(f"IP: {location['ip']}")
        print(f"City: {location['city']}")
        print(f"Region: {location['region']}")
        print(f"Country: {location['country']}")
        print(f"Latitude: {location['latitude']}")
        print(f"Longitude: {location['longitude']}")
