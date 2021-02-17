# added for emulation
from lib.picodisplay import PicoDisplay
picodisplay = PicoDisplay()
# import picodisplay

from view import Colors, Square
from random import randrange

width = picodisplay.get_width()
height = picodisplay.get_height()

display_buffer = bytearray(width * height * 2)  # 2-bytes per pixel (RGB565)
picodisplay.init(display_buffer)
picodisplay.set_backlight(1.0)

picodisplay.set_pen(0, 0, 0)    
picodisplay.clear()

# game start

colors = Colors(picodisplay)
c = [
    colors.green,
    colors.blue,
    colors.yellow,
    colors.magenta,
    colors.fuscia,
    colors.red,
    colors.grey,
    colors.black,
    colors.white,
    colors.blank
]

i = 0
for x in [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220]:
    for y in [0,10,20,30,40,50,60,70,80,90,100,110,120]:
        square = Square(picodisplay, x, y, c[i])
        square.draw()
    i = 0 if i == 6 else i + 1

picodisplay.update()

# added for emulation
picodisplay.keep_running()