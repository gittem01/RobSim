import math

class Motor:
    def __init__(self, dist=0):
        self.dist = dist # Dist from top part of the robot
        self.connection = None
        self.num = 1
        self.dict = {1: 2, 2: 1}
        self.speed = 1
    def move(self, speed=1):
        #Just move and make rotation things
        otherMotor = eval(f"self.connection.motor{self.dict[self.num]}")
        self.connection.pos[0] += math.cos(self.connection.angle)*self.speed*speed
        self.connection.pos[1] -= math.sin(self.connection.angle)*self.speed*speed

    def draw(self):
        pass # Will draw only this motor
