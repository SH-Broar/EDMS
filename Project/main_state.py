import random
import json
import os

from pico2d import *
import game_framework
import game_world

import reset_state

import boy
import BulletManager
from shooter import shooter
from grass import Grass
from Blocks import Blocks

name = "MainState"

by = None
BGM = None
metronom = None

TimeCut = []
gameOverImage = None

bulletDict = [[],[],[],[],[],[],[]]
bulletTime = []
bulletTimeIndex = 0

EnterTime = 0

class Stage1_Bgm:
    def __init__(self):
        self.bgm = load_music("03LegenD.mp3")
        self.bgm.set_volume(64)
        self.bgm.play()

class Metro:
    def __init__(self):
        self.image = load_image('Background\\shin.png')
        self.white = load_image('Background\\shin white.png')
    def update(self):
        global by
        if by.gameOver is False:
            self.image.opacify(clamp(0,((90 - by.jumpHeight) / 112.5 )* (0.01 + by.HP*0.006 ),0.01 + by.HP*0.006))
            self.white.opacify(clamp(0, ((90 - by.jumpHeight) / 112.5)*(0.5 - by.HP*0.005), 0.5 - by.HP*0.005))
        pass

    def draw(self):
        if by.gameOver is False:
            self.white.draw(500, 300)
            self.image.draw(500, 300)

class GameOverImage:
    def __init__(self):
        self.image = load_image('Background\\gameOver.png')

    def update(self):
        pass

    def draw(self):
        if by.gameOver:
            self.image.draw(500, 300)

def enter():
    global by, BGM, metronom, EnterTime, gameOverImage

    grass = Grass()
    metronom = Metro()
    game_world.add_object(grass, 0)
    game_world.add_object(metronom, 4)
    mapper()
    bulletRegister()
    if BGM is None:
        BGM = Stage1_Bgm()
    else:
        BGM.bgm.repeat_play()
    EnterTime = get_time()
    by = boy.Boy()
    game_world.add_object(by, 2)
    gameOverImage = GameOverImage()
    game_world.add_object(gameOverImage, 4)

def bulletRegister():
    global bulletDict, bulletTime
    input = open("shooter\\bullet.txt","rt")
    A = []
    LineOfFile = 0
    i = 0
    for line in input:
        A.append(line.strip())
        LineOfFile += 1
    input.close()
    for line in range(LineOfFile):
        b = A[line].split()
        for text in b:
            if text == '//':
                pass
            elif i == 7:
                bulletTime.append(float(text))
                i = 0
            else:
                bulletDict[i].append(int(text))
                i = i + 1
    pass


def mapper():
    global TimeCut
    input = open("tile\\map.txt", "rt")
    A = []
    LineOfFile = 0
    for line in input:
        A.append(line.strip())
        LineOfFile += 1
    input.close()
    for line in range(LineOfFile):
        if line % 13 == 0:
            TimeCut.append(float(A[line]))
        else:
            for b in A[line]:
                x = int(b)
                boy.Mapper.append(x)

    TimeCut.append(999) # type Music Length


def MakeMap():
    global TimeCut, EnterTime
    xl = 0
    if get_time() - EnterTime < TimeCut[boy.order]:
        pass
    else:
        boy.order += 1
        # block class make and mapping in here
        # by using order in Mapper, can print block in real time.
        game_world.remove_object_by_line(1)
        for yLine in range(0, 12):
            for xLine in range(0, 20):
                tile = Blocks(xLine * 50 + 25, 600 - (yLine+1) * 50 + 25, boy.Mapper[(boy.order-1)*240 + xl])
                game_world.add_object(tile, 1)
                xl += 1

def SpreadAngle(i):
    return (360/bulletDict[6][bulletTimeIndex]) * i

def SpreadBullet():
    global bulletTimeIndex, bulletTime, bulletDict
    if get_time() - EnterTime < bulletTime[bulletTimeIndex]:
        pass
    else:
        for i in range(bulletDict[6][bulletTimeIndex]):
            bullets = shooter(bulletDict[0][bulletTimeIndex],bulletDict[1][bulletTimeIndex],bulletDict[2][bulletTimeIndex],bulletDict[3][bulletTimeIndex],bulletDict[4][bulletTimeIndex] + SpreadAngle(i),bulletDict[5][bulletTimeIndex])
            game_world.add_object(bullets, 3)
        bulletTimeIndex += 1
    pass

def exit():
    global BGM, bulletDict,bulletTime,bulletTimeIndex
    game_world.clear()
    bulletDict = [[], [], [], [], [], [], []]
    bulletTime = []
    bulletTimeIndex = 0
    boy.order = 0
    BGM = None

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_MOUSEBUTTONDOWN:
            BulletManager.BM.clicked(event.x, 600-event.y)
        elif event.type == SDL_MOUSEBUTTONUP:
            BulletManager.BM.deClicked(event.x, 600-event.y)
        elif event.type == SDL_MOUSEMOTION and BulletManager.stoped:
            BulletManager.BM.draged(event.x, 600-event.y)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LSHIFT:
            BulletManager.Hold = True
        elif event.type == SDL_KEYUP and event.key == SDLK_LSHIFT:
            BulletManager.Hold = False
        elif event.type == SDL_KEYDOWN and (event.key == SDLK_0 or event.key == SDLK_1 or event.key == SDLK_2 or event.key == SDLK_3
                                            or event.key == SDLK_4 or event.key == SDLK_5 or event.key == SDLK_6
                                            or event.key == SDLK_7 or event.key == SDLK_8 or event.key == SDLK_9
                                            or event.key == SDLK_BACKSPACE):
            BulletManager.BM.numDown(event.key)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_s:
            BulletManager.saveBulletList()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_r and by.gameOver:
            game_framework.change_state(reset_state)
        else:
            by.handle_event(event)


def update():
    global by
    if BulletManager.stoped:
        pass
    else:
        MakeMap()
        SpreadBullet()
        for game_object in game_world.all_objects():
            game_object.update()
        for game_object in game_world.object_in_line(3):
            if game_world.collide(game_object,by) == True:
                if (by.gameOver is False):
                    game_world.remove_object(game_object)
                    by.eat()
                    pass



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
