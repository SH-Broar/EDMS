import game_framework
import main_state
from pico2d import *

name = "ClearState"

BackgroundImage = None
BGM = None
by = None

class Stage0_Bgm:
    def __init__(self):
        self.bgm = load_music("1City.mp3")
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

def enter():
    global BackgroundImage,BGM,by
    BackgroundImage = load_image("Opening\\4st.png")

    if BGM is None:
        BGM = Stage0_Bgm()
    else:
        BGM.bgm.repeat_play()

def exit():
    pass

def handle_events():
    global startSelect, endSelect, by
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()


def draw():
    global startSelect
    global endSelect
    clear_canvas()
    BackgroundImage.draw(500, 300)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass






