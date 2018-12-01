import game_framework
import title_state
import math
from pico2d import *


name = "StartState"
image = None
white = None

image2 = None
image3 = None

BGM = None
logo_time = -1

class Stage_1_Bgm:
    def __init__(self):
        self.bgm = load_music("FX.mp3")
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

def enter():
    global  image,white,image2,image3, BGM
    image = load_image('logo.png')
    white = load_image('white.png')
    image2 = load_image('Opening\\1st.png')
    image3 = load_image('Opening\\2nd.png')
    if BGM is None:
        BGM = Stage_1_Bgm()
    else:
        BGM.bgm.play()

def exit():
    global image
    del(image)


def update():
    global logo_time, BGM

    if logo_time > 3.0:
        if BGM:
            BGM = None
    if logo_time > 11.0:
        logo_time = 0
        #game_framework.quit()
        game_framework.change_state(title_state)

    delay(0.01)
    logo_time += 0.01


def draw():
    global image, logo_time, image2,image3
    clear_canvas()
    white.draw(500,300)

    if (logo_time < 3.0):
        image.opacify(clamp(0,math.sin(logo_time * 3.14 / 2)*1.5,1))
        image.draw(500,300)
    elif(logo_time < 7.0):
        image2.opacify(clamp(0, math.sin((logo_time-3) * 3.14 / 3)*3, 1))
        image2.draw(500, 300)
    elif (logo_time < 11.0):
        image3.opacify(clamp(0, math.sin((logo_time - 7) * 3.14 / 3)*3, 1))
        image3.draw(500, 300)
    update_canvas()




def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            game_framework.change_state(title_state)


def pause(): pass


def resume(): pass




