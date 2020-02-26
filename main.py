from src.MainImports import *

windowName = "Sim" # Opencv windows name paremeter (it can be named anything)

WIDTH = 800 # Width of the 2d viewing window
HEIGHT = 800 # Height of the 2d viewing window

s = Sim(windowName, [WIDTH, HEIGHT])

v = Vehicle([400, 25], 75, 120) # Position, xSize and ySize of the vehicle

motora = Motor(1, v) # Number of the motor and the vehicle that it is connected to
v.motor1 = motora

motorb = Motor(2, v)
v.motor2 = motorb

c = Camera(v, s, (800, 800))

s.objects.append(v)
s.objects.append(motora)
s.objects.append(motorb)
s.objects.append(c)

addDots(s, 150) # Adds circle road into the simulation
while 1:
    out = s.loop() # loop returns the key that is pressed on
    control(out, v) # Controls vehicles motors with WASD
    motora.move() # Without move command motors does not move even there is a speed given to them
    motorb.move()
    if out == ord("q"):
        break
