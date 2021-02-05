from __future__ import division
from .left_eye import LeftEye
from .right_eye import RightEye
from .eyebrow import Eyebrow
from .smile import Smile
import cv2
import dlib
import os
import numpy as np


class Decision(object):

    def __init__(self):

        cwd = os.path.abspath(os.path.dirname(__file__))
        model_path = os.path.abspath(os.path.join(cwd, "trained_models/shape_predictor_68_face_landmarks.dat"))
        self.predictor = dlib.shape_predictor(model_path)

        self.detector = dlib.get_frontal_face_detector()

        self.frame = None
        self.left_eye = None
        self.right_eye = None
        self.smile = None
        self.eyebrow = None
        self.index = None
        self.array = None
        self.counter = None

    def refresh(self, frame, index):
        self.index = index
        self.frame = frame
        self.analyze()

    def analyze(self):
        frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        faces = self.detector(frame)

        try:
            landmarks = self.predictor(frame, faces[0])
            self.left_eye = LeftEye(frame, landmarks, self.index)
            self.right_eye = RightEye(frame, landmarks, self.index)
            self.eyebrow = Eyebrow(frame, landmarks, self.index)
            self.smile = Smile(frame, landmarks, self.index)

        except IndexError:
            self.left_eye = None
            self.right_eye = None
            self.smile = None
            self.eyebrow = None

    def control(self):
        left_eye = self.left_eye.control()
        right_eye = self.right_eye.control()
        eyebrow = self.eyebrow.control()
        smile = self.smile.control()
        array = np.array([left_eye, right_eye, eyebrow, smile])
        return array

    def password(self, array):
        self.array = array
        self.compare()

    def compare(self):
        left_eye = self.left_eye.decide()
        right_eye = self.right_eye.decide()
        eyebrow = self.eyebrow.decide()
        smile = self.smile.decide()

        array = np.array([left_eye, right_eye, eyebrow, smile])
        if (array == self.array).all():
            return 1
        else:
            return 0
