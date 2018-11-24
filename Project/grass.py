from pico2d import *
import game_framework

class Grass:
    def __init__(self):
        self.x = 0
        self.image = load_image('Background\\Blue.png')

    def update(self):
        self.x += 8 * game_framework.frame_time
        pass

    def draw(self):
        self.image.draw(400 - self.x,300,800,800)
        self.image.draw(1200 - self.x, 300, 800, 800)
        self.image.draw(2000 - self.x, 300, 800, 800)
