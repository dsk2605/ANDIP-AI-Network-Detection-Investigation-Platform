from datetime import datetime, timedelta

from app.detection.flow import NetworkFlow


class FlowManager:

    FLOW_TIMEOUT = 30  # seconds

    def __init__(self):

        self.flows = {}

    def _cleanup(self):

        now = datetime.now()

        expired = []

        for key, flow in self.flows.items():

            if (
                now - flow.last_seen
            ) > timedelta(
                seconds=self.FLOW_TIMEOUT,
            ):
                expired.append(key)

        for key in expired:
            del self.flows[key]

    def process_packet(
        self,
        packet,
    ):

        self._cleanup()

        key = (
            packet.source_ip,
            packet.destination_ip,
            packet.source_port,
            packet.destination_port,
            packet.protocol,
        )

        if key not in self.flows:

            self.flows[key] = NetworkFlow(
                source_ip=packet.source_ip,
                destination_ip=packet.destination_ip,
                source_port=packet.source_port,
                destination_port=packet.destination_port,
                protocol=packet.protocol,

                packet_count=0,
                total_bytes=0,

                packet_delta=0,
                byte_delta=0,

                tcp_flags=packet.tcp_flags,
                window_size=packet.window_size,

                icmp_type=packet.icmp_type,
                icmp_code=packet.icmp_code,

                first_seen=datetime.now(),
                last_seen=datetime.now(),
            )

        flow = self.flows[key]

        # =====================================================
        # Delta Statistics
        # =====================================================

        flow.packet_delta = 1
        flow.byte_delta = packet.packet_size

        # =====================================================
        # Latest Packet Metadata
        # =====================================================

        flow.tcp_flags = packet.tcp_flags
        flow.window_size = packet.window_size

        flow.icmp_type = packet.icmp_type
        flow.icmp_code = packet.icmp_code

        # =====================================================
        # Flow Totals
        # =====================================================

        flow.packet_count += flow.packet_delta
        flow.total_bytes += flow.byte_delta

        flow.last_seen = datetime.now()

        return flow