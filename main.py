# added for emulation
from lib.picodisplay import PicoDisplay
picodisplay = PicoDisplay()
# import picodisplay

from view import Colors, Square, Board
from random import randrange
import time
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

while(True):
    board.draw()
    game.moveTime()
    picodisplay.update()
    time.sleep(1)

# added for emulation
picodisplay.keep_running()