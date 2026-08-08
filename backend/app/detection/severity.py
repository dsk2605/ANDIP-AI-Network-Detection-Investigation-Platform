from enum import Enum


class Severity(str, Enum):

    INFO = "Info"

    LOW = "Low"

    MEDIUM = "Medium"

    HIGH = "High"

    CRITICAL = "Critical"