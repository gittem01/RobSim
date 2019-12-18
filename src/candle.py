import numpy as np

class Candle:
    def __init__(self, pos):
        self.pos = pos

    def makeGridMap(self, map, lst):
        lstx = lst.copy()
        lstx[:, :, 1] = lstx[:, :, 1] - self.pos[0]
        lstx[:, :, 0] = lstx[:, :, 0] - self.pos[1]
        l3 = np.power(lstx[:, :, 1]**2 + lstx[:, :, 0]**2, 0.5)
        maxx = (lstx.shape[0]**2+lstx.shape[1]**2)**0.5
        l3 = np.round((255*l3)/maxx)

        l3 = 255/(l3+1)
        map[:, :, 2] = (map[:, :, 2] + l3)
        map[map > 255] = 255
