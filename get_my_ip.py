import socket
import requests
import socket
import ipaddress
import psutil
import platform


def get_my_lan_ip():
  """Retrieves your local IP address on the LAN.

  Returns:
      str: Your LAN IP address if successful, or None otherwise.
  """
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  try:
      s.connect(("8.8.8.8", 80))  # Connect to a public server (replace if needed)
      ip = s.getsockname()[0]
      return ip
  except Exception as e:
      print(f"Error: Unable to get IP address: {e}")
      return None
  finally:
      s.close()

if __name__ == "__main__":
  my_ip = get_my_lan_ip()
  if my_ip:
      print(f"Your LAN IP address: {my_ip}")
  else:
      print("Failed to retrieve LAN IP address.")

def get_public_ip():
  """Fetches your public IP address using a free external API.

  Returns:
      str: Your public IP address (if successful), or None if an error occurs.
  """
  url = "https://ident.me/"  # You can use https://v4.ident.me/ for IPv4-only
  try:
      response = requests.get(url)
      response.raise_for_status()  # Raise an exception for non-200 status codes
      return response.text.strip()
  except requests.exceptions.RequestException as e:
      print(f"Error: Unable to reach the API: {e}")
      return None

if __name__ == "__main__":
  public_ip = get_public_ip()
  if public_ip:
      print(f"Your public IP address: {public_ip}")
  else:
      print("Failed to retrieve public IP address.")
      
      
      
def get_local_ip():
    try:
        # Create a socket and get the local IP address
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception as e:
        print(f"Error obtaining local IP: {e}")
        return None

def get_network_info():
    try:
        local_ip = get_local_ip()
        if local_ip is None:
            return None, None

        for iface_name, iface_info in psutil.net_if_addrs().items():
            for addr in iface_info:
                if addr.family == socket.AF_INET and addr.address == local_ip:
                    subnet_mask = addr.netmask
                    return local_ip, subnet_mask
        return None, None
    except Exception as e:
        print(f"Error obtaining network info: {e}")
        return None, None

def calculate_network(ip, mask):
    try:
        # Calculate the network address
        network = ipaddress.ip_network(f"{ip}/{mask}", strict=False)
        return network
    except Exception as e:
        print(f"Error calculating network: {e}")
        return None

if __name__ == "__main__":
    local_ip, subnet_mask = get_network_info()
    if local_ip and subnet_mask:
        print(f"Local IP Address: {local_ip}")
        print(f"Subnet Mask: {subnet_mask}")
        network = calculate_network(local_ip, subnet_mask)
        if network:
            print(f"Network: {network}")
        else:
            print("Failed to calculate network.")
    else:
        print("Failed to get local IP address or subnet mask.")


    
      
      
      
