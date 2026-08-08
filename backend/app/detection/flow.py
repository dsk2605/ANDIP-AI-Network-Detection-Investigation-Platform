from dataclasses import dataclass
from datetime import datetime


@dataclass
class NetworkFlow:

    # =====================================================
    # Flow Identity
    # =====================================================

    source_ip: str
    destination_ip: str

    source_port: int | None
    destination_port: int | None

    protocol: str

    # =====================================================
    # Traffic Statistics
    # =====================================================

    packet_count: int = 0
    total_bytes: int = 0

    packet_delta: int = 0
    byte_delta: int = 0

    # =====================================================
    # TCP Metadata
    # =====================================================

    tcp_flags: str | None = None
    window_size: int | None = None

    # =====================================================
    # ICMP Metadata
    # =====================================================

    icmp_type: int | None = None
    icmp_code: int | None = None

    # =====================================================
    # Timing
    # =====================================================

    first_seen: datetime | None = None
    last_seen: datetime | None = None

    # =====================================================
    # Properties
    # =====================================================

    @property
    def duration_seconds(self) -> float:
        """
        Returns the lifetime of the flow in seconds.
        """

        if self.first_seen is None or self.last_seen is None:
            return 0.0

        return (
            self.last_seen - self.first_seen
        ).total_seconds()

    @property
    def packets_per_second(self) -> float:
        """
        Average packets per second.
        """

        duration = self.duration_seconds

        if duration <= 0:
            return 0.0

        return self.packet_count / duration

    @property
    def bytes_per_second(self) -> float:
        """
        Average bytes per second.
        """

        duration = self.duration_seconds

        if duration <= 0:
            return 0.0

        return self.total_bytes / duration

    @property
    def flow_key(self):
        """
        Returns a unique identifier for the flow.
        """

        return (
            self.source_ip,
            self.destination_ip,
            self.source_port,
            self.destination_port,
            self.protocol,
        )