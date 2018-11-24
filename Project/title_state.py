import game_framework
import main_state
from pico2d import *

import game_world
from Blocks import Blocks
import Openingboy

name = "TitleState"

BackgroundImage = None
BGM = None
by = None

map = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0],
       [0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
       [0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
       [0,0,0,0,0,1,0,0,0,3,3,3,0,0,1,0,0,0,0,0],
       [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

class Stage0_Bgm:
    def __init__(self):
        self.bgm = load_music("1City.mp3")
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

def enter():
    global BackgroundImage,BGM,by
    BackgroundImage = load_image("Opening\\3rd.png")

    by = Openingboy.Boy()
    game_world.add_object(by, 2)
    MakeMap()
    if BGM is None:
        BGM = Stage0_Bgm()
    else:
        BGM.bgm.repeat_play()

def exit():
    global BackgroundImage,by
    del BackgroundImage
    del by
    game_world.remove_object_by_line(1)
    game_world.remove_object_by_line(2)

def MakeMap():
    for yLine in range(0, 12):
        for xLine in range(0, 20):
            tile = Blocks(xLine * 50 + 25, 600 - (yLine+1) * 50 + 25, map[yLine][xLine])
            game_world.add_object(tile, 1)

def handle_events():
    global startSelect, endSelect, by
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                by.handle_event(event)



def draw():
    global startSelect
    global endSelect
    clear_canvas()
    BackgroundImage.draw(500, 300)
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()


def update():
    global by
    for game_object in game_world.all_objects():
        game_object.update()
    if by.playerOnX == 10 and by.playerOnY == 6:
        game_framework.change_state(main_state)
    pass


def pause():
    pass


def resume():
    pass






