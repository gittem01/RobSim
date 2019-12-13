import cv2
import numpy as np
import math

def rotateArround(p1, p2, angle):
    s = math.sin(angle)
    c = math.cos(angle)

    p2[0] -= p1[0]
    p2[1] -= p1[1]

    xnew = p2[0] * c - p2[1] * s
    ynew = p2[0] * s + p2[1] * c

    p2[0] = int(xnew + p1[0])
    p2[1] = int(ynew + p1[1])


class Veichle:
    def __init__(self, pos, xSize, ySize, motor1=None, motor2=None):
        self.pos = pos
        self.xSize = xSize
        self.ySize = ySize
        self.angle = math.pi/2
        self.motor1 = motor1
        self.motor2 = motor2
        self.sensors = []

    def draw(self, img):
        print(self.pos)
        cv2.rectangle(img, tuple(self.pos), (self.pos[0]+self.xSize, self.pos[1]+self.ySize), (255, 255, 255))
