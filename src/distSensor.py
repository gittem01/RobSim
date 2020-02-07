import cv2
import math

class distSensor:
    def __init__(self, connection, angle=-math.pi/2):
        self.connection = connection
        self.pos = self.connection.pos
        self.maxDist = 50
        self.dist = self.maxDist
        self.angle = angle # That is constant if you want you can use it as a radar :)
        self.xMargin = 0.9
        self.yMargin = 0.5

    def value(self, img):
        totalAngle = self.angle + self.connection.angle
        for i in range(1, self.maxDist+1):
            pos = (round(self.pos[0]+i*math.cos(totalAngle)),
                   round(self.pos[1]-i*math.sin(totalAngle)))
            if pos[1] >= img.shape[0] or pos[1] < 0 or pos[0] >= img.shape[1] or pos[0] < 0:
                break
            if img[pos[1], pos[0], 0] == 255 and img[pos[1], pos[0], 1] + img[pos[1], pos[0], 2] < 100:
                break
        self.dist = i
        return i

    def draw(self, img):
        cp = self.connection.pos
        totalAngle = self.angle + self.connection.angle
        self.pos = self.connection.definePos(self.xMargin, self.yMargin)
        cv2.circle(img, self.pos, 10, (255, 255, 0), 3)
        cv2.line(img, self.pos, (round(self.pos[0]+self.dist*math.cos(totalAngle)),
                                 round(self.pos[1]-self.dist*math.sin(totalAngle))),
                                 (0, 0, 255))
