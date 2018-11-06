from pico2d import *
import game_framework
import game_world
import math

class shooter:
    image = None

    def __init__(self,type = 0,color = 0, x = 100, y = 100, angle = 0, speed = 1):

        if shooter.image is None:
            shooter.image = load_image('Shooter\\Shooter atl.png')
        self.type = 0       # attending to Y of image
        self.color = 0      # attending to X of image
        self.x = 0
        self.y = 0
        self.angle = 0
        self.speed = 0
        self.type,self.color,self.x,self.y,self.angle,self.speed = type,color,x,y,angle,speed

    def update(self):
        self.x += math.cos(self.angle * 3.14 / 180) * self.speed * game_framework.frame_time
        self.y += math.sin(self.angle * 3.14 / 180) * self.speed * game_framework.frame_time
        if self.x < 0 or self.x > 1000 or self.y < 0 or self.y > 600:
            game_world.remove_object(self)
        pass

    def draw(self):
        self.image.clip_composite_draw(16*self.color,16*(16-self.type),16,16,(self.angle - 90) * 3.14 / 180,'T',self.x,self.y,16,16)

    def get_bb(self):
        return self.x - 8, self.y - 8, self.x + 8, self.y + 8

