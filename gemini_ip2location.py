import requests
import os

def get_location(ip_address):
  """Fetches location data for the given IP address using a stored API key.

  Args:
      ip_address (str): The IP address for which to retrieve location information.

  Returns:
      dict: A dictionary containing location data (if successful), or None if an error occurs.

  Raises:
      requests.exceptions.RequestException: If the request to the API fails.
  """

  # Read API key from a secure environment variable
  api_key = os.getenv("IPAPI_API_KEY", None)

  if not api_key:
      print("Error: API key not found. Please set the 'IPAPI_API_KEY' environment variable.")
      return None

  url = f"http://api.ipapi.com/{ip_address}?access_key={api_key}"
  try:
      response = requests.get(url)
      response.raise_for_status()  # Raise an exception for non-200 status codes
  except requests.exceptions.RequestException as e:
      print(f"Error: Unable to reach the API: {e}")
      return None

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

if __name__ == "__main__":
  ip_address = input("Enter IP address: ")
  location = get_location(ip_address)

  if location:
      print(f"IP: {location['ip']}")
      print(f"City: {location['city']}")
      print(f"Region: {location['region']}")
      print(f"Country: {location['country']}")
      print(f"Latitude: {location['latitude']}")
      print(f"Longitude: {location['longitude']}")

