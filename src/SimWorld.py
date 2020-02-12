import cv2
import numpy as np

class Sim:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.baseImg = np.zeros((size[1], size[0], 3), np.uint16)
        self.img = self.baseImg.copy()
        self.gridList = np.moveaxis(np.mgrid[:size[1],:size[0]], 0, -1)
        self.objects = []
        self.isDrawingLine = False
        self.isDrawingWall = False
        self.lineDots = []
        self.wallDots = []
        cv2.namedWindow(name)
        cv2.setMouseCallback(name, self.event_func)

    def loop(self):
        self.img = self.baseImg.copy()
        key = cv2.waitKey(1)
        for obj in self.objects:
            obj.draw(self.img)

        if key == ord("c"):
            self.baseImg = np.zeros((self.size[1], self.size[0], 3), np.uint16)
            self.lineDots = []
            self.wallDots = []
        cv2.imshow(self.name, np.array(self.img, dtype=np.uint8))
        return key

    def event_func(self, event, x, y, flags, param):

        if self.isDrawingLine:
            self.lineDots[-1].append(np.array([x, 0, y]))
            if len(self.lineDots[-1]) >= 2:
                d2 = self.lineDots[-1][-2]
                cv2.line(self.baseImg, (x, y), (d2[0], d2[2]), (255, 255, 255), 3)

        if event == cv2.EVENT_LBUTTONDOWN:
            self.lineDots.append([])
            self.isDrawingLine = True
        if event == cv2.EVENT_LBUTTONUP:
            self.isDrawingLine = False



        if self.isDrawingWall:
            self.wallDots[-1].append(np.array([x, 0, y]))
            if len(self.wallDots[-1]) >= 2:
                d2 = self.wallDots[-1][-2]
                cv2.line(self.baseImg, (x, y), (d2[0], d2[2]), (255, 0, 0), 3)

        if event == cv2.EVENT_RBUTTONDOWN:
            self.wallDots.append([])
            self.isDrawingWall = True
        if event == cv2.EVENT_RBUTTONUP:
            self.isDrawingWall = False

        if event == cv2.EVENT_MBUTTONDOWN:
            Candle((x, y)).makeGridMap(self.baseImg, self.gridList)
