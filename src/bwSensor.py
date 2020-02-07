import math
import numpy as np

class bwSensor:
    def __init__(self, connection, xMargin, yMargin, size=1):
        self.size = size
        self.connection = connection
        self.pos = self.connection.pos
        self.yMargin = xMargin
        self.xMargin = yMargin
    def value(self, img):
        vision = img[round(self.pos[1]-self.size): round(self.pos[1]+self.size),
                     round(self.pos[0]-self.size): round(self.pos[0]+self.size)]
        sum = np.count_nonzero(vision==(255, 255, 255), axis=2)
        sum = np.count_nonzero(sum==3)
        if sum >= ((self.size*2)**2)/2:
            return 1
        else:
            return 0

    def draw(self, img):
        cp = self.connection.pos
        self.pos = self.connection.definePos(self.xMargin, self.yMargin)
        img[round(self.pos[1]-self.size): round(self.pos[1]+self.size),
            round(self.pos[0]-self.size): round(self.pos[0]+self.size)] = (0, 0, 255)
