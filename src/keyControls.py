def control(key, v):
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
