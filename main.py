from lib.picodisplay import PicoDisplay
from lib.utime import MicroTime
utime = MicroTime()
picodisplay = PicoDisplay()
# added for emulation ↑↑↑↑↑↑↑↑↑↑

# import picodisplay
# import utime

from view import Colors, Square, Board
from random import randrange
from model import Game

width = picodisplay.get_width()
height = picodisplay.get_height()

display_buffer = bytearray(width * height * 2)  # 2-bytes per pixel (RGB565)
picodisplay.init(display_buffer)
picodisplay.set_backlight(1.0)

picodisplay.set_pen(0, 0, 0)
picodisplay.clear()

game = Game(width=20, height=10)
board = Board(
        game, picodisplay, square_size=10, 
        x=33, y=2, width=200, height=100, draw_frame=True, draw_grid=False, 
        next_x=33, next_y=106, next_width=40, next_height=40, draw_next_frame=False)
last_frame_time = 0

try:
    while True:
        current_time = utime.ticks_ms()
        delta_time = current_time - last_frame_time
        last_frame_time = current_time
        game.run(delta_time)
        game_time = utime.ticks_ms()
        if picodisplay.is_pressed(picodisplay.BUTTON_X):
            game.move_left()
        if picodisplay.is_pressed(picodisplay.BUTTON_Y):
            game.move_right()
        if picodisplay.is_pressed(picodisplay.BUTTON_A):
            game.reset()
        if picodisplay.is_pressed(picodisplay.BUTTON_B):
            game.rotate()
        board.draw()
except:
    raise

# added for emulation ↓↓↓↓↓↓↓↓↓↓
picodisplay.keep_running()