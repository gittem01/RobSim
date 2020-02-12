import math
import numpy as np
import cv2

def control(key, v):
    if v.motor1 == None or v.motor2 == None:
        return

    sp = 0.002
    if key == ord("d"):
        v.motor1.set(v.motor1.speed+sp)
        v.motor2.set(v.motor2.speed-sp)
    if key == ord("a"):
        v.motor1.set(v.motor1.speed-sp)
        v.motor2.set(v.motor2.speed+sp)
    if key == ord("w"):
        v.motor1.set(v.motor1.speed+sp)
        v.motor2.set(v.motor2.speed+sp)
    if key == ord("s"):
        v.motor1.set(v.motor1.speed-sp)
        v.motor2.set(v.motor2.speed-sp)

def addDots(sim, dn):
    sim.lineDots.append([])
    for i in range(dn+1):
        i = (math.pi*2*i)/dn
        sim.lineDots[-1].append(np.array([math.sin(i)*400+400, 0, math.cos(i)*400+400]))
        if i>0:
            cv2.line(sim.baseImg, (int(sim.lineDots[-1][-2][0]), int(sim.lineDots[-1][-2][2])),
                              (int(sim.lineDots[-1][-1][0]), int(sim.lineDots[-1][-1][2])), (255, 255, 255), 3)
    sim.lineDots.append([])
    for i in range(dn+1):
        i = (math.pi*2*i)/dn
        sim.lineDots[-1].append(np.array([math.sin(i)*300+400, 0, math.cos(i)*300+400]))
        if i>0:
            cv2.line(sim.baseImg, (int(sim.lineDots[-1][-2][0]), int(sim.lineDots[-1][-2][2])),
                              (int(sim.lineDots[-1][-1][0]), int(sim.lineDots[-1][-1][2])), (255, 255, 255), 3)


def rotateArround(p1, p2, angle):
    s = math.sin(angle)
    c = math.cos(angle)

    p2[0] -= p1[0]
    p2[1] -= p1[1]

    xnew = p2[0] * c - p2[1] * s
    ynew = p2[0] * s + p2[1] * c

    p2[0] = xnew + p1[0]
    p2[1] = ynew + p1[1]
    return p2
