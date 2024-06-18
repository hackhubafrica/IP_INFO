from scapy.all import *

def capture_packets(packet_count):
    packets = sniff(count=packet_count)
    return packets

def analyze_packets(packets):
    for packet in packets:
        # Print packet summary
        print(packet.summary())

def main():
    packet_count = 10   # Number of packets to capture

    captured_packets = capture_packets(packet_count)
    analyze_packets(captured_packets)

if __name__ == "__main__":
    main()
