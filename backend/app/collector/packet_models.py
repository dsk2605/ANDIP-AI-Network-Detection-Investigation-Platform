from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class PacketData:
    """
    Normalized packet representation used throughout
    the ANDIP processing pipeline.
    """

    timestamp: datetime

    source_ip: str | None
    destination_ip: str |None

    source_port: int | None
    destination_port: int | None

    protocol: str

    packet_size: int

    # -------------------------
    # TCP Metadata
    # -------------------------

    tcp_flags: str | None = None

    window_size: int | None = None

    # -------------------------
    # IP Metadata
    # -------------------------

    ttl: int | None = None

    # -------------------------
    # ICMP Metadata
    # -------------------------

    icmp_type: int | None = None

    icmp_code: int | None = None