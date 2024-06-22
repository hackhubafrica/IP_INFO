from scapy.all import *
import json

def capture_packets(packet_count):
    packets = sniff(count=packet_count)
    return packets

def analyze_packets(packets):
    captured_packets = []

    for packet in packets:
        # Create a dictionary to store packet information
        packet_info = {}

        # Ethernet layer information
        ether_info = {
            "dst": packet.dst,
            "src": packet.src,
            "type": packet.type
        }
        packet_info["Ethernet"] = ether_info

        # IP layer information if present
        if IP in packet:
            ip_info = {
                "version": packet[IP].version,
                "ihl": packet[IP].ihl,
                "tos": hex(packet[IP].tos),
                "len": packet[IP].len,
                "id": packet[IP].id,
                "flags": packet[IP].flags,
                "frag": packet[IP].frag,
                "ttl": packet[IP].ttl,
                "proto": packet[IP].proto,
                "chksum": hex(packet[IP].chksum),
                "src": packet[IP].src,
                "dst": packet[IP].dst
            }
            packet_info["IP"] = ip_info

        # TCP layer information if present
        if TCP in packet:
            tcp_info = {
                "sport": packet[TCP].sport,
                "dport": packet[TCP].dport,
                "seq": packet[TCP].seq,
                "ack": packet[TCP].ack,
                "dataofs": packet[TCP].dataofs,
                "reserved": packet[TCP].reserved,
                "flags": packet[TCP].flags,
                "window": packet[TCP].window,
                "chksum": hex(packet[TCP].chksum),
                "urgptr": packet[TCP].urgptr,
                "options": packet[TCP].options
            }
            packet_info["TCP"] = tcp_info

        # Raw layer information if present
        if Raw in packet:
            raw_info = {
                "load": repr(packet[Raw].load)  # Convert bytes to a printable representation
            }
            packet_info["Raw"] = raw_info

        # Add packet_info to captured_packets list
        captured_packets.append(packet_info)

    return captured_packets

def save_to_file(captured_packets, filename="captured_packets.json"):
    with open(filename, 'w') as file:
        json.dump(captured_packets, file, indent=4)

def main():
    packet_count = 10   # Number of packets to capture

    captured_packets = capture_packets(packet_count)
    save_to_file(captured_packets)

if __name__ == "__main__":
    main()
