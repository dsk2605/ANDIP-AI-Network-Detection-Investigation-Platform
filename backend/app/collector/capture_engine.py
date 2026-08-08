from scapy.all import sniff

from app.collector.packet_parser import PacketParser
from app.core.logging import get_logger

logger = get_logger(__name__)


class PacketCaptureEngine:

    def __init__(self):
        self.parser = PacketParser()

        logger.info("PacketCaptureEngine initialized.")

    def start_capture(
        self,
        interface=None,
        packet_count=0,
        packet_callback=None,
    ):

        logger.info(
            "Starting packet capture | Interface=%s | Packet Count=%s",
            interface if interface else "Default",
            "Unlimited" if packet_count == 0 else packet_count,
        )

        def process_packet(packet):

            try:
                parsed_packet = self.parser.parse(packet)

                if parsed_packet is None:
                    return

                logger.debug(
                    "Packet parsed successfully | %s -> %s | %s",
                    parsed_packet.source_ip,
                    parsed_packet.destination_ip,
                    parsed_packet.protocol,
                )

                if packet_callback:
                    packet_callback(parsed_packet)
                else:
                    logger.debug(parsed_packet)

            except Exception:
                logger.exception("Error while processing captured packet.")

        try:
            sniff(
                iface=interface,
                prn=process_packet,
                store=False,
                count=packet_count,
            )

        except KeyboardInterrupt:
            logger.info("Packet capture stopped by user.")

        except Exception:
            logger.exception("Packet capture engine crashed.")
            raise