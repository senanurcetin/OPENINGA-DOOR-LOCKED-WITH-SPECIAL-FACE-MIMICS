from __future__ import division
from math import hypot


class Smile(object):

    SMILE_POINTS = [48, 50, 52, 54, 56, 58]

    def __init__(self, frame, landmarks, index):
        self.check = None
        self.index = None
        self.decision = None
        self.analyze(frame, landmarks, index)

    @staticmethod
    def midpoint(p1, p2):
        x = int((p1.x + p2.x) / 2)
        y = int((p1.y + p2.y) / 2)
        return x, y

    def analyze(self, frame, landmarks, index):
        points = self.SMILE_POINTS
        self.smiling(landmarks, points)
        self.index = index

    def smiling(self, landmarks, points):
        left_point = (landmarks.part(points[0]).x, landmarks.part(points[0]).y)
        right_point = (landmarks.part(points[3]).x, landmarks.part(points[3]).y)
        center_top = self.midpoint(landmarks.part(points[1]), landmarks.part(points[2]))
        center_bottom = self.midpoint(landmarks.part(points[5]), landmarks.part(points[4]))

        hor_line_length = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
        ver_line_length = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))

        ratio = (hor_line_length - ver_line_length) / (2*ver_line_length)
        self.check = ratio

    def control(self):
        if self.check < 0.6:
            self.decision = 1
            return self.decision
        else:
            self.decision = 0
            return self.decision

    def decide(self):
        if self.index == 3:
            return self.decision
        else:
            self.decision = 0
            return self.decision
