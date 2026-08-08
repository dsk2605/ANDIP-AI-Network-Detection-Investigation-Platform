from app.database.models.alert import Alert as AlertModel
from app.database.repositories.alert_repository import AlertRepository
from app.database.session import SessionLocal


class AlertDatabaseService:

    @staticmethod
    def save(alert):

        db = SessionLocal()

        try:
            repo = AlertRepository(db)

            db_alert = AlertModel(
                attack=alert.attack,
                severity=alert.severity,
                source_ip=alert.source_ip,
                destination_ip=alert.destination_ip,
                description=alert.description,
                details=alert.details,
                timestamp=alert.timestamp,
            )

            repo.create(db_alert)

        finally:
            db.close()