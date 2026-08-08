from app.alerts.cooldown import AlertCooldown
from app.alerts.database_service import AlertDatabaseService
from app.core.logging import get_logger
from app.database.models.alert import Alert
from app.detection.detection_result import DetectionResult

logger = get_logger(__name__)


class AlertManager:

    def __init__(self):
        self.cooldown = AlertCooldown(
            cooldown_seconds=60,
        )

    def raise_alert(
        self,
        result: DetectionResult,
    ):

        key = (
            f"{result.attack.value}:"
            f"{result.source_ip}"
        )

        if not self.cooldown.can_alert(key):

            logger.info(
                "Alert suppressed by cooldown | Attack=%s | Source=%s",
                result.attack.value,
                result.source_ip,
            )

            return

        db_alert = Alert(
            attack=result.attack.value,
            severity=result.severity.value,
            source_ip=result.source_ip,
            destination_ip=result.destination_ip,
            description=result.description,
            details={
                "category": result.category.value,
                "protocol": result.protocol,
                "confidence": result.confidence,
                **result.metadata,
            },
            timestamp=result.detected_at,
        )

        logger.warning("=" * 60)
        logger.warning("SECURITY ALERT DETECTED")
        logger.warning("=" * 60)

        logger.warning("Attack      : %s", db_alert.attack)
        logger.warning("Severity    : %s", db_alert.severity)
        logger.warning("Source IP   : %s", db_alert.source_ip)
        logger.warning("Destination : %s", db_alert.destination_ip)
        logger.warning("Description : %s", db_alert.description)

        if db_alert.details:
            logger.warning("Details     : %s", db_alert.details)

        logger.warning("=" * 60)

        try:

            AlertDatabaseService.save(db_alert)

            logger.info(
                "Alert saved successfully | Attack=%s | Source=%s",
                db_alert.attack,
                db_alert.source_ip,
            )

        except Exception:

            logger.exception(
                "Failed to save alert | Attack=%s | Source=%s",
                db_alert.attack,
                db_alert.source_ip,
            )

            raise


alert_manager = AlertManager()