import socket
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

def dns_lookup(domain):
    """Performs DNS lookup to resolve the domain to an IP address.

    Args:
        domain (str): The domain name to resolve.

    Returns:
        str: The resolved IP address if successful, or None otherwise.
    """
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror as e:
        print(f"Error: {domain} - {e}")
        return None

def main():
    """Prompts the user for domain names, resolves them to IPs, retrieves information, and saves results."""
    all_responses = []
    while True:
        domain = input("Enter a domain name (or 'q' to quit): ")
        if domain.lower() == 'q':
            break

        # Perform DNS lookup
        ip_address = dns_lookup(domain)
        if ip_address:
            print(f"Resolved IP for {domain}: {ip_address}")
            
            # Fetch information from ipinfo.io
            response = get_response(ip_address)
            if response:
                response['domain'] = domain  # Add the domain to the response for reference
                all_responses.append(response)
        else:
            print(f"No IP address found for {domain}")

    if all_responses:
        save_responses(all_responses)
        print("Responses saved to ipinfo_responses.json")
    else:
        print("No valid responses retrieved.")

if __name__ == "__main__":
    main()
