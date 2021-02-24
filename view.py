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

class Board:
    def __init__(self, game, display, x=10, y=10, width=200, height=100, square_size=10, draw_frame=True, draw_grid=True):
        self._game = game
        self._width = width
        self._height = height
        self._display = display
        self._square_size = square_size
        self._x = x
        self._y = y
        self._draw_frame = draw_frame
        colors = Colors(display)
        self._frame = Frame(display, x - 2, y - 2, width + 4, height + 4, colors.white_fill, colors.black_fill)
        self._draw_grid  = draw_grid 
        self._grid = Grid(display, x, y, width, height, colors.white_fill)
        if self._draw_frame:
            self._frame.draw()

    def _map_piece_type_to_color(self, piece_type):
        colors = Colors(self._display)
        if piece_type == 0:
            return colors.black_fill
        elif piece_type == 1:
            return colors.white
        elif piece_type == 2:
            return colors.yellow
        elif piece_type == 3:
            return colors.magenta
        elif piece_type == 4:
            return colors.blue
        elif piece_type == 5:
            return colors.grey
        elif piece_type == 6:
            return colors.green
        elif piece_type == 7:
            return colors.red
        elif piece_type == 8:
            return colors.fuscia

    def draw(self):
        for tile in self._game.changed_tiles:
            Square(self._display, self._x + (tile.x * self._square_size), self._y + (tile.y * self._square_size), self._map_piece_type_to_color(tile.piece.type)).draw()
        if self._draw_grid:
            self._grid.draw()