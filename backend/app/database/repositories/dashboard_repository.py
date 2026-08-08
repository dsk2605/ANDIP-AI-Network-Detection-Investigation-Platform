from datetime import datetime, timedelta

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.database.models.alert import Alert


class DashboardRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_severity_distribution(self):
        """
        Returns alert count grouped by severity.
        """

        rows = (
            self.db.query(
                Alert.severity,
                func.count(Alert.id).label("count"),
            )
            .group_by(Alert.severity)
            .all()
        )

        return [
            {
                "severity": severity,
                "count": count,
            }
            for severity, count in rows
        ]

    def get_threat_trend(self):
        """
        Returns alert counts for the last 8 hours
        in Asia/Kolkata timezone.
        """

        # Get latest alert in IST
        latest_timestamp = (
            self.db.query(
                func.max(
                    func.timezone(
                        "Asia/Kolkata",
                        Alert.timestamp,
                    )
                )
            )
            .scalar()
        )

        if latest_timestamp is None:
            latest_timestamp = datetime.now()

        now = latest_timestamp.replace(
            minute=0,
            second=0,
            microsecond=0,
        )

        start_time = now - timedelta(hours=7)

        rows = (
            self.db.query(
                func.date_trunc(
                    "hour",
                    func.timezone(
                        "Asia/Kolkata",
                        Alert.timestamp,
                    ),
                ).label("hour"),
                func.count(Alert.id).label("alerts"),
            )
            .filter(
                func.timezone(
                    "Asia/Kolkata",
                    Alert.timestamp,
                ) >= start_time
            )
            .filter(
                func.timezone(
                    "Asia/Kolkata",
                    Alert.timestamp,
                ) < now + timedelta(hours=1)
            )
            .group_by("hour")
            .order_by("hour")
            .all()
        )

        counts = {
            row.hour.replace(
                minute=0,
                second=0,
                microsecond=0,
            ): row.alerts
            for row in rows
        }

        trend = []

        current = start_time

        while current <= now:
            trend.append(
                {
                    "time": current.strftime("%H:00"),
                    "alerts": counts.get(current, 0),
                }
            )
            current += timedelta(hours=1)

        return trend