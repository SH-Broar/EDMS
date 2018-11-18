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
income = 0

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
    def numDown(num):
        global income
        if num == SDLK_BACKSPACE:
            income = 0
            return
        income *= 10
        if num == SDLK_0:
            income += 0
        elif num == SDLK_1:
            income += 1
        elif num == SDLK_2:
            income += 2
        elif num == SDLK_3:
            income += 3
        elif num == SDLK_4:
            income += 4
        elif num == SDLK_5:
            income += 5
        elif num == SDLK_6:
            income += 6
        elif num == SDLK_7:
            income += 7
        elif num == SDLK_8:
            income += 8
        elif num == SDLK_9:
            income += 9



    @staticmethod
    def deClicked(mx,my):
        global stoped, inTime,income
        if income == 0:
            income = 1
        for i in range(1,income):
            if (mx > preMx):
                bullets = shooter(2, 1, preMx, preMy,
                                  math.atan((my - preMy) / (clamp(0.1, mx - preMx, 2100000))) * 180 / 3.14 + (360/income)*i, 0, 6)
            else:
                bullets = shooter(2, 1, preMx, preMy,
                                  math.atan((preMy - my) / (clamp(0.1, preMx - mx, 2100000))) * 180 / 3.14 + 180 + (360/income)*i, 0, 6)
            game_world.add_object(bullets,3)
        stoped = False
        main_state.EnterTime += get_time() - inTime
        main_state.BGM.bgm.resume()

        pass