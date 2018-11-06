import game_framework
import title_state
import math
from pico2d import *


name = "StartState"
image = None
white = None
logo_time = 0.0


def enter():
    global  image,white
    image = load_image('logo.png')
    white = load_image('white.png')


def exit():
    global image
    del(image)


def update():
    global logo_time

    if logo_time > 2.0:
        logo_time = 0
        #game_framework.quit()
        game_framework.change_state(title_state)

    delay(0.01)
    logo_time += 0.01


def draw():
    global image, logo_time
    clear_canvas()
    white.draw(500,300)
    image.opacify(math.sin(logo_time * 3.14 / 2))
    image.draw(500,300)
    update_canvas()




def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            game_framework.change_state(title_state)


def pause(): pass


def resume(): pass




