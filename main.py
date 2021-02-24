# added for emulation
from lib.picodisplay import PicoDisplay
from lib.utime import MicroTime
utime = MicroTime()
picodisplay = PicoDisplay()
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

# game start

game = Game()
board = Board(game, picodisplay)
last_frame_time = 0

while True:
    current_time = utime.ticks_ms()
    delta_time = current_time - last_frame_time
    print('Loop: ' + str(delta_time) + 'ms')
    last_frame_time = current_time
    game.run(delta_time)
    game_time = utime.ticks_ms()
    print('Game: ' + str(game_time - current_time) + 'ms')
    board.draw()
    picodisplay.update()
    print('Draw: ' + str(utime.ticks_ms() - game_time) + 'ms')
    if picodisplay.is_pressed(picodisplay.BUTTON_X):
        game.move_left()
    if picodisplay.is_pressed(picodisplay.BUTTON_Y):
        game.move_right()
    if picodisplay.is_pressed(picodisplay.BUTTON_A):
        game.reset()
    if picodisplay.is_pressed(picodisplay.BUTTON_B):
        game.rotate()

# added for emulation
picodisplay.keep_running()