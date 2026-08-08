from sqlalchemy.orm import Session

from app.database.repositories.alert_repository import AlertRepository
from app.database.repositories.dashboard_repository import DashboardRepository


class DashboardService:

    def __init__(self, db: Session):
        self.db = db
        self.alert_repo = AlertRepository(db)
        self.dashboard_repo = DashboardRepository(db)

    def get_overview(self):
        """
        Returns dashboard KPI cards.
        """

        alert_stats = self.alert_repo.get_stats()

        return {
            "total_alerts": alert_stats["total_alerts"],
            "critical": alert_stats["critical"],
            "high": alert_stats["high"],
            "medium": alert_stats["medium"],
            "low": alert_stats["low"],
            "today": alert_stats["today"],
            "top_attack": alert_stats["top_attack"],
            "top_source_ip": alert_stats["top_source_ip"],
        }

    def get_severity_distribution(self):
        """
        Returns data for the Severity Distribution pie chart.
        """

        return self.dashboard_repo.get_severity_distribution()

    def get_threat_trend(self):
        """
        Returns data for the Threat Trend line chart.
        """

        return self.dashboard_repo.get_threat_trend()



    def get_recent_events(self, limit: int = 10):
        """
        Returns the latest security events for the dashboard.
        """

        alerts, _ = self.alert_repo.get_alerts(
            skip=0,
            limit=limit,
        )

        return alerts