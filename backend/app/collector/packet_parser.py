from datetime import datetime

from scapy.layers.inet import ICMP, IP, TCP, UDP

from app.collector.packet_models import PacketData


class PacketParser:

    def parse(self, packet):

        if not packet.haslayer(IP):
            return None

        source_port = None
        destination_port = None

        protocol = "OTHER"

        tcp_flags = None
        window_size = None

        icmp_type = None
        icmp_code = None

        if packet.haslayer(TCP):

            protocol = "TCP"

            source_port = packet[TCP].sport
            destination_port = packet[TCP].dport

            tcp_flags = str(packet[TCP].flags)
            window_size = packet[TCP].window

        elif packet.haslayer(UDP):

            protocol = "UDP"

            source_port = packet[UDP].sport
            destination_port = packet[UDP].dport

        elif packet.haslayer(ICMP):

            protocol = "ICMP"

            icmp_type = packet[ICMP].type
            icmp_code = packet[ICMP].code

        return PacketData(

            timestamp=datetime.now(),

            source_ip=packet[IP].src,
            destination_ip=packet[IP].dst,

            source_port=source_port,
            destination_port=destination_port,

            protocol=protocol,

            packet_size=len(packet),

            ttl=packet[IP].ttl,

            tcp_flags=tcp_flags,
            window_size=window_size,

            icmp_type=icmp_type,
            icmp_code=icmp_code,
        )