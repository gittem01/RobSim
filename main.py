from src.Motor import *
from src.Vehicle import *
from src.bwSensor import *
from src.distSensor import *
from src.candle import *
from src.heatSensor import *
from src.keyControls import control
from src.SimWorld import *
from src.Camera import *
import random
import time
import math

windowName = "Sim"

WIDTH = 800
HEIGHT = 500

s = Sim(windowName, [WIDTH, HEIGHT])

v = Vehicle([400, 200], 75, 120)

motora = Motor(1, v)
v.motor1 = motora

motorb = Motor(2, v)
v.motor2 = motorb

c = Camera(v, s, (600, 1200))

s.objects.append(v)
s.objects.append(motora)
s.objects.append(motorb)
s.objects.append(c)

while 1:
    out = s.loop()
    control(out, v)
    motora.move()
    motorb.move()
    if out == ord("q"):
        break
