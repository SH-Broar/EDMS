import game_framework
import main_state
from pico2d import *


name = "TitleState"
BackgroundImage = None
START = None
END = None
startSelect = 0
endSelect = 1

def enter():
    global BackgroundImage
    global START
    global END
    BackgroundImage = load_image("UI\\BG.png")
    START = load_image('UI\\start.png')
    END = load_image('UI\\ENDpng.png')

def exit():
    global BackgroundImage
    global START
    global END
    del BackgroundImage
    del(START)
    del(END)


def handle_events():
    global startSelect, endSelect
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)


def draw():
    global startSelect
    global endSelect
    clear_canvas()
    BackgroundImage.draw(800, 400)
    START.clip_draw(startSelect * 129, 0, 129, 25, 800, 300)
    END.clip_draw(0, endSelect * 17, 31, 17, 800, 250, 60, 20)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass






