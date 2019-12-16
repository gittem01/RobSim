def control(key, v):
    if key == ord("d"):
        v.motor1.set(v.motor1.speed+0.002)
        v.motor2.set(v.motor2.speed-0.002)
    if key == ord("a"):
        v.motor1.set(v.motor1.speed-0.002)
        v.motor2.set(v.motor2.speed+0.002)
    if key == ord("w"):
        v.motor1.set(v.motor1.speed+0.002)
        v.motor2.set(v.motor2.speed+0.002)
    if key == ord("s"):
        v.motor1.set(v.motor1.speed-0.002)
        v.motor2.set(v.motor2.speed-0.002)
