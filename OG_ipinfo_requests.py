#!/usr/bin/env python3
# created by @HackHubAfrica
import requests
import json

def get_response(ip_address):
  """Fetches IP information from the ipinfo.io widget demo API.

  Args:
      ip_address (str): The IP address to retrieve information for.

  Returns:
      dict: A dictionary containing the parsed JSON response (if successful), 
           or None if an error occurs.
  """
  url = f"https://ipinfo.io/widget/demo/{ip_address}"
  try:
      response = requests.get(url)
      response.raise_for_status()  # Raise an exception for non-200 status codes
      return response.json()
  except requests.exceptions.RequestException as e:
      print(f"Error: Unable to reach the API for {ip_address}: {e}")
      return None

def save_responses(responses):
  """Saves a list of IP information dictionaries to a JSON file.

  Args:
      responses (list): A list of dictionaries containing IP information.
  """
  with open("ipinfo_responses.json", "w") as file:
      json.dump(responses, file, indent=4)  # Ensures proper JSON formatting

def main():
  """Prompts the user for IP addresses, retrieves information, and saves results."""
  all_responses = []  # Changed to an empty list to collect responses
  while True:
      ip_address = input("Enter an IP address (or 'q' to quit): ")
      if ip_address.lower() == 'q':
          break
      response = get_response(ip_address)
      if response:
          all_responses.append(response)  # Append successful responses

  if all_responses:
      save_responses(all_responses)
      print("Responses saved to ipinfo_responses.json")
  else:
      print("No valid responses retrieved.")

if __name__ == "__main__":
  main()
