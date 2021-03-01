from model import Game

class Color:
    _intensityGradient1 = 25
    _intensityGradient2 = _intensityGradient1 * 2
    def __init__(self, display, r, g, b, gradient=True):
        self._display = display
        self.r = r
        self.g = g
        self.b = b
        self.pen = display.create_pen(r, g, b)
        self.penMinus2 = display.create_pen(
            0 if r - Color._intensityGradient2 < 0 else r - Color._intensityGradient2,
            0 if g - Color._intensityGradient2 < 0 else g - Color._intensityGradient2,
            0 if b - Color._intensityGradient2 < 0 else b - Color._intensityGradient2
        ) if gradient else self.pen
        self.penMinus1 = display.create_pen(
            0 if r - Color._intensityGradient1 < 0 else r - Color._intensityGradient1,
            0 if g - Color._intensityGradient1 < 0 else g - Color._intensityGradient1,
            0 if b - Color._intensityGradient1 < 0 else b - Color._intensityGradient1
        ) if gradient else self.pen
        self.penPlus1 = display.create_pen(
            255 if r + Color._intensityGradient1 > 255 else r + Color._intensityGradient1,
            255 if g + Color._intensityGradient1 > 255 else g + Color._intensityGradient1,
            255 if b + Color._intensityGradient1 > 255 else b + Color._intensityGradient1
        ) if gradient else self.pen

    def enable_color(self, intensity=0):
        if intensity < -1:
            self._display.set_pen(self.penMinus2)
        elif intensity == -1:
            self._display.set_pen(self.penMinus1)
        elif intensity == 0:
            self._display.set_pen(self.pen)
        else:
            self._display.set_pen(self.penPlus1)

class Colors:
    def __init__(self, display):
        self.red = Color(display, 200, 0, 0)
        self.green = Color(display, 0, 200, 0)
        self.blue = Color(display, 0, 0, 200)
        self.grey = Color(display, 200, 200, 200)
        self.yellow = Color(display, 200, 200, 0)
        self.fuscia = Color(display, 200, 0, 200)
        self.magenta = Color(display, 0, 200, 200)
        self.black = Color(display, 0, 0, 0)
        self.white = Color(display, 255, 255, 255)
        self.white_fill = Color(display, 255, 255, 255, gradient=False)
        self.black_fill = Color(display, 0, 0, 0, gradient=False)

class Frame:
    size = 10
    def __init__(self, display, x, y, width, height, fg_color, bg_color=None, line_width=1):
        self._display = display
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.line_width = line_width
        self.fg_color = fg_color
        self.bg_color = bg_color

    def draw(self):
        self.fg_color.enable_color()
        self._display.rectangle(self.x, self.y, self.width + 1, self.height + 1)
        if self.bg_color != None:
            self.bg_color.enable_color()
        self._display.rectangle(self.x + 1, self.y + 1, self.width - 1, self.height - 1)

class Grid:
    size = 10
    def __init__(self, display, x, y, width, height, fg_color):
        self._display = display
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fg_color =  fg_color

    def draw(self):
        self.fg_color.enable_color()
        for x in range(self.x, self.width + self.x + 1, self.size):
            for y in range(self.y, self.height + self.y + 1, self.size):
                self._display.pixel(x, y)

class Square:
    size = 10
    def __init__(self, display, x, y, color):
        self._display = display
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        intensities = [-2, -1, 1]
        self.color.enable_color(intensities[0])
        self._display.rectangle(self.x, self.y, Square.size, Square.size)
        self.color.enable_color(intensities[1])
        self._display.rectangle(self.x, self.y + 1, Square.size, Square.size - 1)
        self.color.enable_color(intensities[2])
        self._display.rectangle(self.x + 1, self.y + 1, Square.size - 1, Square.size - 1)
        self.color.enable_color()
        self._display.rectangle(self.x + 1, self.y + 1, Square.size - 2, Square.size - 2)

