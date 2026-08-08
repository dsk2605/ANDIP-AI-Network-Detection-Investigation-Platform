from enum import Enum


class AttackType(str, Enum):

    PORT_SCAN = "Port Scan"

    DOS = "DoS"

    SYN_FLOOD = "SYN Flood"

    UDP_FLOOD = "UDP Flood"

    ICMP_FLOOD = "ICMP Flood"

    HTTP_FLOOD = "HTTP Flood"

    DDOS = "Distributed DoS"

    TRAFFIC_SPIKE = "Traffic Spike"

    UNKNOWN = "Unknown"