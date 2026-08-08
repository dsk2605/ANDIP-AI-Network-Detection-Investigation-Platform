from scapy.all import get_if_list

from app.core.logging import get_logger

logger = get_logger(__name__)


class InterfaceManager:

    @staticmethod
    def list_interfaces():
        """
        Return all available network interfaces.
        """

        try:
            interfaces = get_if_list()

            logger.info(
                "Discovered %d network interface(s).",
                len(interfaces),
            )

            logger.debug("Interfaces: %s", interfaces)

            return interfaces

        except Exception:
            logger.exception("Failed to retrieve network interfaces.")
            return []