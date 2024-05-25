#!/usr/bin/env python3
# created by @HackHubAfrica
import socket
import requests
import ipaddress
import psutil
from scapy.all import ARP, Ether, srp

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

def get_local_ip(default_ip='127.0.0.1'):
    """Retrieves your local IP address with a fallback option.

    Args:
        default_ip (str, optional): The default IP address to return if
            unable to determine the local IP. Defaults to '127.0.0.1' (localhost).

    Returns:
        str: Your local IP address if successful, or the default IP otherwise.
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('10.254.254.254', 1))  # Any unreachable address
        local_ip = s.getsockname()[0]
    except Exception:
        local_ip = default_ip
    finally:
        s.close()
    return local_ip

def get_network_info():
    """Retrieves local IP address and subnet mask (if available).

    Returns:
        tuple: A tuple containing (local_ip, subnet_mask) if successful,
            or (None, None) otherwise.
    """
    local_ip = get_local_ip()
    if local_ip is None:
        return None, None

    for iface_name, iface_info in psutil.net_if_addrs().items():
        for addr in iface_info:
            if addr.family == socket.AF_INET and addr.address == local_ip:
                subnet_mask = addr.netmask
                return local_ip, subnet_mask
    return None, None

def calculate_network(ip, mask):
    """Calculates the network address based on IP and subnet mask.

    Args:
        ip (str): The IP address.
        mask (int): The subnet mask in CIDR notation or integer.

    Returns:
        ipaddress.Network: The network object representing the calculated network,
            or None if an error occurs.
    """
    try:
        network = ipaddress.ip_network(f"{ip}/{mask}", strict=False)
        return network
    except Exception as e:
        print(f"Error calculating network: {e}")
        return None


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
      


def scan(ip_range):
    """Scans the specified IP range for devices using ARP requests.

    Args:
        ip_range (str): The IP range to scan in CIDR notation (e.g., '192.168.1.0/24').

    Returns:
        list: A list of dictionaries containing device information (IP and MAC address).
    """
    # Create an ARP request packet
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    result = srp(packet, timeout=2, verbose=0)[0]

    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

# Example usage with proper indentation (assuming sudo privileges for network scanning)
if __name__ == "__main__":
    # Get local IP address (consider using get_my_lan_ip() for public-facing IP)
    local_ip, subnet_mask = get_network_info()
    
    if local_ip and subnet_mask:
        print(f"Local IP: {local_ip}")
        print(f"Subnet Mask: {subnet_mask}")

        # Calculate the network address
        network = calculate_network(local_ip, subnet_mask)
        
        if network:
            print(f"Scanning network: {network}")
            devices = scan(str(network))
            
            print("Devices found:")
            for device in devices:
                print(f"IP: {device['ip']}, MAC: {device['mac']}")
        else:
            print("Error: Unable to calculate network.")
    else:
        print("Error: Unable to get network information.")
