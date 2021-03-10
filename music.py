# Based on https://github.com/robsoncouto/arduino-songs/blob/master/tetris/tetris.ino

class MusicPlayer:
    def __init__(self, tone, melody, tempo, volume = 50, loop=True):
        self._tone = tone
        self._volume = volume
        self._melody = melody
        self._wholenote = (60000 * 4) / tempo
        self._note_index = 0
        self._note_time = 0
        self._status = "stop"
        self._current_duty = 0
        self._current_freq = 0
        self._loop = loop

    def pluse(self):
        self._status = "pause"

    def stop(self):
        self._note_index = 0
        self._status = "stop"

    def play(self):
        self._status = "play"

    def _set_duty(self, duty):
        if self._current_duty != duty:
            self._current_duty = duty
            self._tone.duty_u16(duty)
    
    def _set_freq(self, freq):
        if self._current_freq != freq:
            self._current_freq = freq
            self._tone.freq(freq)

    def run(self, time_from_last_note):
        # Skip bad times
        if time_from_last_note > 5000:
            return
        if self._status != "play":
            return
        if self._note_index >= len(self._melody):
            self._note_index = 0
            self._note_time = 0
            if not self._loop:
                self._status = "stop"
                return

        # calculates the duration of each note
        divider = self._melody[self._note_index + 1]
        note_duration = 0
        if divider > 0:
            # regular note, just proceed
            note_duration = self._wholenote / divider
        elif divider < 0:
            # dotted notes are represented with negative durations!!
            note_duration = self._wholenote / abs(divider)
            note_duration *= 1.5 # increases the duration in half for dotted notes

        # we only play the note for 90% of the duration, 10% as a pause, if REST just wait the note
        curr_note = self._melody[self._note_index]
        if curr_note < 10:
            self._set_duty(0)
        else:
            self._set_duty(self._volume)
            self._set_freq(curr_note)

        if self._note_time < note_duration:
            self._note_time += time_from_last_note
        else:
            self._set_duty(0)
            self._note_index += 2
            self._note_time = self._note_time - note_duration
