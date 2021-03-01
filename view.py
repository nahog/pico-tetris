from model import Game
from char_letters import Letters
from char_numbers import Numbers

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

class Legends:
    def __init__(self, display, fg_color, bg_color, game):
        self._display = display
        self.fg_color = fg_color
        self._game = game
        self._numbers = Numbers(display, fg_color, bg_color)
        self._letters = Letters(display, fg_color)
    def draw(self):
        self.fg_color.enable_color()
        # Points
        self._letters.draw("points", 1, 133)
        self._numbers.draw(self._game.points, 11, 133)
        # Lines
        self._letters.draw("lines", 1, 30)
        self._numbers.draw(self._game.lines, 11, 30)
        # Level
        self._letters.draw("level", 31, 133)
        self._numbers.draw(self._game.level, 40, 133)
        # Next piece
        self._letters.draw("next", 61, 133)

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
        self._last_points = 0
        self._last_lines = 0
        self._last_level = 1
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
        if self._game.points != self._last_points or self._game.lines != self._last_lines or self._game.level != self._last_level:
            self._last_points = self._game.points
            self._last_lines = self._game.lines
            self._last_level = self._game.level
            if self._draw_legends:
                self._legends.draw()
        self._display.update()
