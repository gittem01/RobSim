import math
from .veichle import *

class Motor:
    def __init__(self, num):
        self.connection = None
        self.num = num
        self.dict = {1: 2, 2: 1}
        self.speed = 0
        self.posMult = 0.75
        self.maxSpeed = 0.01
    def move(self):
        #Just move and make rotation things
        otherMotor = self.connection.tirePos()[self.dict[self.num]-1]
        if self.num == 1:
            rotateArround(otherMotor, self.connection.pos, +self.speed)
            self.connection.angle -= self.speed
        else:
            rotateArround(otherMotor, self.connection.pos, -self.speed)
            self.connection.angle += self.speed
    def set(self, speed):
        if speed > self.maxSpeed:
            self.speed = self.maxSpeed
        elif speed < -self.maxSpeed:
            self.speed = -self.maxSpeed
        else:
            self.speed = speed
    def draw(self, img, v=None):
        tire1, tire2 = v.tirePos(self.posMult)
        cv2.circle(img, tire1, 10, (255, 0, 0)) # (imageToDraw, locationOfCircle, radiusOfCircle, ThicknessOfCircle)
        cv2.circle(img, tire2, 10, (255, 0, 0))
