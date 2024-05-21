import requests
import json

def get_response(ip_address):
    url = f"https://ipinfo.io/widget/demo/{ip_address}"
    response = requests.get(url)
    return response.json()  # Parse the JSON response

def save_responses(responses):
    with open("ipinfo_responses.json", "w") as file:
        json.dump(responses, file, indent=4)

if __name__ == "__main__":
    ip_addresses = ["102.210.221.2"]  # Add more IP addresses if needed
    all_responses = {}
    
    for ip_address in ip_addresses:
        response = get_response(ip_address)
        all_responses[ip_address] = response
        
    save_responses(all_responses)
    print("Responses saved to ipinfo_responses.json")