class Numbers:
    def __init__(self, display, fg_color, bg_color=None):
        self._display = display
        self.fg_color = fg_color
        self.bg_color = bg_color
        self._one_height = 7
        self._others_height = 12
        self._all_width = 19
    def _draw_number(self, number, x, y):
        if number == "1":
            # Line 1
            self._display.pixel(x, y-1)
            self._display.pixel(x, y-2)
            self._display.pixel(x, y-3)
            # Line 2
            self._display.pixel(x+1, y)
            self._display.pixel(x+1, y-1)
            self._display.pixel(x+1, y-2)
            self._display.pixel(x+1, y-3)
            # Line 3
            self._display.pixel(x+2, y)
            self._display.pixel(x+2, y-1)
            self._display.pixel(x+2, y-2)
            self._display.pixel(x+2, y-3)
            # Line 4
            self._display.pixel(x+3, y-1)
            self._display.pixel(x+3, y-2)
            self._display.pixel(x+3, y-3)
            # Line 5
            self._display.pixel(x+4, y-1)
            self._display.pixel(x+4, y-2)
            self._display.pixel(x+4, y-3)
            # Line 6
            self._display.pixel(x+5, y-1)
            self._display.pixel(x+5, y-2)
            self._display.pixel(x+5, y-3)
            # Line 7
            self._display.pixel(x+6, y-1)
            self._display.pixel(x+6, y-2)
            self._display.pixel(x+6, y-3)
            # Line 8
            self._display.pixel(x+7, y-1)
            self._display.pixel(x+7, y-2)
            self._display.pixel(x+7, y-3)
            # Line 9
            self._display.pixel(x+8, y-1)
            self._display.pixel(x+8, y-2)
            self._display.pixel(x+8, y-3)
            # Line 10
            self._display.pixel(x+9, y-1)
            self._display.pixel(x+9, y-2)
            self._display.pixel(x+9, y-3)
            # Line 11
            self._display.pixel(x+10, y-1)
            self._display.pixel(x+10, y-2)
            self._display.pixel(x+10, y-3)
            # Line 12
            self._display.pixel(x+11, y-1)
            self._display.pixel(x+11, y-2)
            self._display.pixel(x+11, y-3)
            # Line 13
            self._display.pixel(x+12, y-1)
            self._display.pixel(x+12, y-2)
            self._display.pixel(x+12, y-3)
            # Line 14
            self._display.pixel(x+13, y-1)
            self._display.pixel(x+13, y-2)
            self._display.pixel(x+13, y-3)
            # Line 15
            self._display.pixel(x+14, y)
            self._display.pixel(x+14, y-1)
            self._display.pixel(x+14, y-2)
            self._display.pixel(x+14, y-3)
            self._display.pixel(x+14, y-4)
            # Line 16
            self._display.pixel(x+15, y)
            self._display.pixel(x+15, y-1)
            self._display.pixel(x+15, y-2)
            self._display.pixel(x+15, y-3)
            self._display.pixel(x+15, y-4)
            # Line 17
            self._display.pixel(x+16, y)
            self._display.pixel(x+16, y-1)
            self._display.pixel(x+16, y-2)
            self._display.pixel(x+16, y-3)
            self._display.pixel(x+16, y-4)
            return y-7
        elif number == "2":
            return 0
        elif number == "3":
            return 0
        elif number == "4":
            return 0
        elif number == "5":
            return 0
        elif number == "6":
            return 0
        elif number == "7":
            return 0
        elif number == "8":
            return 0
        elif number == "9":
            return 0
        elif number == "0":
            # Line 1
            self._display.pixel(x, y-2)
            self._display.pixel(x, y-3)
            self._display.pixel(x, y-4)
            self._display.pixel(x, y-5)
            self._display.pixel(x, y-6)
            # Line 2
            self._display.pixel(x+1, y-1)
            self._display.pixel(x+1, y-2)
            self._display.pixel(x+1, y-3)
            self._display.pixel(x+1, y-4)
            self._display.pixel(x+1, y-5)
            self._display.pixel(x+1, y-6)
            self._display.pixel(x+1, y-7)
            # Line 3
            self._display.pixel(x+2, y)
            self._display.pixel(x+2, y-1)
            self._display.pixel(x+2, y-2)
            self._display.pixel(x+2, y-3)
            self._display.pixel(x+2, y-5)
            self._display.pixel(x+2, y-6)
            self._display.pixel(x+2, y-7)
            self._display.pixel(x+2, y-8)
            # Line 4
            self._display.pixel(x+3, y)
            self._display.pixel(x+3, y-1)
            self._display.pixel(x+3, y-2)
            self._display.pixel(x+3, y-6)
            self._display.pixel(x+3, y-7)
            self._display.pixel(x+3, y-8)
            # Line 5
            self._display.pixel(x+4, y)
            self._display.pixel(x+4, y-1)
            self._display.pixel(x+4, y-2)
            self._display.pixel(x+4, y-6)
            self._display.pixel(x+4, y-7)
            self._display.pixel(x+4, y-8)
            # Line 6
            self._display.pixel(x+5, y)
            self._display.pixel(x+5, y-1)
            self._display.pixel(x+5, y-2)
            self._display.pixel(x+5, y-6)
            self._display.pixel(x+5, y-7)
            self._display.pixel(x+5, y-8)
            # Line 7
            self._display.pixel(x+6, y)
            self._display.pixel(x+6, y-1)
            self._display.pixel(x+6, y-2)
            self._display.pixel(x+6, y-6)
            self._display.pixel(x+6, y-7)
            self._display.pixel(x+6, y-8)
            # Line 8
            self._display.pixel(x+7, y)
            self._display.pixel(x+7, y-1)
            self._display.pixel(x+7, y-2)
            self._display.pixel(x+7, y-6)
            self._display.pixel(x+7, y-7)
            self._display.pixel(x+7, y-8)
            # Line 9
            self._display.pixel(x+8, y)
            self._display.pixel(x+8, y-1)
            self._display.pixel(x+8, y-2)
            self._display.pixel(x+8, y-6)
            self._display.pixel(x+8, y-7)
            self._display.pixel(x+8, y-8)
            # Line 10
            self._display.pixel(x+9, y)
            self._display.pixel(x+9, y-1)
            self._display.pixel(x+9, y-2)
            self._display.pixel(x+9, y-6)
            self._display.pixel(x+9, y-7)
            self._display.pixel(x+9, y-8)
            # Line 11
            self._display.pixel(x+10, y)
            self._display.pixel(x+10, y-1)
            self._display.pixel(x+10, y-2)
            self._display.pixel(x+10, y-6)
            self._display.pixel(x+10, y-7)
            self._display.pixel(x+10, y-8)
            # Line 12
            self._display.pixel(x+11, y)
            self._display.pixel(x+11, y-1)
            self._display.pixel(x+11, y-2)
            self._display.pixel(x+11, y-6)
            self._display.pixel(x+11, y-7)
            self._display.pixel(x+11, y-8)
            # Line 13
            self._display.pixel(x+12, y)
            self._display.pixel(x+12, y-1)
            self._display.pixel(x+12, y-2)
            self._display.pixel(x+12, y-6)
            self._display.pixel(x+12, y-7)
            self._display.pixel(x+12, y-8)
            # Line 14---------------------------
            self._display.pixel(x+13, y)
            self._display.pixel(x+13, y-1)
            self._display.pixel(x+13, y-2)
            self._display.pixel(x+13, y-6)
            self._display.pixel(x+13, y-7)
            self._display.pixel(x+13, y-8)
            # Line 15
            self._display.pixel(x+14, y)
            self._display.pixel(x+14, y-1)
            self._display.pixel(x+14, y-2)
            self._display.pixel(x+14, y-3)
            self._display.pixel(x+14, y-4)
            # Line 16
            self._display.pixel(x+15, y)
            self._display.pixel(x+15, y-1)
            self._display.pixel(x+15, y-2)
            self._display.pixel(x+15, y-3)
            self._display.pixel(x+15, y-4)
            # Line 17
            self._display.pixel(x+16, y)
            self._display.pixel(x+16, y-1)
            self._display.pixel(x+16, y-2)
            self._display.pixel(x+16, y-3)
            self._display.pixel(x+16, y-4)
            return y-11
        else:
            return -1
    def draw(self, number, x, y):
        str_number = str(number)
        clear_height = 0
        for i in str_number:
            if i == "1":
                clear_height += self._one_height
            else:
                clear_height += self._others_height
        if self.bg_color != None:
            self.bg_color.enable_color()
            self._display.rectangle(x, y-clear_height, self._all_width, clear_height)
        self.fg_color.enable_color()
        next_y = y
        for i in str_number:
            next_y = self._draw_number(i, x, next_y)

