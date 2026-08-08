class DetectorMetrics:

    def __init__(self):

        self.executions = 0
        self.detections = 0

    def executed(self):

        self.executions += 1

    def detected(self):

        self.detections += 1