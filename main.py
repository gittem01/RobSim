from src.motor import *
from src.veichle import *
from src.sensor import *
import random


v = Veichle([300, 150], 50, 75)
motora = Motor()
v.motor1 = motora
motorb = Motor()
v.motor2 = motorb

while 1:
    print(random.random())
    img = np.zeros((500, 800, 3), np.uint8)
    key = cv2.waitKey(1)
    tires = v.tirePos()
    if key == ord("q"):
        break
    if key == ord("d"):
        rotateArround(tires[1], v.pos, +0.1)
        v.angle -= 0.1
    if key == ord("a"):
        rotateArround(tires[0], v.pos, -0.1)
        v.angle += 0.1
    if key == ord("w"):
        rotateArround(tires[0], v.pos, -0.1)
        v.angle += 0.1
        rotateArround(tires[1], v.pos, +0.1)
        v.angle -= 0.1


    v.tirePos(img)
    #motorx.move(0.5)
    v.draw(img)
    cv2.imshow("Sim", img)
