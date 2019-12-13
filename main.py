from src.motor import *
from src.veichle import *
from src.sensor import *

img = np.zeros((500, 800, 3), np.uint8)

v = Veichle((50, 50), 50, 50)


while 1:
    key = cv2.waitKey(0)
    if key == ord("q"):
        break
    v.draw(img)
    cv2.imshow("Sim", img)
