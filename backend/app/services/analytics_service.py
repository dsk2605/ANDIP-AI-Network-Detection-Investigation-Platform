from sqlalchemy import func
from sqlalchemy.orm import Session

from app.database.models.alert import Alert
from app.models.asset import (
    Asset,
    EnvironmentType,
)
from app.models.discovery_scan import DiscoveryScan


class AnalyticsService:

    def __init__(self, db: Session):
        self.db = db

    def get_overview(self):

        total_alerts = self.db.query(Alert).count()

        critical_alerts = (
            self.db.query(Alert)
            .filter(Alert.severity == "Critical")
            .count()
        )

        total_assets = self.db.query(Asset).count()

        total_scans = self.db.query(DiscoveryScan).count()

        average_risk_score = (
            self.db.query(func.avg(Asset.risk_score))
            .scalar()
            or 0
        )

        return {
            "total_alerts": total_alerts,
            "critical_alerts": critical_alerts,
            "total_assets": total_assets,
            "total_scans": total_scans,
            "average_risk_score": round(
                average_risk_score,
                2,
            ),
        }

    def get_top_risk_assets(self):

        return (
            self.db.query(Asset)
            .order_by(Asset.risk_score.desc())
            .limit(10)
            .all()
        )

    def get_os_distribution(self):

        results = (
            self.db.query(
                Asset.operating_system,
                func.count(Asset.id),
            )
            .group_by(Asset.operating_system)
            .all()
        )

        return [
            {
                "operating_system": operating_system,
                "count": count,
            }
            for operating_system, count in results
        ]

    def get_environment_distribution(self):

        results = (
            self.db.query(
                Asset.environment,
                func.count(Asset.id),
            )
            .group_by(Asset.environment)
            .all()
        )

        return [
            {
                "environment": environment.value,
                "count": count,
            }
            for environment, count in results
        ]

    def get_asset_type_distribution(self):

        results = (
            self.db.query(
                Asset.asset_type,
                func.count(Asset.id),
            )
            .group_by(Asset.asset_type)
            .all()
        )

        return [
            {
                "asset_type": asset_type.value,
                "count": count,
            }
            for asset_type, count in results
        ]

    def get_security_recommendations(self):

        recommendations = []

        high_risk_assets = (
            self.db.query(Asset)
            .filter(Asset.risk_score >= 80)
            .count()
        )

        if high_risk_assets:
            recommendations.append({
                "priority": "HIGH",
                "message": (
                    f"{high_risk_assets} high-risk asset(s) "
                    "require immediate attention."
                ),
            })

        production_assets = (
            self.db.query(Asset)
            .filter(
                Asset.environment == EnvironmentType.PRODUCTION
            )
            .count()
        )

        if production_assets:
            recommendations.append({
                "priority": "MEDIUM",
                "message": (
                    f"{production_assets} production asset(s) "
                    "should be continuously monitored."
                ),
            })

        average_risk = (
            self.db.query(
                func.avg(Asset.risk_score)
            )
            .scalar()
            or 0
        )

        if average_risk >= 40:
            recommendations.append({
                "priority": "MEDIUM",
                "message": (
                    "Average asset risk is increasing. "
                    "Review vulnerable assets."
                ),
            })
        else:
            recommendations.append({
                "priority": "LOW",
                "message": (
                    "Overall asset risk is low. "
                    "Continue regular monitoring."
                ),
            })

        total_scans = (
            self.db.query(DiscoveryScan)
            .count()
        )

        recommendations.append({
            "priority": "LOW",
            "message": (
                f"{total_scans} discovery scan(s) "
                "have been completed successfully."
            ),
        })

        return recommendations

    def get_discovery_summary(self):

        total_scans = (
            self.db.query(DiscoveryScan)
            .count()
        )

        total_hosts = (
            self.db.query(
                func.sum(
                    DiscoveryScan.hosts_found
                )
            )
            .scalar()
            or 0
        )

        average_hosts = (
            total_hosts / total_scans
            if total_scans > 0
            else 0
        )

        latest_scan = (
            self.db.query(DiscoveryScan)
            .order_by(
                DiscoveryScan.started_at.desc()
            )
            .first()
        )

        return {
            "total_scans": total_scans,
            "total_hosts_discovered": total_hosts,
            "average_hosts_per_scan": round(
                average_hosts,
                2,
            ),
            "latest_scan": (
                latest_scan.started_at
                if latest_scan
                else None
            ),
        }