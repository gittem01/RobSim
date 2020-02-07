import cv2
import math

class heatSensor:
    def __init__(self, connection, xMargin, yMargin, sensivity=0.9):
        self.connection = connection
        self.pos = self.connection.pos
        self.xMargin = xMargin
        self.yMargin = yMargin
        self.sensivity = sensivity

    def value(self, img):
        num = img[self.pos[1], self.pos[0], 2]
        if self.pos[1] >= img.shape[0] or self.pos[1] < 0 or self.pos[0] >= img.shape[1] or self.pos[0] < 0:
            return 0
        if num > (1-self.sensivity)*255:
            return 1
        else:
            return 0

    def draw(self, img):
        cp = self.connection.pos
        self.pos = self.connection.definePos(self.xMargin, self.yMargin)
        cv2.circle(img, self.pos, 5, (0, 255, 255), 2)
        cv2.circle(img, self.pos, 10, (255, 0, 0), 1)
