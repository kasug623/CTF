from scapy.all import *

# Read packets
packets = rdpcap("./capture.pcap")

# List to store extracted UDP source ports
udp_src_ports = []

# Iterate over packets and extract UDP source ports
for packet in packets:
    if packet.haslayer(IP) and packet[IP].dst == "10.0.0.1" and packet.haslayer(UDP) and packet[UDP].dport == 22:
        udp_src_ports.append(packet[UDP].sport)

# Output the list of UDP source ports
print(udp_src_ports)

a = [num - 5000 for num in udp_src_ports if num >= 5000]
print(a)

flag = ""
for i in a:
    flag += chr(i)
print(flag)