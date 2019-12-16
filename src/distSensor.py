class distSensor:
    def __init__(self, connection, size=1, angle=0):
        self.connection = connection
        self.size = size
        self.angle = angle # That is constant if you want you can use it as a radar :)

    def value(self, img):
        pass # Value return
             # Details are not certain yet
             # How it works, algorithm etc
    def draw(self):
            # Draw the sensor according to angle and the connections position
             # Each sensor should have !!!unique!!! drawing
             # Connections angle must be included into the self angle
        pass 
