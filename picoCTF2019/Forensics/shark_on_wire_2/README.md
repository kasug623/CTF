a little guess ctf for me.  

# Lesson
- a usage of `Scapy`

# Memo
1. check `Wireshark`
2. extract suspicious packets
    ```zsh
    $ tshark -r ./capture.pcap -Y "ip.dst==10.0.0.1 && udp.dstport==22" -T fields -e udp.srcport | tr '\n' ', '
    5000,5112,5105,5099,5111,5067,5084,5070,5123,5112,5049,5076,5076,5102,5051,5114,5051,5100,5095,5100,5097,5116,5097,5095,5118,5049,5097,5095,5115,5116,5051,5103,5048,5125,5000,
    ```
3. guess and translate with `Scapy`  
    solver.py
