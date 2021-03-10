class Pin:
    def __init__(self, pin):
        self.pin = pin

class PWM:
    def __init__(self, pin):
        self.pin = pin
        self.duty_value = 0
        self.freq_value = 0
    def duty_u16(self, duty_value):
        self.duty_value = duty_value
    def freq(self, freq_value):
        self.freq_value = freq_value