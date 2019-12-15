from src.motor import *
from src.veichle import *
from src.sensor import *
import random
import time

mults = [-4, -3, -2, -1, 1, 2, 3, 4]

baseImg = cv2.imread("untitled.png", 0)/255; 
baseImg.dtype = np.float64

v = Veichle([300, 150], 50, 80)

v.sensors = [sensor(v, i, 2) for i in range(1, 9)]

motora = Motor(1)
v.motor1 = motora
v.motor1.connection=v
motorb = Motor(2)
v.motor2 = motorb
v.motor2.connection=v

v.motor1.set(0)
v.motor2.set(0)

startTracing = False
while 1:
 
    img = baseImg.copy()
    key = cv2.waitKey(1)
    sensorValues = []
    for sensor in v.sensors:
        sensorValues.append(sensor.value(img))
    #print(str(sensorValues), end = "\r")
    if startTracing:
        sum = 0
        for i in range(len(mults)):
            sum += mults[i] * sensorValues[i]
        v.motor1.set(sum/400)
        v.motor2.set(-sum/400)
        v.motor1.speed += 0.01
        v.motor2.speed += 0.01
    if key == ord("q"):
        break
    if key == ord("d"):
        v.motor1.speed += 0.002
        v.motor2.speed -= 0.002
    if key == ord("a"):
        v.motor1.speed -= 0.002
        v.motor2.speed += 0.002
    if key == ord("w"):
        v.motor1.speed += 0.001
        v.motor2.speed += 0.001
    if key == ord("s"):
        v.motor1.speed -= 0.001
        v.motor2.speed -= 0.001
    if key == ord("z"):
        startTracing = not startTracing
        v.motor1.set(0)
        v.motor2.set(0)
    v.motor1.move()
    v.motor2.move()
    
    for sensor in v.sensors: # For loops seperated because sensors were interfiering each other at high speeds
        sensor.draw(img)
    v.motor1.draw(img, v)
    v.motor2.draw(img, v)
    v.draw(img)
    cv2.imshow("Sim", img)
