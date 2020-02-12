from .Funcs import *
import cv2
import math

class Vehicle:
    def __init__(self, pos, xSize, ySize, motor1=None, motor2=None, color=(0, 255, 0)):
        self.pos = pos
        self.xSize = xSize
        self.ySize = ySize
        self.angle = 0
        self.motor1 = motor1
        self.motor2 = motor2
        self.color = color

    def tirePos(self, tireMult=0.75):
        tire1 = self.definePos(0, tireMult)
        tire2 = self.definePos(1, tireMult)

        return (tire1, tire2)

    def draw(self, img):
        cv2.line(img, self.definePos(0, 0), self.definePos(1, 0) ,self.color, 2)

        cv2.line(img, self.definePos(0, 0), self.definePos(0, 1) ,self.color, 2)

        cv2.line(img, self.definePos(1, 0), self.definePos(1, 1), self.color, 2)

        cv2.line(img, self.definePos(0, 1), self.definePos(1, 1) ,self.color, 2)

    def definePos(self, xMargin, yMargin):
        cp = self.pos
        xSize = self.xSize
        ySize = self.ySize
        angle = self.angle
        pos = (round(cp[0]+xSize*math.sin(angle)*xMargin
                    -ySize*math.cos(angle)*yMargin),
               round(cp[1]+xSize*math.cos(angle)*xMargin
                    +ySize*math.sin(angle)*yMargin))

        return pos
