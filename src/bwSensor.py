import math
import numpy as np

class bwsensor:
    def __init__(self, connection, num, size=1):
        self.size = size
        self.connection = connection
        self.num = num
        self.pos = self.connection.pos
        self.yMargin = 0.075
        self.xMargin = 0.11
    def value(self, img):
        vision = img[round(self.pos[1]-self.size): round(self.pos[1]+self.size),
                     round(self.pos[0]-self.size): round(self.pos[0]+self.size)]

        sum = np.count_nonzero(vision==(255, 255, 255))
        if sum >= (self.size**2)*2:
            return 1
        else:
            return 0

    def draw(self, img):
        cp = self.connection.pos
        self.pos = (round(cp[0]+self.connection.xSize*math.sin(self.connection.angle)*(self.num*self.xMargin)
                    -self.connection.ySize*math.cos(self.connection.angle)*self.yMargin),
                    round(cp[1]+self.connection.xSize*math.cos(self.connection.angle)*(self.num*self.xMargin)
                    +self.connection.ySize*math.sin(self.connection.angle)*self.yMargin))
        img[round(self.pos[1]-self.size): round(self.pos[1]+self.size),
            round(self.pos[0]-self.size): round(self.pos[0]+self.size)] = (0, 0, 255)
