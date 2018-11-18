
# layer 0: Background Objects
# layer 1: tiles
# layer 2: Player
# layer 3: bullets
objects = [[],[],[],[],[]]


def add_object(o, layer):
    objects[layer].append(o)


def remove_object(o):
    for i in range(len(objects)):
        if o in objects[i]:
            objects[i].remove(o)
            del o
            break

def remove_object_by_line(num):
    for i in objects[num][::-1]:
        objects[num].remove(i)
        del i

def remove_inturrepted_bullet():
    i = objects[3][-1]
    objects[3].remove(i)
    del i

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

def object_in_line(num):
    for i in objects[num]:
        yield i

def clear():
    global objects
    for o in all_objects():
        del o
    objects.clear()
    objects = [[],[],[],[],[]]


def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o

