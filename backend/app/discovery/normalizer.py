from typing import Any, Dict, List
import xml.etree.ElementTree as ET


class DiscoveryNormalizer:
    """Converts scanner output into ANDIP's internal format."""

    def normalize_nmap(self, xml_data: str) -> List[Dict[str, Any]]:
        """
        Convert Nmap XML into ANDIP's internal asset format.
        """

        assets: List[Dict[str, Any]] = []

        root = ET.fromstring(xml_data)

        for host in root.findall("host"):

            status = host.find("status")
            if status is None or status.attrib.get("state") != "up":
                continue

            ip_address = None
            mac_address = None
            vendor = None

            for address in host.findall("address"):
                addr_type = address.attrib.get("addrtype")

                if addr_type == "ipv4":
                    ip_address = address.attrib.get("addr")

                elif addr_type == "mac":
                    mac_address = address.attrib.get("addr")
                    vendor = address.attrib.get("vendor")

            hostname = None
            hostnames = host.find("hostnames")
            if hostnames is not None:
                hostname_node = hostnames.find("hostname")
                if hostname_node is not None:
                    hostname = hostname_node.attrib.get("name")

            operating_system = None
            os_node = host.find("os")
            if os_node is not None:
                osmatch = os_node.find("osmatch")
                if osmatch is not None:
                    operating_system = osmatch.attrib.get("name")

            ports = []

            ports_node = host.find("ports")

            if ports_node is not None:

                for port in ports_node.findall("port"):

                    state = port.find("state")
                    service = port.find("service")

                    ports.append(
                        {
                            "port": int(port.attrib.get("portid")),
                            "protocol": port.attrib.get("protocol"),
                            "state": state.attrib.get("state") if state is not None else None,
                            "service": service.attrib.get("name") if service is not None else None,
                            "product": service.attrib.get("product") if service is not None else None,
                            "version": service.attrib.get("version") if service is not None else None,
                        }
                    )

            assets.append(
                {
                    "ip_address": ip_address,
                    "mac_address": mac_address,
                    "hostname": hostname,
                    "operating_system": operating_system,
                    "vendor": vendor,
                    "ports": ports,
                }
            )

        return assets