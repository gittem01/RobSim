class sensor:
    def __init__(self, connection, num, size=1):
        self.size = size
        self.connection = connection
        self.num = num
        self.pos = self.connection.pos
    def value(self, img):
        vision = img[round(self.pos[1]-self.size): round(self.pos[1]+self.size),
                     round(self.pos[0]-self.size): round(self.pos[0]+self.size)]
        sum = vision.sum()
        print(vision)
        if sum >= (self.size**2)*2:
            return 1
        else:
            return 0

    def draw(self, img):
        self.pos = self.connection.pos
        img[round(self.pos[1]-self.size): round(self.pos[1]+self.size),
            round(self.pos[0]-self.size): round(self.pos[0]+self.size)] = 1
