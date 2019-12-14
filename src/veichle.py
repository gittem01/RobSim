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

    p2[0] = xnew + p1[0]
    p2[1] = ynew + p1[1]

class Veichle:
    def __init__(self, pos, xSize, ySize, motor1=None, motor2=None):
        self.pos = pos
        self.xSize = xSize
        self.ySize = ySize
        self.angle = 0
        self.motor1 = motor1
        self.motor2 = motor2
        self.sensors = []

    def tirePos(self, img=None):
        tireMult = 0.75
        tire1 = (round(self.pos[0]-self.ySize*math.cos(self.angle)*tireMult),
                 round(self.pos[1]+self.ySize*math.sin(self.angle)*tireMult))
        tire2 = (round(self.pos[0]-self.ySize*math.cos(self.angle)*tireMult+self.xSize*math.sin(self.angle)),
                 round(self.pos[1]+self.ySize*math.sin(self.angle)*tireMult+self.xSize*math.cos(self.angle)))

        if img is not None:
            cv2.circle(img, tire1, 10, (255, 255, 255))
            cv2.circle(img, tire2, 10, (255, 255, 255))
        return (tire1, tire2)

    def draw(self, img):
        cv2.line(img, (round(self.pos[0]), round(self.pos[1])),
                      (round(self.pos[0]+self.xSize*math.sin(self.angle)),
                       round(self.pos[1]+self.xSize*math.cos(self.angle)))
                       ,(255, 0, 0))
        cv2.line(img, (round(self.pos[0]), round(self.pos[1])),
                      (round(self.pos[0]-self.ySize*math.cos(self.angle)),
                       round(self.pos[1]+self.ySize*math.sin(self.angle)))
                       ,(255, 0, 0))
        cv2.line(img, (round(self.pos[0]+self.xSize*math.sin(self.angle)),
                       round(self.pos[1]+self.xSize*math.cos(self.angle))),
                      (round(self.pos[0]+self.xSize*math.sin(self.angle)-self.ySize*math.cos(self.angle)),
                       round(self.pos[1]+self.xSize*math.cos(self.angle)+self.ySize*math.sin(self.angle)))
                       ,(255, 0, 0))
        cv2.line(img, (round(self.pos[0]-self.ySize*math.cos(self.angle)),
                       round(self.pos[1]+self.ySize*math.sin(self.angle))),
                      (round(self.pos[0]-self.ySize*math.cos(self.angle)+self.xSize*math.sin(self.angle)),
                       round(self.pos[1]+self.ySize*math.sin(self.angle)+self.xSize*math.cos(self.angle)))
                       ,(255, 0, 0))
