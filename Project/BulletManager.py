from pico2d import *
import boy
from shooter import shooter
import main_state
import game_world
import math

stoped = False
inTime = 0
bullets = None
Hold = False

preMx, preMy = 0,0
income = 0

tmpList = [[],[],[],[],[],[],[],[]]
saveString = ''

def angle(mx,my):
    global preMx,preMy
    return math.atan((my - preMy) / (clamp(0.1, mx - preMx, 2100000))) * 180 / 3.14

def R_angle(mx,my):
    global preMx, preMy
    return math.atan((preMy - my) / (clamp(0.1, preMx - mx, 2100000))) * 180 / 3.14 + 180

def speed(mx,my):
    global preMx, preMy
    return math.sqrt(pow(preMx-mx,2)+pow(preMy-my,2)) / 10

def change(maxIndex, num):
    global tmpList
    for i in range(8):
        tmpList[i][maxIndex],tmpList[i][num] = tmpList[i][num],tmpList[i][maxIndex]

def BulletListSorting():
    global tmpList
    num = len(tmpList[7]) - 1
    for k in range(len(tmpList[7])):
        max = -1
        maxIndex = 0
        for i in range(num+1):
            if max < tmpList[7][i]:
                max = tmpList[7][i]
                maxIndex = i
        change(maxIndex, num)
        num -= 1
    pass

def saveBulletList():
    global tmpList, saveString

    BulletListSorting()
    output = open("shooter\\save.txt",'w')

    for i in range(len(tmpList[0])):
        saveString = str(tmpList[0][i]) +" "+ str(tmpList[1][i]) +" "+ str(tmpList[2][i]) +" "+ str(tmpList[3][i]) +" "+ str(tmpList[4][i]) +" "+ str(tmpList[5][i]) +" "+ str(tmpList[6][i]) +" "+ str(tmpList[7][i])
        output.write(saveString)
        output.write('\n')
    output.close()
    pass

class BM:
    def __init__(self):
        pass

    @staticmethod
    def clicked(mx,my):
        global stoped, inTime, bullets, preMx,preMy
        preMx = mx
        preMy = my
        if (Hold == False):
            stoped = True
            inTime = get_time() - main_state.EnterTime
            print(get_time(),main_state.EnterTime,inTime)
            main_state.BGM.bgm.pause()
        bullets = shooter(2, 1, preMx, preMy, 0, 0, 6)
        game_world.add_object(bullets,3)
        pass

    @staticmethod
    def draged(mx,my):
        global bullets,preMx,preMy
        game_world.remove_inturrepted_bullet()
        if (mx > preMx):
            bullets = shooter(2, 1, preMx, preMy,angle(mx,my), speed(mx,my), 6)
        else:
            bullets = shooter(2, 1, preMx, preMy,R_angle(mx, my), speed(mx, my), 6)
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
    def fileDecoder():
        global tmpList
        if tmpList == [[],[],[],[],[],[],[],[]]:
            input = open("shooter\\bullet.txt", "rt")
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
                    if i == 7:
                        tmpList[i].append(float(text))
                    else:
                        tmpList[i].append(int(text))
                    i = i + 1
                    i %= 8

    @staticmethod
    def deClicked(mx,my):
        global stoped, inTime,income, tmpList, preMx,preMy, Hold
        if income == 0:
            income = 1
        BM.fileDecoder()

        if (Hold is False):
            main_state.EnterTime = (get_time() - inTime)

        for i in range(0,income):
            if (mx > preMx):
                bullets = shooter(2, 1, preMx, preMy,
                                  angle(mx, my) + (360/income)*i, speed(mx, my), 0)
                if (i == 0):
                    tmpList[0].append(2)
                    tmpList[1].append(1)
                    tmpList[2].append(preMx)
                    tmpList[3].append(preMy)
                    tmpList[4].append(int(angle(mx,my) + (360/income)*i))
                    tmpList[5].append(int(speed(mx,my)))
                    tmpList[6].append(income)
                    tmpList[7].append(inTime)
            else:
                bullets = shooter(2, 1, preMx, preMy, R_angle(mx, my) + (360/income)*i, speed(mx, my), 0)
                if (i == 0):
                    tmpList[0].append(2)
                    tmpList[1].append(1)
                    tmpList[2].append(preMx)
                    tmpList[3].append(preMy)
                    tmpList[4].append(int(R_angle(mx, my) + (360/income)*i))
                    tmpList[5].append(int(speed(mx, my)))
                    tmpList[6].append(income)
                    tmpList[7].append(inTime)
            game_world.add_object(bullets,3)
        if (Hold == False):
            stoped = False
            main_state.BGM.bgm.resume()
        pass
