from enum import Enum


class AlertCategory(str, Enum):

    RECONNAISSANCE = "Reconnaissance"

    DENIAL_OF_SERVICE = "Denial of Service"

    MALWARE = "Malware"

    BRUTE_FORCE = "Brute Force"

    ANOMALY = "Anomaly"

    NETWORK = "Network"

    SYSTEM = "System"