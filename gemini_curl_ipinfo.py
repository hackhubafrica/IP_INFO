import subprocess
import os

def get_location(ip_address):
  """Fetches location data for the given IP address using a stored API key.

  Args:
      ip_address (str): The IP address for which to retrieve location information.

  Returns:
      str: The JSON response containing location data (if successful), or None if an error occurs.
  """

  # Read API key from a secure environment variable
  api_key = os.getenv("IPINFO_API_KEY", None)

  if not api_key:
      print("Error: API key not found. Please set the 'IPINFO_API_KEY' environment variable.")
      return None

  command = ['curl', f'https://ipinfo.io/{ip_address}/json?token={api_key}']
  try:
      result = subprocess.run(command, capture_output=True, text=True, check=True)
      response = result.stdout
      return response
  except subprocess.CalledProcessError as e:
      print(f"Error: {e}")
      return None

if __name__ == "__main__":
  ip_address = input("Enter IP address: ")
  location_data = get_location(ip_address)

  if location_data:
      # Display the JSON response
      print(location_data)

      # Optionally save the JSON response to a file (replace with your desired logic)
      # with open(f'{ip_address}_location.json', 'w') as file:
      #     file.write(location_data)
      #     print(f"Response saved to {ip_address}_location.json")
  else:
      print("Failed to retrieve location data.")
