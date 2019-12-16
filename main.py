from src.motor import *
from src.veichle import *
from src.bwSensor import *
from src.distSensor import *
from src.keyControls import control
import random
import time

windowName = "Sim"
mults = [-4, -3, -2, -1, 1, 2, 3, 4]

WIDTH = 800
HEIGHT = 500

baseSpeed = 0.005

baseImg = np.zeros((HEIGHT, WIDTH, 3), np.uint8)

v = Veichle([300, 150], 75, 120)
sensors = [bwsensor(v, i, 1) for i in range(1, 9)]

motora = Motor(1)
v.motor1 = motora
v.motor1.connection=v

motorb = Motor(2)
v.motor2 = motorb
v.motor2.connection=v

v.motor1.set(0)
v.motor2.set(0)

d = distSensor(v)

lineList = []
def event_func(event, x, y, flags, param):
    global lineList
    if event == cv2.EVENT_LBUTTONDOWN:
        lineList.append((x, y))
        if len(lineList) == 2:
            cv2.line(baseImg, lineList[0], lineList[1], (255, 255, 255), 2)
            lineList = [lineList[1]]

cv2.namedWindow(windowName)
cv2.setMouseCallback(windowName, event_func)

startTracing = False
while 1:
    img = baseImg.copy()
    key = cv2.waitKey(1)
    sensorValues = []
    for sensor in sensors:
        sensorValues.append(sensor.value(img))
    #print(str(sensorValues), end = "\r") # Sensor values can be seen for debuging

    if startTracing:
        sum = 0
        for i in range(len(mults)):
            sum += mults[i] * sensorValues[i]
        v.motor1.set(sum/(400)+baseSpeed)
        v.motor2.set(-sum/(400)+baseSpeed)

    control(key, v)
    if key == ord("q"):
        break
    if key == ord("z"):
        startTracing = not startTracing
        v.motor1.set(0)
        v.motor2.set(0)
    if key == ord("c"):
        baseImg = np.zeros((HEIGHT, WIDTH, 3), np.uint8)# Clears screen
        lineList = []

    v.motor1.move()
    v.motor2.move()

    for sensor in sensors: # For loops seperated because sensors were interfiering each other at high speeds
        sensor.draw(img)
    v.motor1.draw(img, v)
    v.motor2.draw(img, v)
    v.draw(img)
    d.draw(img)
    cv2.imshow(windowName, img)
