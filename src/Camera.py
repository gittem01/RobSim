from math import sin
from math import cos
from math import pi
import numpy as np
import cv2

class Camera:
    def __init__(self, connection, sim, viewSize, height=50, pos=np.array([0, 0, 0], np.float64),
                angle=np.array([1, 0, 0], np.float64), e=np.array([0, 0, -300], np.float64)):
        self.connection = connection
        self.sim = sim
        self.viewSize = viewSize
        self.height = height
        self.pos = pos
        self.angle = angle
        self.e = e
        self.array1 = np.array([[1, 0, 0],
                           [0, cos(self.angle[0]), sin(self.angle[0])],
                           [0, -sin(self.angle[0]), cos(self.angle[0])]])

        self.array2  = np.array([[cos(self.angle[1]), 0, -sin(self.angle[1])],
                           [0, 1, 0],
                           [sin(self.angle[1]), 0, cos(self.angle[1])]])

        self.array3 = np.array([[cos(self.angle[2]), sin(self.angle[2]), 0],
                           [-sin(self.angle[2]), cos(self.angle[2]), 0],
                           [0, 0, 1]])
        self.xMargin = 0.5
        self.yMargin = 0.2
        self.img = np.zeros((self.viewSize))
        self.name = "Camera"
        self.seenDots = []

    def update(self):
        p = self.connection.definePos(self.xMargin, self.yMargin)
        self.seenDots = []
        self.img = np.zeros((self.viewSize))
        self.pos = np.array([p[0], self.height, p[1]], np.float64)
        self.angle[1] = self.connection.angle+pi/2
        self.array1 = np.array([[1, 0, 0],
                           [0, cos(self.angle[0]), sin(self.angle[0])],
                           [0, -sin(self.angle[0]), cos(self.angle[0])]])

        self.array2  = np.array([[cos(self.angle[1]), 0, -sin(self.angle[1])],
                           [0, 1, 0],
                           [sin(self.angle[1]), 0, cos(self.angle[1])]])

        self.array3 = np.array([[cos(self.angle[2]), sin(self.angle[2]), 0],
                           [-sin(self.angle[2]), cos(self.angle[2]), 0],
                           [0, 0, 1]])

    def draw(self, img):
        self.update()
        self.img = np.zeros((self.viewSize))
        linePoints = self.sim.lineDots
        for points in linePoints:
            self.seenDots.append([])
            for point in points:
                b = self.put(point)
                if type(b) == type(None) or np.isnan(b[0]) or np.isnan(b[1]) or np.isinf(b[0]) or np.isinf(b[1]):
                    continue
                b[0] += int(self.viewSize[1]/2)
                b[1] += (self.viewSize[0]/2)
                self.seenDots[-1].append(b)
                """
                if b[0]<self.viewSize[1] and b[0]>=0 and b[1]<self.viewSize[0] and b[1]>=0:
                    self.img[int(b[1]), int(b[0])] = 1 # if dots are necessary
                """
        for line in self.seenDots:
            if len(line) < 2:
                continue
            for i in range(len(line)-1):
                try:
                    cv2.line(self.img, (int(line[i][0]), int(line[i][1])),
                                       (int(line[i+1][0]), int(line[i+1][1])), 1, 2)
                except:
                    continue

        cv2.circle(img, (int(self.pos[0]), int(self.pos[2])), 5, (0, 255, 255), 2)

        cv2.line(img, (int(self.pos[0]), int(self.pos[2])),
                                (int(self.pos[0]+50*cos(self.angle[1]-pi/4)),
                                 int(self.pos[2]-50*sin(self.angle[1]-pi/4))),
                                 (0, 0, 255))
        cv2.line(img, (int(self.pos[0]), int(self.pos[2])),
                                (int(self.pos[0]+50*cos(self.angle[1]-3*pi/4)),
                                 int(self.pos[2]-50*sin(self.angle[1]-3*pi/4))),
                                 (0, 0, 255))
        cv2.imshow(self.name, self.img)
        
    def put(self, point):

        array4 = point-self.pos
        result = np.dot(self.array1, self.array2)
        result = np.dot(result, self.array3)
        result = np.dot(result, array4)
        if result[2] < 0:
            return None
        b = np.array([0, 0], dtype=np.float64)
        b[0] = (self.e[2]/result[2])*result[0] + self.e[0]
        b[1] = (self.e[2]/result[2])*result[1] + self.e[1]
        return b
