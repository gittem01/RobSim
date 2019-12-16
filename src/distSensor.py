import cv2
import math

class distSensor:
    def __init__(self, connection, size=1, angle=math.pi/2):
        self.connection = connection
        self.maxDist = 50
        self.angle = angle # That is constant if you want you can use it as a radar :)
        self.xMargin = 0.1
        self.yMargin = 0.5
    def value(self, img):
        pass # Value return
             # Details are not certain yet
             # How it works, algorithm etc
    def draw(self, img):
        cp = self.connection.pos
        totalAngle = self.angle + self.connection.angle
        self.pos = (round(cp[0]+self.connection.xSize*math.sin(self.connection.angle)*self.xMargin
                    -self.connection.ySize*math.cos(self.connection.angle)*self.yMargin),
                    round(cp[1]+self.connection.xSize*math.cos(self.connection.angle)*self.xMargin
                    +self.connection.ySize*math.sin(self.connection.angle)*self.yMargin))
        cv2.circle(img, self.pos, 10, (255, 255, 0), 3)
        cv2.line(img, self.pos, (round(self.pos[0]+self.maxDist*math.cos(totalAngle)),
                                 round(self.pos[1]-self.maxDist*math.sin(totalAngle))),
                                 (0, 0, 255))
