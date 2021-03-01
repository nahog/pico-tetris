from .graphycs import GraphWin, Rectangle, Circle, Line, Point, color_rgb

# https://mcsp.wartburg.edu/zelle/python/graphics/graphics/graphref.html
# https://github.com/pimoroni/pimoroni-pico/tree/main/micropython/modules/pico_display

class PicoDisplay:

    def __init__(self):
        self.BUTTON_A = 0
        self.BUTTON_B = 1
        self.BUTTON_X = 2
        self.BUTTON_Y = 3
        self._button_a = False
        self._button_b = False
        self._button_x = False
        self._button_y = False
        self._canvas_width = 240
        self._canvas_height = 135
        self._win = GraphWin("Pico Display", self._canvas_width, self._canvas_height)
        self._lastKey = ''

    def init(self, buffer):
        self._buffer = buffer

    def get_height(self):
        return self._canvas_height

    def get_width(self):
        return self._canvas_width

    def set_backlight(self, brightness):
        self._backlight_brightness = brightness

    def set_led(self, r, g, b):
        self._led_r = r
        self._led_g = g
        self._led_b = b

    def is_pressed(self, button):
        keyString = self._win.checkKey()
        if keyString == 'a' or keyString == 'b' or keyString == 'x' or keyString == 'y':
            self._lastKey = keyString
        if self._lastKey == 'a' and button == self.BUTTON_A:
            self._lastKey = ''
            return True
        if self._lastKey == 'b' and button == self.BUTTON_B:
            self._lastKey = ''
            return True
        if self._lastKey == 'x' and button == self.BUTTON_X:
            self._lastKey = ''
            return True
        if self._lastKey == 'y' and button == self.BUTTON_Y:
            self._lastKey = ''
            return True
        return False

    def set_pen(self, r, g=0, b=0):
        if isinstance(r, tuple):
            b = r[2]
            g = r[1]
            r = r[0]
        self._pen_r = r
        self._pen_g = g
        self._pen_b = b

    def create_pen(self, r, g, b):
        return (r, g, b)

    def clear(self):
        rect = Rectangle(Point(0, 0), Point(self._canvas_width, self._canvas_height))
        rect.setFill(color_rgb(self._pen_r, self._pen_g, self._pen_b))
        rect.draw(self._win)

    def pixel(self, x, y):
        px = Point(x, y)
        px.setFill(color_rgb(self._pen_r, self._pen_g, self._pen_b))
        px.draw(self._win)

    def pixel_span(self, x, y, l):
        calc_l = x + l
        if (calc_l > self._canvas_width):
            calc_l = self._canvas_width
        line = Line(Point(x, y), Point(calc_l, y))
        line.setFill(color_rgb(self._pen_r, self._pen_g, self._pen_b))
        line.draw(self._win)

    def rectangle(self, x, y, w, h):
        rect = Rectangle(Point(x, y), Point(x + w, y + h))
        rect.setOutline(color_rgb(self._pen_r, self._pen_g, self._pen_b))
        rect.setFill(color_rgb(self._pen_r, self._pen_g, self._pen_b))
        rect.draw(self._win)

    def circle(self, x, y, r):
        circle = Circle(Point(x, y), r)
        circle.setOutline(color_rgb(self._pen_r, self._pen_g, self._pen_b))
        circle.setFill(color_rgb(self._pen_r, self._pen_g, self._pen_b))
        circle.draw(self._win)

    def character(self, char_a, x, y, scale):
        print("character not implemented: " + char_a)

    def text(self, string, x, y, wrap, scale):
        print("text not implemented: " + string)

    def set_clip(self, string, x, y, w, h):
        print("set_clip not implemented")

    def remove_clip(self):
        print("remove_clip not implemented")

    def update(self):
        return

    def keep_running(self):
        try:
            self._win.getMouse()
            self._win.close()
            self._win.close()
        except:
            pass
