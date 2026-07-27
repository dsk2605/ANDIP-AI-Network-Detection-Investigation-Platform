from app.models.asset import AssetType, EnvironmentType


def calculate_risk(
    operating_system: str,
    asset_type: AssetType,
    environment: EnvironmentType,
    is_monitored: bool,
) -> int:

    score = 0

    os_name = operating_system.lower()

    if "windows" in os_name:
        score += 20
    elif "linux" in os_name:
        score += 10

    if environment == EnvironmentType.PRODUCTION:
        score += 40

    if asset_type == AssetType.SERVER:
        score += 20
    elif asset_type == AssetType.WORKSTATION:
        score += 10

    if not is_monitored:
        score += 10

    return min(score, 100)