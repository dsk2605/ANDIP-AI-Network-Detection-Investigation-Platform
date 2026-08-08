"""
Centralized detection thresholds for ANDIP.
"""


# =====================================================
# Minimum Flow Requirements
# =====================================================

MIN_FLOW_PACKETS = 100

MIN_FLOW_DURATION = 2.0

ICMP_FLOOD_THRESHOLD = 300


# =====================================================
# Port Scan
# =====================================================

PORT_SCAN_THRESHOLD = 10


# =====================================================
# SYN Flood
# =====================================================

SYN_FLOOD_THRESHOLD = 300


# =====================================================
# UDP Flood
# =====================================================

UDP_FLOOD_THRESHOLD = 300



# =====================================================
# DoS
# =====================================================

DOS_THRESHOLD = 600


# =====================================================
# DDoS
# =====================================================

DDOS_THRESHOLD = 1500
DDOS_PACKET_THRESHOLD = 50
DDOS_SOURCE_THRESHOLD = 10


# =====================================================
# Traffic Spike
# =====================================================

TRAFFIC_SPIKE_THRESHOLD = 1000


# =====================================================
# Generic compatibility aliases
# =====================================================

MIN_PACKETS = MIN_FLOW_PACKETS
MIN_DURATION = MIN_FLOW_DURATION
PACKET_THRESHOLD = MIN_FLOW_PACKETS

# =====================================================
# Traffic Spike
# =====================================================

TRAFFIC_SPIKE_THRESHOLD = 1000

# Compatibility aliases
TRAFFIC_SPIKE_PPS_THRESHOLD = TRAFFIC_SPIKE_THRESHOLD
TRAFFIC_SPIKE_MIN_PACKETS = MIN_FLOW_PACKETS
TRAFFIC_SPIKE_MIN_DURATION = MIN_FLOW_DURATION