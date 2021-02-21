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
        self.blank = Color(display, 0, 0, 0, gradient=False)

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
    def __init__(self, game, display, width=200, height=100, square_size=10):
        self._game = game
        self._width = width
        self._height = height
        self._display = display
        self._square_size = square_size

    def _map_piece_type_to_color(self, piece_type):
        colors = Colors(self._display)
        if piece_type == 0:
            return colors.blank
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
        for tile in self._game.tiles:
            Square(self._display, tile.x * self._square_size, tile.y * self._square_size, self._map_piece_type_to_color(tile.piece.type)).draw()