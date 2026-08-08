from datetime import datetime

from app.database.repositories.alert_repository import AlertRepository


class AlertService:

    def __init__(self, repository: AlertRepository):
        self.repository = repository

    def get_alerts(
        self,
        page: int = 1,
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
        skip = (page - 1) * limit

        alerts, total = self.repository.get_alerts(
            skip=skip,
            limit=limit,
            severity=severity,
            attack=attack,
            source_ip=source_ip,
            destination_ip=destination_ip,
            search=search,
            start_date=start_date,
            end_date=end_date,
            sort=sort,
        )

        return {
            "items": alerts,
            "total": total,
            "page": page,
            "limit": limit,
            "pages": (total + limit - 1) // limit,
        }

    def get_alert_by_id(
        self,
        alert_id: int,
    ):
        return self.repository.get_by_id(alert_id)

    def get_stats(self):
        return self.repository.get_stats()