class Legends:
    def __init__(self, display, fg_color, bg_color, game):
        self._display = display
        self.fg_color = fg_color
        self._game = game
        self._numbers = Numbers(display, fg_color, bg_color)
    def draw(self):
        self.fg_color.enable_color()
        # Points
        self._draw_word("points", 1, 133)
        self._numbers.draw(self._game.points, 11, 133)
        # Lines word
        self._draw_word("lines", 1, 60)
        self._numbers.draw(self._game.lines, 11, 60)
        # Level word
        self._draw_word("level", 31, 133)
        self._numbers.draw(self._game.level, 40, 133)
        # Next word
        self._draw_word("next", 61, 133)
    def _draw_word(self, word, x, y):
        next_y = y
        for letter in word:
            next_y = self._draw_letter(letter, x, next_y)
    def _draw_letter(self, letter, x, y):
        if letter == "e":
            # Line 1
            self._display.pixel(x, y)
            self._display.pixel(x, y-1)
            self._display.pixel(x, y-2)
            self._display.pixel(x, y-3)
            # Line 2
            self._display.pixel(x+1, y)
            # Line 3
            self._display.pixel(x+2, y)
            # Line 4
            self._display.pixel(x+3, y)
            self._display.pixel(x+3, y-1)
            self._display.pixel(x+3, y-2)
            # Line 5
            self._display.pixel(x+4, y)
            # Line 6
            self._display.pixel(x+5, y)
            # Line 7
            self._display.pixel(x+6, y)
            self._display.pixel(x+6, y-1)
            self._display.pixel(x+6, y-2)
            self._display.pixel(x+6, y-3)
            return y-6
        elif letter == "i":
            # Line 1
            self._display.pixel(x, y)
            # Line 2
            self._display.pixel(x+1, y)
            # Line 3
            self._display.pixel(x+2, y)
            # Line 4
            self._display.pixel(x+3, y)
            # Line 5
            self._display.pixel(x+4, y)
            # Line 6
            self._display.pixel(x+5, y)
            # Line 7
            self._display.pixel(x+6, y)
            return y-3
        elif letter == "l":
            # Line 1
            self._display.pixel(x, y)
            # Line 2
            self._display.pixel(x+1, y)
            # Line 3
            self._display.pixel(x+2, y)
            # Line 4
            self._display.pixel(x+3, y)
            # Line 5
            self._display.pixel(x+4, y)
            # Line 6
            self._display.pixel(x+5, y)
            # Line 7
            self._display.pixel(x+6, y)
            self._display.pixel(x+6, y-1)
            self._display.pixel(x+6, y-2)
            self._display.pixel(x+6, y-3)
            return y-6
        elif letter == "n":
            # Line 1
            self._display.pixel(x, y)
            self._display.pixel(x, y-4)
            # Line 2
            self._display.pixel(x+1, y)
            self._display.pixel(x+1, y-1)
            self._display.pixel(x+1, y-4)
            # Line 3
            self._display.pixel(x+2, y)
            self._display.pixel(x+2, y-1)
            self._display.pixel(x+2, y-4)
            # Line 4
            self._display.pixel(x+3, y)
            self._display.pixel(x+3, y-2)
            self._display.pixel(x+3, y-4)
            # Line 5
            self._display.pixel(x+4, y)
            self._display.pixel(x+4, y-3)
            self._display.pixel(x+4, y-4)
            # Line 6
            self._display.pixel(x+5, y)
            self._display.pixel(x+5, y-3)
            self._display.pixel(x+5, y-4)
            # Line 7
            self._display.pixel(x+6, y)
            self._display.pixel(x+6, y-4)
            return y-7
        elif letter == "o":
            # Line 1
            self._display.pixel(x, y-1)
            self._display.pixel(x, y-2)
            # Line 2
            self._display.pixel(x+1, y)
            self._display.pixel(x+1, y-3)
            # Line 3
            self._display.pixel(x+2, y)
            self._display.pixel(x+2, y-3)
            # Line 4
            self._display.pixel(x+3, y)
            self._display.pixel(x+3, y-3)
            # Line 5
            self._display.pixel(x+4, y)
            self._display.pixel(x+4, y-3)
            # Line 6
            self._display.pixel(x+5, y)
            self._display.pixel(x+5, y-3)
            # Line 7
            self._display.pixel(x+6, y-1)
            self._display.pixel(x+6, y-2)
            return y-6
        elif letter == "p":
            # Line 1
            self._display.pixel(x, y)
            self._display.pixel(x, y-1)
            self._display.pixel(x, y-2)
            # Line 2
            self._display.pixel(x+1, y)
            self._display.pixel(x+1, y-3)
            # Line 3
            self._display.pixel(x+2, y)
            self._display.pixel(x+2, y-3)
            # Line 4
            self._display.pixel(x+3, y)
            self._display.pixel(x+3, y-1)
            self._display.pixel(x+3, y-2)
            # Line 5
            self._display.pixel(x+4, y)
            # Line 6
            self._display.pixel(x+5, y)
            # Line 7
            self._display.pixel(x+6, y-1)
            return y-6
        elif letter == "s":
            # Line 1
            self._display.pixel(x, y-1)
            self._display.pixel(x, y-2)
            self._display.pixel(x, y-2)
            # Line 2
            self._display.pixel(x+1, y)
            # Line 3
            self._display.pixel(x+2, y)
            # Line 4
            self._display.pixel(x+3, y-1)
            self._display.pixel(x+3, y-2)
            # Line 5
            self._display.pixel(x+4, y-3)
            # Line 6
            self._display.pixel(x+5, y-3)
            # Line 7
            self._display.pixel(x+6, y)
            self._display.pixel(x+6, y-1)
            self._display.pixel(x+6, y-2)
            return y-6
        elif letter == "t":
            # Line 1
            self._display.pixel(x, y)
            self._display.pixel(x, y-1)
            self._display.pixel(x, y-2)
            self._display.pixel(x, y-3)
            self._display.pixel(x, y-4)
            # Line 2
            self._display.pixel(x+1, y-2)
            # Line 3
            self._display.pixel(x+2, y-2)
            # Line 4
            self._display.pixel(x+3, y-2)
            # Line 5
            self._display.pixel(x+4, y-2)
            # Line 6
            self._display.pixel(x+5, y-2)
            # Line 7
            self._display.pixel(x+6, y-2)
            return y-7
        elif letter == "v":
            # Line 1
            self._display.pixel(x, y)
            self._display.pixel(x, y-4)
            # Line 2
            self._display.pixel(x+1, y)
            self._display.pixel(x+1, y-4)
            # Line 3
            self._display.pixel(x+2, y)
            self._display.pixel(x+2, y-4)
            # Line 4
            self._display.pixel(x+3, y)
            self._display.pixel(x+3, y-4)
            # Line 5
            self._display.pixel(x+4, y)
            self._display.pixel(x+4, y-4)
            # Line 6
            self._display.pixel(x+5, y-1)
            self._display.pixel(x+5, y-3)
            # Line 7
            self._display.pixel(x+6, y-2)
            return y-7
        elif letter == "x":
            # Line 1
            self._display.pixel(x, y)
            self._display.pixel(x, y-4)
            # Line 2
            self._display.pixel(x+1, y)
            self._display.pixel(x+1, y-4)
            # Line 3
            self._display.pixel(x+2, y-1)
            self._display.pixel(x+2, y-3)
            # Line 4
            self._display.pixel(x+3, y-2)
            # Line 5
            self._display.pixel(x+4, y-1)
            self._display.pixel(x+4, y-3)
            # Line 6
            self._display.pixel(x+5, y)
            self._display.pixel(x+5, y-4)
            # Line 7
            self._display.pixel(x+6, y)
            self._display.pixel(x+6, y-4)
            return y-7
        else:
            return -1
