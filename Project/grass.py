from pico2d import *
import game_framework

class Grass:
    def __init__(self):
        self.x = 0
        self.image = load_image('Background\\BlueSky.png')

    def update(self):
        self.x += 8 * game_framework.frame_time
        pass

    def draw(self):
        self.image.draw(0 - self.x,300,4000,800)
