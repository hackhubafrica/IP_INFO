import socket

def dns_lookup(domain, record_type="A"):
  try:
    # Perform DNS lookup using socket library
    return socket.gethostbyname_ex(domain)[record_type]
  except socket.gaierror as e:
    print(f"Error: {domain} - {e}")
    return None

if __name__ == "__main__":
  while True:
    # Prompt user for domain name
    domain = input("Enter a domain name (or 'q' to quit): ")

    if domain.lower() == 'q':
      break

    # Perform lookup and display results
    ip_addresses = dns_lookup(domain)
    if ip_addresses:
      print(f"{domain}: {', '.join(ip_addresses)}")
    else:
      print(f"No records found for {domain}")
