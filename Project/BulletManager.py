from pico2d import *
import boy
from shooter import shooter
import main_state
import game_world
import math

stoped = False
inTime = 0
bullets = None

preMx, preMy = 0,0

class BM:
    def __init__(self):
        pass

    @staticmethod
    def clicked(mx,my):
        global stoped, inTime, bullets, preMx,preMy
        preMx = mx
        preMy = my
        stoped = True
        inTime = get_time()
        main_state.BGM.bgm.pause()
        bullets = shooter(2, 1, preMx, preMy, 0, 0, 6)
        game_world.add_object(bullets,3)
        pass

    @staticmethod
    def draged(mx,my):
        global bullets
        game_world.remove_inturrepted_bullet()
        if (mx > preMx):
            bullets = shooter(2, 1, preMx, preMy,
                              math.atan((my - preMy) / (clamp(0.1, mx - preMx, 2100000))) * 180 / 3.14, 0, 6)
        else:
            bullets = shooter(2, 1, preMx, preMy,
                              math.atan((preMy-my) / (clamp(0.1, preMx-mx, 2100000))) * 180 / 3.14 + 180, 0, 6)

        game_world.add_object(bullets, 3)
        pass

    @staticmethod
    def deClicked(mx,my):
        global stoped, inTime
        stoped = False
        main_state.EnterTime += get_time() - inTime
        main_state.BGM.bgm.resume()
        pass