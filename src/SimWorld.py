from src.motor import *
from src.Vehicle import *
from src.bwSensor import *
from src.distSensor import *
from src.candle import *
from src.heatSensor import *
from src.keyControls import control
import random
import time

class Sim:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.baseImg = np.zeros((size[1], size[0], 3), np.uint16)
        self.gridList = np.moveaxis(np.mgrid[:size[1],:size[0]], 0, -1)
        self.objects = []
        cv2.namedWindow(name)
        cv2.setMouseCallback(name, self.event_func)

    def event_func(self, event, x, y, flags, param):
        print(x, y)
        if event == cv2.EVENT_LBUTTONDOWN:
            print("424rf")
        if event == cv2.EVENT_LBUTTONUP:
            print("dsnknnj")

    def loop(self):
        img = self.baseImg.copy()
        key = cv2.waitKey(1)
        for obj in self.objects:
            obj.draw(img)

        if key == ord("q"):
            return key
        cv2.imshow(self.name, np.array(img, dtype=np.uint8))
        return key
