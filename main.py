from src.motor import *
from src.veichle import *
from src.sensor import *
import random

baseImg = np.zeros((600, 1000))
baseImg[100:150, 100:150] = 1

v = Veichle([300, 150], 50, 100)
sensor1 = sensor(v, 1, 5)
motora = Motor(1)
v.motor1 = motora
v.motor1.connection=v
motorb = Motor(2)
v.motor2 = motorb
v.motor2.connection=v

v.motor1.set(0.01)
v.motor2.set(0.01)

while 1:
    #print(random.random())
    img = baseImg.copy()
    key = cv2.waitKey(1)
    tires = v.tirePos()
    if key == ord("q"):
        break
    if key == ord("d"):
        v.motor2.speed -= 0.001
        v.motor1.speed += 0.001
    if key == ord("a"):
        v.motor2.speed += 0.001
        v.motor1.speed -= 0.001
    if key == ord("w"):
        v.motor1.speed += 0.001
        v.motor2.speed += 0.001
    if key == ord("s"):
        v.motor1.speed -= 0.001
        v.motor2.speed -= 0.001

    v.motor1.move()
    v.motor2.move()

    print(sensor1.value(img))
    sensor1.draw(img)
    v.motor1.draw(img, v)
    v.motor2.draw(img, v)
    v.draw(img)
    cv2.imshow("Sim", img)
