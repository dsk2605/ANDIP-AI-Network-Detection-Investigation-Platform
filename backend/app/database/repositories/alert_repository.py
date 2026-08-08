from datetime import datetime, timedelta, time

from sqlalchemy import func, or_
from sqlalchemy.orm import Session

from app.database.models.alert import Alert


class AlertRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, alert: Alert) -> Alert:
        self.db.add(alert)
        self.db.commit()
        self.db.refresh(alert)
        return alert

    def get_alerts(
        self,
        skip: int = 0,
        limit: int = 25,
        severity: str | None = None,
        attack: str | None = None,
        source_ip: str | None = None,
        destination_ip: str | None = None,
        search: str | None = None,
        start_date: datetime | None = None,
        end_date: datetime | None = None,
        sort: str = "desc",
    ):
        query = self.db.query(Alert)

        # Severity Filter
        if severity:
            query = query.filter(Alert.severity == severity)

        # Attack Filter
        if attack:
            query = query.filter(Alert.attack == attack)

        # Source IP Filter
        if source_ip:
            query = query.filter(Alert.source_ip == source_ip)

        # Destination IP Filter
        if destination_ip:
            query = query.filter(Alert.destination_ip == destination_ip)

        # Date Range Filter
        if start_date:
            start_datetime = datetime.combine(
                start_date.date(),
                time.min,
            )
            query = query.filter(
                Alert.timestamp >= start_datetime
            )

        if end_date:
            end_datetime = datetime.combine(
                end_date.date(),
                time.max,
            )
            query = query.filter(
                Alert.timestamp <= end_datetime
            )

        # Global Search
        if search:
            query = query.filter(
                or_(
                    Alert.attack.ilike(f"%{search}%"),
                    Alert.description.ilike(f"%{search}%"),
                    Alert.source_ip.ilike(f"%{search}%"),
                    Alert.destination_ip.ilike(f"%{search}%"),
                )
            )

        # Sorting
        if sort.lower() == "asc":
            query = query.order_by(Alert.timestamp.asc())
        else:
            query = query.order_by(Alert.timestamp.desc())

        total = query.count()

        alerts = (
            query
            .offset(skip)
            .limit(limit)
            .all()
        )

        return alerts, total

    def get_by_id(
        self,
        alert_id: int,
    ):
        return (
            self.db.query(Alert)
            .filter(Alert.id == alert_id)
            .first()
        )

    def get_stats(self):
        total_alerts = self.db.query(Alert).count()

        critical = (
            self.db.query(Alert)
            .filter(Alert.severity == "Critical")
            .count()
        )

        high = (
            self.db.query(Alert)
            .filter(Alert.severity == "High")
            .count()
        )

        medium = (
            self.db.query(Alert)
            .filter(Alert.severity == "Medium")
            .count()
        )

        low = (
            self.db.query(Alert)
            .filter(Alert.severity == "Low")
            .count()
        )

        today = (
            self.db.query(Alert)
            .filter(
                Alert.timestamp >= datetime.utcnow() - timedelta(days=1)
            )
            .count()
        )

        top_attack = (
            self.db.query(
                Alert.attack,
                func.count(Alert.attack).label("count"),
            )
            .group_by(Alert.attack)
            .order_by(func.count(Alert.attack).desc())
            .first()
        )

        top_source_ip = (
            self.db.query(
                Alert.source_ip,
                func.count(Alert.source_ip).label("count"),
            )
            .group_by(Alert.source_ip)
            .order_by(func.count(Alert.source_ip).desc())
            .first()
        )

        return {
            "total_alerts": total_alerts,
            "critical": critical,
            "high": high,
            "medium": medium,
            "low": low,
            "today": today,
            "top_attack": top_attack[0] if top_attack else None,
            "top_source_ip": top_source_ip[0] if top_source_ip else None,
        }