class Board:
    def __init__(self,
        game, display, square_size=10, 
        x=33, y=2, width=200, height=100, draw_frame=True, draw_grid=False, 
        next_x=74, next_y=106, next_width=40, next_height=40,
        draw_next_piece=True, draw_next_frame=False, draw_legends=True):
        self._game = game
        self._width = width
        self._height = height
        self._display = display
        self._square_size = square_size
        self._x = x
        self._y = y
        self._next_x = next_x
        self._next_y = next_y
        self._next_width = next_width
        self._next_height = next_height
        self._draw_frame = draw_frame
        self.colors = Colors(display)
        self._frame = Frame(display, x - 2, y - 2, width + 4, height + 4, self.colors.white_fill, self.colors.black_fill)
        self._draw_grid  = draw_grid 
        self._grid = Grid(display, x, y, width, height, self.colors.white_fill)
        self._draw_next_frame  = draw_next_frame 
        self._next_frame = Frame(display, next_x - 2, next_y - 2, next_width + 4, next_height + 4, self.colors.white_fill, self.colors.black_fill)
        self._last_next_tetronimo = game._active_tetronimo
        if self._draw_frame:
            self._frame.draw()
        self._legends = Legends(display, self.colors.white_fill, self.colors.black_fill, game)
        self._draw_next_piece = draw_next_piece
        self._draw_legends = draw_legends
        if draw_legends:
            self._legends.draw()
        display.update()

    def _map_piece_type_to_color(self, piece_type):
        if piece_type == 0:
            return self.colors.black_fill
        elif piece_type == 1:
            return self.colors.white
        elif piece_type == 2:
            return self.colors.yellow
        elif piece_type == 3:
            return self.colors.magenta
        elif piece_type == 4:
            return self.colors.blue
        elif piece_type == 5:
            return self.colors.grey
        elif piece_type == 6:
            return self.colors.green
        elif piece_type == 7:
            return self.colors.red
        elif piece_type == 8:
            return self.colors.fuscia

    def _draw_next(self):
        if self._last_next_tetronimo != self._game.next_tetronimo:
            self._last_next_tetronimo = self._game.next_tetronimo
            if self._draw_next_frame:
                self._next_frame.draw()
            for x in range(4):
                for y in range(3):
                    Square(self._display, self._next_x + (x * self._square_size), self._next_y + (y * self._square_size), self.colors.black_fill).draw()
            for tile in self._last_next_tetronimo.current_tiles:
                Square(self._display, self._next_x + (tile[0] * self._square_size), self._next_y + (tile[1] * self._square_size), self._map_piece_type_to_color(self._last_next_tetronimo.type)).draw()

    def draw(self):
        for tile in self._game.changed_tiles:
            Square(self._display, self._x + (tile.x * self._square_size), self._y + (tile.y * self._square_size), self._map_piece_type_to_color(tile.piece.type)).draw()
        if self._draw_grid:
            self._grid.draw()
        if self._draw_next_piece:
            self._draw_next()
        self._display.update()
