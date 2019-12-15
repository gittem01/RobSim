from src.motor import *
from src.veichle import *
from src.sensor import *
import random

v = Veichle([300, 150], 50, 100)
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
    img = np.zeros((600, 1000, 3), np.uint8)
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

    v.tirePos(img, 0.8)
    v.draw(img)
    cv2.imshow("Sim", img)
