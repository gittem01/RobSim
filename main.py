from src.motor import *
from src.veichle import *
from src.bwSensor import *
from src.distSensor import *
from src.candle import *
from src.heatSensor import *
from src.keyControls import control
import random
import time

windowName = "Sim"
mults = [-4, -3, -2, -1, 1, 2, 3, 4]

WIDTH = 800
HEIGHT = 500

baseSpeed = 0.005

baseImg = np.zeros((HEIGHT, WIDTH, 3), np.uint16)
gridList = np.moveaxis(np.mgrid[:HEIGHT,:WIDTH], 0, -1)

v = Veichle([300, 150], 75, 120)
sensors = [bwsensor(v, i, 2) for i in range(1, 9)]

motora = Motor(1)
v.motor1 = motora
v.motor1.connection=v

motorb = Motor(2)
v.motor2 = motorb
v.motor2.connection=v

v.motor1.set(0)
v.motor2.set(0)

dSensor = distSensor(v)

hSensor = heatSensor(v, 0.8)

c = Candle((100, 100))
c.makeGridMap(baseImg, gridList)

lineList = []
wallList = []
def event_func(event, x, y, flags, param):
    global lineList
    global wallList
    if event == cv2.EVENT_LBUTTONDOWN:
        lineList.append((x, y))
        if len(lineList) == 2:
            cv2.line(baseImg, lineList[0], lineList[1], (255, 255, 255), 3)
            lineList = [lineList[1]]
    elif event == cv2.EVENT_MBUTTONDOWN:
        wallList.append((x, y))
        if len(wallList) == 2:
            cv2.line(baseImg, wallList[0], wallList[1], (255, 0, 0), 3)
            wallList = [wallList[1]]
    elif event == cv2.EVENT_RBUTTONDOWN:
        c = Candle((x, y))
        c.makeGridMap(baseImg, gridList)

cv2.namedWindow(windowName)
cv2.setMouseCallback(windowName, event_func)

startTracing = False
while 1:
    img = baseImg.copy()
    key = cv2.waitKey(1)
    print(hSensor.value(img))
    sensorValues = []
    for sensor in sensors:
        sensorValues.append(sensor.value(img))

    distance1 = dSensor.value(img)
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
        baseImg = np.zeros((HEIGHT, WIDTH, 3), np.uint16)# Clears screen
        lineList = []
        wallList = []

    v.motor1.move()
    v.motor2.move()

    for sensor in sensors: # For loops seperated because sensors were interfiering each other at high speeds
        sensor.draw(img)
    v.motor1.draw(img, v)
    v.motor2.draw(img, v)
    v.draw(img)
    dSensor.draw(img)
    hSensor.draw(img)
    cv2.imshow(windowName, np.array(img, dtype=np.uint8))
