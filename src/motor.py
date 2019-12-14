import math
from .veichle import rotateArround

class Motor:
    def __init__(self, num, dist=0):
        self.dist = dist # Dist from top part of the robot
        self.connection = None
        self.num = num
        self.dict = {1: 2, 2: 1}
        self.speed = 0.01
        self.posMult = 0.75

    def move(self):
        #Just move and make rotation things
        #otherMotor = eval(f"self.connection.motor{self.dict[self.num]}")
        otherMotor = self.connection.tirePos()[self.dict[self.num]-1]
        print(otherMotor)
        rotateArround(otherMotor, self.connection.pos, +self.speed)
        self.connection.angle -= self.speed
    def set(self, speed):
        self.speed = speed
    def draw(self):
        pass # Will draw only this motor
