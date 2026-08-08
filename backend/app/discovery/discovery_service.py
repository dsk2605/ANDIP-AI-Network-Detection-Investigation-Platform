from typing import List, Dict, Any
from sqlalchemy.orm import Session

from app.discovery.nmap_scanner import NmapScanner
from app.discovery.normalizer import DiscoveryNormalizer
from app.discovery.validator import DiscoveryValidator
from app.services.asset_observation_service import AssetObservationService

from app.services.asset_reconciliation_service import (
    AssetReconciliationService,
)

class DiscoveryService:
    """Coordinates the discovery workflow."""

    def __init__(self, db: Session):
        self.db = db
        self.scanner = NmapScanner()
        self.normalizer = DiscoveryNormalizer()
        self.validator = DiscoveryValidator()
        self.observation_service = AssetObservationService(db)
        self.reconciliation_service = AssetReconciliationService(db)

    def discover(self, target: str, scan_id):

        raw_results = self.scanner.scan(target)

        print("=" * 50)
        print("RAW RESULTS")
        print(raw_results)
        print("=" * 50)

        discovered_assets = []

        for result in raw_results:

            assets = self.normalizer.normalize_nmap(result["xml"])

            print("NORMALIZED ASSETS")
            print(assets)

            for asset in assets:

                print("VALIDATING")
                print(asset)

                if not self.validator.validate(asset):
                    print("FAILED VALIDATION")
                    continue

                print("PASSED VALIDATION")

                observation = self.observation_service.create_observation(
                    scan_id=scan_id,
                    asset_data=asset,
                )
                
                self.reconciliation_service.reconcile(observation)
                discovered_assets.append(observation)

        self.db.commit()

        return discovered_assets