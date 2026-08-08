from app.detection.detectors.ddos_detector import DDoSDetector
from app.detection.detectors.dos_detector import DoSDetector
from app.detection.detectors.icmp_flood_detector import IcmpFloodDetector
from app.detection.detectors.port_scan_detector import PortScanDetector
from app.detection.detectors.spike_detector import SpikeDetector
from app.detection.detectors.syn_flood_detector import SynFloodDetector
from app.detection.detectors.udp_flood_detector import UdpFloodDetector


class DetectorRegistry:

    @staticmethod
    def get_detectors():

        return [

            #
            # Specific attack detectors first
            #

            DDoSDetector(),

            SynFloodDetector(),

            UdpFloodDetector(),

            IcmpFloodDetector(),

            PortScanDetector(),

            SpikeDetector(),

            #
            # Generic detector LAST
            #

            DoSDetector(),

        ]