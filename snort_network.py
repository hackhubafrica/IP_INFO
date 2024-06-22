from scapy.all import *
import json

def capture_packets(packet_count):
    packets = sniff(count=packet_count)
    return packets

def analyze_packets(packets):
    packet_summaries = []
    detailed_info = []

    for packet in packets:
        # Print packet summary
        summary = packet.summary()
        print(summary)
        packet_summaries.append(summary)
        
        # Collect detailed packet information
        detailed_packet_info = packet.show(dump=True)
        detailed_info.append(detailed_packet_info)

    return packet_summaries, detailed_info

def save_to_file(packet_summaries, detailed_info, filename="captured_packets.json"):
    data = {
        "packet_summaries": packet_summaries,
        "detailed_info": detailed_info
    }

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    packet_count = 20  # Number of packets to capture

    captured_packets = capture_packets(packet_count)
    packet_summaries, detailed_info = analyze_packets(captured_packets)
    save_to_file(packet_summaries, detailed_info)

if __name__ == "__main__":
    main()
