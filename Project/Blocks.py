from pico2d import *
import game_world

class Blocks:
    b1 = None
    b2 = None
    b3 = None
    def __init__(self, x = 400, y = 300, style = 0):
        if Blocks.b1 == None and style == 1:
            Blocks.b1 = load_image('tile\\1.png')
        if Blocks.b2 == None and style == 2:
            Blocks.b2 = load_image('tile\\2.png')
        if Blocks.b3 == None and style == 3:
            Blocks.b3 = load_image('tile\\3.png')
        self.x, self.y, self.style = x, y, style

    def draw(self):
        if self.style == 1:
            self.b1.draw(self.x, self.y)
        elif self.style == 2:
            self.b2.draw(self.x, self.y)
        elif self.style == 3:
            self.b3.draw(self.x, self.y)

    def update(self):
        pass

    def deadCall(self):
        game_world.remove_object(self)