class Letters:

    def __init__(self, display, fg_color):
        self._display = display
        self.fg_color = fg_color

    def draw(self, word, x, y):
        self.fg_color.enable_color()
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
            return y-3
