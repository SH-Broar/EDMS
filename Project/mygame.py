import game_framework
import pico2d

import main_state
import start_state
import clear_state

pico2d.open_canvas(1000, 600,sync=True)
game_framework.run(start_state)
pico2d.close_canvas()