from abc import ABC, abstractmethod
from typing import Any, Dict, List


class BaseScanner(ABC):
    """Base interface for all discovery scanners."""

    @abstractmethod
    def scan(self, target: str) -> List[Dict[str, Any]]:
        """
        Scan a target network or host.

        Args:
            target: Target IP, hostname, or CIDR range.

        Returns:
            A list of discovered hosts in ANDIP's internal format.
        """
        pass