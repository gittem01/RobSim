import cv2
import numpy as np
import math

def rotateArround(p1, p2, angle):
    pass

class Veichle:
    def __init__(self, pos, xSize, ySize):
        self.pos = pos
        self.xSize = xSize
        self.ySize = ySize
        self.angle = math.pi/2

    def connect(self, thing):
        pass

    def draw(self, img):
        cv2.rectangle(img, self.pos, (self.pos[0]+self.xSize, self.pos[1]+self.ySize),
        (255, 255, 255))
