from typing import Any, Dict


class DiscoveryValidator:
    """Validates normalized discovery data."""

    def validate(self, asset: Dict[str, Any]) -> bool:
        """
        Validate a normalized asset.

        Returns:
            True if the asset is valid, otherwise False.
        """

        # IP address is mandatory
        if not asset.get("ip_address"):
            return False

        return True