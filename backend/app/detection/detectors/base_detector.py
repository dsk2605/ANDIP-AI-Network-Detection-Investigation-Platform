from abc import ABC, abstractmethod

from app.detection.detection_context import DetectionContext
from app.detection.detectors.detector_state import DetectorState


class BaseDetector(ABC):

    WINDOW_SECONDS = 5
    COOLDOWN_SECONDS = 30

    def __init__(self):

        self.context = DetectionContext()
        self.state = DetectorState()

    @abstractmethod
    def analyze(
        self,
        flow,
    ):
        ...