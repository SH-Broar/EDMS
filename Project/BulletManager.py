from pico2d import *
import boy
import shooter
import main_state

stoped = False
inTime = 0

class BM:
    def __init__(self):
        pass

    @staticmethod
    def clicked(mx,my):
        global stoped, inTime
        stoped = True
        inTime = get_time()
        main_state.BGM.bgm.pause()

        pass

    @staticmethod
    def draged(mx,my):
        pass

    @staticmethod
    def deClicked(mx,my):
        global stoped, inTime
        stoped = False
        main_state.EnterTime += get_time() - inTime
        main_state.BGM.bgm.resume()
        pass