from src.motor import *
from src.veichle import *
from src.sensor import *
import random


v = Veichle([300, 150], 50, 100)
motorx = Motor()
motorx.connection = v

while 1:
    print(random.random())
    img = np.zeros((500, 800, 3), np.uint8)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    if key == ord("d"):
        v.angle += 0.1

    v.tirePos(img)
    #motorx.move(0.5)
    v.draw(img)
    cv2.imshow("Sim", img)
