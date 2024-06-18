import socket

def resolve_domain_to_ip(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror as e:
        return f"Error resolving domain: {e}"

if __name__ == "__main__":
    domain = input("Enter a domain name: ")
    ip_address = resolve_domain_to_ip(domain)
    print(f"The IP address of {domain} is {ip_address}")
