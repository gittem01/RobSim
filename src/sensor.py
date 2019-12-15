class sensor:
    def __init__(self, connection, pos, size=1):
        self.size = size
        self.pos = pos
    def value(self, img):
        return None
    def draw(self):
        pass # Will draw sensors maybe as dots not fully planned yet
