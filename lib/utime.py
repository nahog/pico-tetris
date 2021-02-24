import time

class MicroTime:

    def ticks_ms(self):
        return int(time.time() * 1000)