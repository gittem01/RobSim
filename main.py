from src.motor import *
from src.Vehicle import *
from src.bwSensor import *
from src.distSensor import *
from src.candle import *
from src.heatSensor import *
from src.keyControls import control
from src.SimWorld import *
import random
import time
import math

windowName = "Sim"

WIDTH = 800
HEIGHT = 500

s = Sim(windowName, [WIDTH, HEIGHT])

v = Vehicle([300, 150], 75, 120)

motora = Motor(1, v)
v.motor1 = motora

motorb = Motor(2, v)
v.motor2 = motorb


s.objects.append(v)
s.objects.append(motora)
s.objects.append(motorb)


while 1:
    out = s.loop()
    control(out, v)
    motora.move()
    motorb.move()
    if out == ord("q"):
        break
